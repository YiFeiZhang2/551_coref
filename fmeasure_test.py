import json 
from allennlp import pretrained

with open('dev.english.jsonlines') as f:
      train_examples = [json.loads(jsonline) for jsonline in f.readlines()]
    
#get list of sentences for allen input 
allen_inputs = []
for sentence in train_examples[0]['sentences']: 
    string = ''
    for word in sentence: 
        if "'" in word or word in [",", ".", "!", ";", ":"]: 
            string = string + word 
        else:
            string = string + ' ' +word 
        allen_inputs.append(string)
allen_coref_predictions = {}
allen_model = pretrained.neural_coreference_resolution_lee_2017()
index = 0
for cur_sentence in allen_inputs
    allen_result = allen_model.predict(cur_sentence) 
    top_span_ends_allen = []
    top_span_starts_allen = []
    for span in allen_result["top_spans"]
        top_span_ends_allen.append(span[1])
    allen_coref_predictions[str(index)] = self.evaluate_coref(top_span_starts_allen, top_span_ends_allen, allen_result["predicted_antecedents"], allen_result["clusters"], coref_evaluator)

allen_conll_results = conll.evaluate_conll(self.config["conll_eval_path"], allen_coref_predictions, official_stdout)
allen_average_f1 = sum(results["f"] for results in allen_conll_results.values()) / len(allen_conll_results)
print(allen_average_f1)
