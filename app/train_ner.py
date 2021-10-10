from __future__ import unicode_literals, print_function
from random import random
from argparse import ArgumentParser
import logging
import pickle
import random
from pathlib import Path
import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding
from tuple_to_spacy_converter import convert_to_spacy_format

spacy.prefer_gpu()
logging.basicConfig(level=logging.INFO)


def load_or_create_model(model):
    if model is not None:
        nlp = spacy.load(model)  # load existing spacy model
        logging.info("Loaded model " + model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        logging.info("Created blank 'en' model")
    return nlp


def get_optimizer(model, nlp):
    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.resume_training()
    return optimizer


def save_model(new_model_name, nlp, output_dir, test_text):
    # Save model
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        logging.info("Saved model to" + str(output_dir))

        # Test the saved model
        logging.info("Loading from " + str(output_dir))
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            logging.info(ent.label_ + " " + ent.text)


def check_performance_of_model(nlp, test_text):
    # Test the trained model

    doc = nlp(test_text)
    logging.info("Entities in " + test_text)
    for ent in doc.ents:
        logging.info(ent.label_ + " " + ent.text)


def parse_args_and_load_vars():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename",
                        help="FILE to read training data from")
    parser.add_argument("-d", "--dir",
                        dest="directory",
                        help="directory to write the training model"
                        )

    args = parser.parse_args()
    if not args.filename:
        args.filename = "../lifebit-nlp-data/train.pkl"

    if not args.directory:
        args.directory = "model/"
    return args


def main(data, labels, output_dir, model=None, new_model_name='new_model', n_iter=10):
    """Setting up the pipeline and entity recognizer, and training the new entity."""
    nlp = load_or_create_model(model)

    if 'ner' not in nlp.pipe_names:
        nlp.add_pipe("ner")

    ner = nlp.get_pipe('ner')

    for i in labels:
        ner.add_label(i)  # Add new entity labels to entity recognizer

    optimizer = get_optimizer(model, nlp)

    # Get names of other pipes to disable them during training to train only NER
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    prev_loss = float("inf")
    test_text = 'Positron emission tomography in a case of intracranial hemangiopericytoma .'
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for _ in range(n_iter):
            random.shuffle(data)
            losses = {}
            batches = minibatch(data, size=compounding(4., 32., 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                example = []
                # Update the model with iterating each text
                for i in range(len(texts)):
                    doc = nlp.make_doc(texts[i])
                    example.append(Example.from_dict(doc, annotations[i]))

                # Update the model
                nlp.update(example, drop=0.5, losses=losses, sgd=optimizer)

            logging.info('Losses ' + str(losses))
            if prev_loss > float(losses["ner"]):
                prev_loss = float(losses["ner"])
                logging.info("Model improved")
                save_model(new_model_name, nlp, output_dir, test_text)

    check_performance_of_model(nlp, test_text)
    save_model(new_model_name, nlp, output_dir, test_text)


if __name__ == '__main__':
    args = parse_args_and_load_vars()
    with open(args.filename, 'rb') as fp:
        training_data = pickle.load(fp)
    print("length of training data", len(training_data))
    converted_data, all_labels = convert_to_spacy_format(training_data)
    logging.info("These are all levels")
    logging.info(all_labels)
    main(data=converted_data, labels=all_labels, output_dir=args.directory, n_iter=1000, model="app/best_model/")
