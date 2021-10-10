from app.tuple_to_spacy_converter import convert_to_spacy_format


def test_convert_to_spacy_format():
    data = [
        (['Positron', 'emission', 'tomography', 'in', 'a', 'case', 'of', 'intracranial', 'hemangiopericytoma', '.'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-Cancer', 'I-Cancer', 'O']),
        (['Due', 'to', 'the', 'low', 'prevalence', 'of', 'hemangiopericytomas', '(', 'HPCs', ')', ',', 'data', 'on',
          'the', 'biophysiological', 'characteristics', 'of', 'this', 'tumor', 'are', 'rare', '.'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'B-Cancer', 'O', 'B-Cancer', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
          'B-Cancer', 'O', 'O', 'O'])
    ]
    converted_data, labels = convert_to_spacy_format(data)
    print(converted_data)
    print(labels)
    for idx in range(len(converted_data)):
        sentence = converted_data[idx][0]
        entities = converted_data[idx][1]["entities"]
        assert len(data[idx][1]) == len(entities)  # for *2
        for entity_idx in range(len(entities)):
            entity = entities[entity_idx]
            token = data[idx][0][entity_idx]
            token_label = data[idx][1][entity_idx]
            # sentence_token = sentence[entity[0]:entity[1]+1]
            sentence_token = sentence[entity[0]:entity[1]]
            print(token, sentence_token.strip())
            assert token == sentence_token
            assert token_label == entity[2] or entity[2] == ""
