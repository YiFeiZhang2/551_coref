import json
import util
from allennlp import pretrained
from allennlp.commands import evaluate
import conll
import coref_model as cm
import metrics

# config = util.initialize_from_env()
# print(config)
# model = cm.CorefModel(config)
# coref_evaluator = metrics.CorefEvaluator()


# def interpret(resultsObj):
#     #[[[0, 1], [24, 24], [36, 36], [47, 47], [54, 54]], [[11, 11], [33, 33]], [[38, 39], [56, 56]], [[54, 56], [62, 62], [70, 70]]]
#     for cluster in resultsObj['clusters']:
#         #[[0, 1], [24, 24], [36, 36], [47, 47], [54, 54]]
#         print("New cluster")
#         for span in cluster:
#             #[0, 1]
#             print(resultsObj['document'][span[0]:span[1] + 1])


# with open('dev.english.jsonlines') as f:
#     train_examples = [json.loads(jsonline) for jsonline in f.readlines()]

# # get list of sentences for allen input
# allen_inputs = []
# for sentence in train_examples[0]['sentences']:
#     newval = ''
#     for word in sentence:
#         if "'" in word or word in [",", ".", "!", ";", ":", "-", "?"] or (len(newval) > 0 and newval[-1] is '-'):
#             newval = newval + word
#         else:
#             newval = newval + ' ' + word
#     allen_inputs.append(newval)

# allen_coref_predictions = {}
# allen_model = pretrained.neural_coreference_resolution_lee_2017()

# evaluate.evaluate(allen_model, )
# 'dev.english.conll'
# for sentence in allen_inputs:
#     allen_result = allen_model.predict(sentence)
# index = 0
# for cur_sentence in allen_inputs:
#     allen_result = allen_model.predict(cur_sentence)
#     top_span_ends_allen = []
#     top_span_starts_allen = []
#     for span in allen_result["top_spans"]:
#         top_span_starts_allen.append(span[0])
#         top_span_ends_allen.append(span[1])
#     allen_coref_predictions[str(index)] = model.evaluate_coref(top_span_starts_allen, top_span_ends_allen,
#                                                                allen_result["predicted_antecedents"], allen_result["clusters"], coref_evaluator)
#     index += 1
# allen_conll_results = conll.evaluate_conll(
#     model.config["conll_eval_path"], allen_coref_predictions, False)
# allen_average_f1 = sum(
#     results["f"] for results in allen_conll_results.values()) / len(allen_conll_results)
# print(allen_average_f1)
