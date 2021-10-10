# Model used for training
Here Spacy is used for training ner.

Please Read **docs/Training Documentation.md** to get details about 
 - ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+)  **Training, Issues, Next Steps** 

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
Though I have saved my model in the 'best_model' directory.

run the following command from project root
- -f for validation data file
- -d for from where to load the saved model
- 
`python app/evaulate_ner_model.py -f lifebit-nlp-data/test.pkl -d app/best_model/`
or 
`python app/evaulate_ner_model.py -f lifebit-nlp-data/test.pkl -d app/google_colab_model/`

Folder Structure
============================

### top-level directory layout

    .
    ├── app                     # all the source code to run NER, test the model and preprocessing 
    ├── docs                    # Documentation details about model and training
    ├── lifebit-nlp-data        # train and test data
    ├── test                    # unit test of the preprocessing script
    ├── venv                    # python                  
    ├── .gitignore              # gitignore                  
    ├── requirments.txt         # all dependencies list                  
    ├── Train_NER___lifebit.ipynb  # notebook created for google colab                
    └── README.md               # project documenation



### Source files
    .
    ├── ...
    ├── app
    │   ├── __init__.py
    │   ├── train_ner.py                        # script to run custom training on the biomedical data using spacy
    │   ├── evaulate_ner_model.py               # script to test the performance on the unseen data
    │   ├── tuple_to_spacy_converter.py         # converts training data to spacy formatted training data
    │   ├── best_model                          # saved best model ( manual save)
    │   ├── google_colab_model                  # model that trained on google colab
    │   └── model                               # saved model directory for future run
    └── ...


### Tests files
    .
    ├── ...
    ├── test
    │   ├── __init__.py         
    │   └── test_tuple_to_spacy_converter.py                # Unit tests for data processing
    └── ...

### Data folder
    .
    ├── ...
    ├── lifebit-nlp-data
    │   ├── test.pkl                # test data file 
    │   └── train.pkl               # training data file
    └── ...

### Documentation files
    .
    ├── ...
    ├── docs
    │   ├── Training Documentation.md # Brief discussion about Training
    └── ...