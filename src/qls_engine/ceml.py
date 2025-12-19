import numpy as np

def calculate_ceml(phases, epsilon=0.01):
    """
    Calcule le score CEML (Cognitive Entropy Minimization Law).
    """
    # Cohérence : Moyenne des similarités cosinus
    coherence = np.abs(np.mean(np.exp(1j * phases)))
    
    # Entropie : Variance des phases (proxy)
    entropy = np.var(phases)
    
    ceml_score = coherence / (entropy + epsilon)
    return ceml_score, coherence, entropy
