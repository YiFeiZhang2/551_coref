cnn_conll_path = "cnn_0000.conll"
eng_conll_path = "eng_0000.conll"
train_path = "train.english.conll"
dev_path = "dev.english.conll"
test_path = "test.english.conll"

train_ratio = 0.75
dev_ratio = 0.1
test_ratio = 0.15

def read_conll(path):
    title = ""
    data = []
    sentence = []
    f = open(path, 'r')
    # last line is # document
    for line in f.readlines()[:-1]:
        if line[0] == "#":
            title = line.strip()
        elif line.strip() == "":
            data.append(sentence)
            sentence = []
        else:
            sentence.append(line.strip())

    return title, data

def split(data):
    train_data = []
    dev_data = []
    test_data = []
    num_sentences = len(data)
    for i in range(num_sentences):
        curr_proportion = float(i)/num_sentences

        if curr_proportion < train_ratio:
            train_data.append(data[i])
        elif curr_proportion < train_ratio + dev_ratio:
            dev_data.append(data[i])
        else:
            test_data.append(data[i])
    return train_data, dev_data, test_data

def write_document(title, data, f):
    f.write(title + "\n")
    f.write("\n")
    for sentence in data:
        f.write('\n'.join(sentence) + '\n')
        f.write("\n")
    f.write("#end document" + "\n")

cnn_title, cnn_data = read_conll(cnn_conll_path)
eng_title, eng_data = read_conll(eng_conll_path)

cnn_train, cnn_dev, cnn_test = split(cnn_data)
eng_train, eng_dev, eng_test = split(eng_data)

f_train = open(train_path, 'w')
write_document(cnn_title + " (train)", cnn_train, f_train)
write_document(eng_title + " (train)", eng_train, f_train)
f_train.close()

f_dev = open(dev_path, 'w')
write_document(cnn_title + " (dev)", cnn_dev, f_dev)
write_document(eng_title + " (dev)", eng_dev, f_dev)
f_dev.close()

f_test = open(test_path, 'w')
write_document(cnn_title +  " (test)", cnn_test, f_test)
write_document(eng_title +  " (test)", eng_test, f_test)
f_test.close()

