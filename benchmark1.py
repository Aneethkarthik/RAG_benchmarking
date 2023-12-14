from mteb import MTEB
import inspect


from abc import ABC, abstractmethod
from typing import List,Dict, Union
import numpy as np
from torch import tensor


class EmbedderModell(ABC):
    @abstractmethod
    def encode(self, sentences: List[str], batch_size: int = 32, **kwargs) -> List[Union[np.ndarray, tensor]]:
        """
        Returns a list of embeddings for the given sentences.

        Args:
            sentences (`List[str]`): List of sentences to encode.
            batch_size (`int`): Batch size for the encoding.

        Returns:
            `List[np.ndarray]` or `List[tensor]`: List of embeddings for the given sentences.
        """
        pass

class SelectiveEmbedderModell(ABC):
    @abstractmethod
    def encode_queries(self, queries: List[str], batch_size: int = 32, **kwargs) -> List[Union[np.ndarray, tensor]]:
        """
        Returns a list of embeddings for the given queries.

        Args:
            queries (`List[str]`): List of queries to encode.
            batch_size (`int`): Batch size for the encoding.

        Returns:
            `List[np.ndarray]` or `List[tensor]`: List of embeddings for the given queries.
        """
        pass

    @abstractmethod
    def encode_corpus(self, corpus: List[Union[str, Dict[str, str]]], batch_size: int = 32, **kwargs) -> List[Union[np.ndarray, tensor]]:
        """
        Returns a list of embeddings for the given corpus.

        Args:
            corpus (`List[str]` or `List[Dict[str, str]]`): List of sentences to encode
                or list of dictionaries with keys "title" and "text".
            batch_size (`int`): Batch size for the encoding.

        Returns:
            `List[np.ndarray]` or `List[tensor]`: List of embeddings for the given corpus.
        """
        pass


def benchmark_embedder(embedder:SelectiveEmbedderModell|EmbedderModell):
    #TODO check if class is implemented correctly
    #if not issubclass(type(embedder), CustomModel):
    #    if not issubclass(type(embedder),CustomModel2):
    #        raise ValueError('There seems to be an implementation error with the modell. Prease revise if the nescessery calsses are implemented correctly.')
    evaluation = MTEB(tasks=['SciFact','FEVER','NQ'])
    results = evaluation.run(embedder,output_folder=None, eval_splits=['test'])
    return results

