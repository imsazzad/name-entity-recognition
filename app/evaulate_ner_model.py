import pickle
from argparse import ArgumentParser

import spacy
from spacy.scorer import Scorer
from spacy.training.example import Example

from tuple_to_spacy_converter import convert_to_spacy_format


def evaluate(model, validation_data):
    scorer = Scorer()
    examples = []
    for input_, annotations in validation_data:
        prediction = model(input_)
        print(prediction)
        for ent in prediction.ents:
            print(ent.label_, ent.text)
        example = Example.from_dict(prediction, dict.fromkeys(annotations))
        examples.append(example)
    scores = scorer.score(examples)
    return scores


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename",
                        help="FILE to read test data from")
    parser.add_argument("-d", "--dir",
                        dest="directory",
                        help="directory to read the training model from"
                        )

    args = parser.parse_args()
    if not args.filename:
        args.filename = "../lifebit-nlp-data/test.pkl"

    if not args.directory:
        args.directory = "model/"

    with open(args.filename, 'rb') as fp:
        data = pickle.load(fp)
        converted_data, labels = convert_to_spacy_format(data)

    output_dir = args.directory
    print("Loading from", output_dir)
    ner_model = spacy.load(output_dir)

    results = evaluate(ner_model, converted_data)
    print(results)
