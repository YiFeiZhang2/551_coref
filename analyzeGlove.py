import numpy as np
import collections
import util

config = util.initialize_from_env()
context_embeddings = util.EmbeddingDictionary(
    config["context_embeddings"])
head_embeddings = util.EmbeddingDictionary(
    config["head_embeddings"], maybe_cache=context_embeddings)
print(head_embeddings._embeddings.keys()[:100])
