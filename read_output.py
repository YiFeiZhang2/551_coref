import matplotlib.pyplot as plt

output_path = 'train_output.txt'
prev_output_path = 'train_output_prev.txt'

def read_single_line(line):
    '''
    reads the percentage at the end of the line, stripping away the percentage sign and leading spaces
    '''
    return float(line.strip()[-6:-1].strip())

f = open(output_path, 'r')
conll_f1s = []
py_f1s = []
py_precs = []
py_recalls = []
all_lines = f.readlines()

for i in range(0, len(all_lines), 5):
    conll_f1s.append(read_single_line(all_lines[i]))
    py_f1s.append(read_single_line(all_lines[i+1]))
    py_precs.append(read_single_line(all_lines[i+2]))
    py_recalls.append(read_single_line(all_lines[i+3]))

num_epocs = len(all_lines)/5
X = range(1, 200)

plt.title("Elmo Validation Performance Over Epochs")
plt.plot(X, py_f1s, label = "F1")
plt.plot(X, py_precs, label = "Precision")
plt.plot(X, py_recalls, label = "Recall")
plt.ylabel("Score")
plt.xlabel("Epoch number")
plt.legend(bbox_to_anchor=(0, 1), loc='upper left')
plt.show()
# print(len(conll_f1s), len(py_f1s), len(py_precs), len(py_recalls))


    




