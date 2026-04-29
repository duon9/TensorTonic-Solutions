import numpy as np

def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    reference_counts = np.asarray(reference_counts) / sum(reference_counts)
    production_counts = np.asarray(production_counts) / sum(production_counts)

    score = np.sum(np.abs(reference_counts - production_counts)) / 2

    return {
        "score" : score,
        "drift_detected" : bool(score > threshold)
    }