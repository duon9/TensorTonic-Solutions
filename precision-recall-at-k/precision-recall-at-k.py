import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recommended = np.array(recommended)
    relevant = np.array(relevant)

    recommended_k = recommended[:k]
    nominator = np.sum(np.isin(recommended_k, relevant))
    precision_k = nominator / k
    recall_k = nominator / len(relevant)

    return [precision_k, recall_k]