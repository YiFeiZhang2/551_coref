import json

with open('dev.english.jsonlines') as f:
    
    train_examples = [json.loads(jsonline) for jsonline in f.readlines()]
allen_inputs = []
for sentence in train_examples[0]['sentences']: 
    string = ''
    for word in sentence: 
        if "'" in word or word == "," or word == "." or word =="!" or word == ";" or word ==":": 
            string = string + word 
        else:
            string = string + ' ' +word 


