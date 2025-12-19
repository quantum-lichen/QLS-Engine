import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ceml(phases):
    """Cognitive Entropy Minimization Law - Lichen Edition"""
    # Phases → embeddings 2D (angle + radius)
    embeddings = np.column_stack([np.cos(phases), np.sin(phases)])
    
    sim_matrix = cosine_similarity(embeddings)
    coherence = np.mean(np.triu(sim_matrix, k=1))  # Triangulaire sup
    
    # Entropie informationnelle
    entropy = -np.sum(sim_matrix * np.log(sim_matrix + 1e-10), axis=1).mean()
    
    ceml_score = coherence / (entropy + 0.01)
    return float(ceml_score)
