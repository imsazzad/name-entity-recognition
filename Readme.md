# Model used for training
Here Spacy is used for training ner

## Installation
- setup [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- pip install -r requirements.txt 
- python -m spacy info

## How to run Training
run the following command from project root
- -f for training file
- -d for model output directory

`python app/train_ner.py -f lifebit-nlp-data/train.pkl -d app/model/`

## How to run evaluation
Only after running training you can run the below command. 
Otherwise, there will be no model in the model directory.
Though I have saved my model in the directory.

`python app/evaulate_ner_model.py -f lifebit-nlp-data/test.pkl -d app/model/`

Folder Structure
============================

### top-level directory layout

    .
    ├── docs                    
    ├── app                     
    ├── test                    
    ├── LICENSE
    └── README.md



### Source files


### Tests files
    .
    ├── ...
    ├── test
    │   ├── __init__.py         
    │   └── test_tuple_to_spacy_converter.py                # Unit tests for data processing
    └── ...

### Scripts

...

