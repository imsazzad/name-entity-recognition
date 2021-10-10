## Software Features
- **Custom Name Entity Recognition Training and Validation**
  - Argument parser :- you can pass the parameters from command line.
  - Training FileReader
  - Spacy formatted data converter
  - Unit tests to validate the code is right
  - Model Loader
    - you can train from blank model from the scratch
    - you can begin training from your saved model
  - Model Training
    - mini batch
    - set the epoch number
    - monitor loss
    - resolves overfitting issue
  - Model save
    - saves the best model
    - saves the final model
  - Model evaluator
    - validates the model performance with test data
    - log different metric like accuracy, precision, recall to show the model performance 

## Software best practices
1. Tried to write small methods
2. Ran SonarLint and pylint to find code smells and solved the issues
3. Tried to parameterize most of the dependencies
4. Wrote reusable code [ data processing is used in both training and evaluation]
5. made small commits
6. code is pushed int Github.
7. Tried to make meaningful variable names

## Scripts
- Training script
- Evaluation script
- Training data spacy-formatted data converter script


## How I trained my model
1. take processed_data, labels , saved model if any, num of iteration as input
2. load old model or create new model
3. added ner in nlp pipelines if it is already not added
4. disable the remaining pipelines while training
5. randomly shuffle data on each iteration
6. used mini batch for training
7. used dropout as regularization
8. monitored loss
9. if loss is decreased, best model is saved on each iteration

## Training on My Desktop [ No GPU] :(
1. took only 3000 sentences from training data to run NER training due to insufficient resources. 
2. run only 1100 epochs
3. starting loss - about 4000
4. end loss - #TODO

## Training on Google Colab [ GPU]

1. took full training data to run NER training. 
2. run only 1000 epochs.
3. starting loss - 642309.21634819
4. end loss - 589102.0629441325 #TODO


## Issue faced
1. Spacy takes annotation as **(start, end+1, LABEL)** but I was giving  **(start, end, LABEL)**. Noticed the issue 45 minutes later

## Next improvement target
1. Make training faster
2. Try other libraries also, not only Spacy
3. As loss is decreasing on each iteration and the model is still running not sure it will go how far. **But I ran the model on small data, it was doing really good.**
4. Only after full training on colab, I can say the model is doing good or not
5. As we have __huge__ data we can try **BERT/ELMO** to run training from scarth also