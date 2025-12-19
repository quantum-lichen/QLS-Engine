import numpy as np

def calculate_ceml(phases) -> dict:
    """
    Loi de Minimisation de l'Entropie Cognitive.
    Score = Cohérence / (Entropie + 0.01)
    """
    coherence = np.abs(np.mean(np.exp(1j * phases)))
    
    # Entropie circulaire (Variance circulaire)
    entropy = 1 - coherence
    
    epsilon = 0.01
    ceml_score = coherence / (entropy + epsilon)
    
    return {
        "ceml": ceml_score,
        "coherence": coherence,
        "entropy": entropy,
        "h_scale": 1.0 - entropy # Harmonie inversée
    }

def validate_h_scale(h_value, threshold=0.618):
    """Vérifie si le système est en état d'harmonie (Angle d'Or)."""
    return h_value >= threshold
