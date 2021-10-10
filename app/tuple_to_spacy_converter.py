import pickle


def convert_to_spacy_format(content:list):
    all_labels = set()
    data_in_spacy_format = []

    for tokens, labels in content:
        entities = []
        start = 0
        for idx in range(len(tokens)):
            token_start = start
            token_end = token_start + len(tokens[idx]) - 1
            label = labels[idx]
            label = '' if label == "O" else label
            all_labels.add(label) ###
            entities.append((token_start, token_end+1, label))
            # entities.append((token_end+1, token_end+1, ""))
            start = token_end + 2 # added 1 for space and 1 for next index = Total 2

        all_entities = {"entities": entities}
        sentence = " ".join(tokens)
        data_in_spacy_format.append((sentence,all_entities))
        if "O" in all_labels:
            all_labels.remove("O")
    return data_in_spacy_format, list(all_labels)


if __name__ == '__main__':
    with open('../lifebit-nlp-data/test.pkl', 'rb') as fp:
        data = pickle.load(fp)
        for i in range(len(data)):
            print(data[i])
            if i == 2:
                break
        print('==================')
        #print(convert_to_spacy_format((TRAIN_DATA[0:2])))

        converted_data, labels = convert_to_spacy_format(data[0:100])
        print(converted_data)
        print(labels)
        for idx in range(len(converted_data)):
            sentence= converted_data[idx][0]
            entities = converted_data[idx][1]["entities"]
            assert len(data[idx][1]) == len(entities) # for *2
            for entity_idx in range(len(entities)):
                entity = entities[entity_idx]
                token = data[idx][0][entity_idx]
                token_label = data[idx][1][entity_idx]
                sentence_token = sentence[entity[0]:entity[1]]
                print(token, sentence_token)
                assert token == sentence_token
                assert token_label == entity[2] or entity[2] == ""
