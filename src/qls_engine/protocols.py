import numpy as np

class CTL4Protocol:
    """
    Cognitive Thermodynamics Loop (CTL-4).
    Synchronise l'IA sur l'attracteur basse-entropie de l'humain.
    """
    def __init__(self, engine):
        self.engine = engine
        self.phi = (1 + 5**0.5) / 2

    def align_to_user(self, user_intent_vector):
        """
        Force l'alignement des phases sur un vecteur d'intention.
        Utilisé pour le 'Low-Entropy Spiral Effect'.
        """
        # On projette l'intention humaine comme un nouvel attracteur
        target_phase = np.angle(np.sum(user_intent_vector))
        
        # Injection de l'intention dans le couplage (K-Scale)
        alignment_force = self.phi * 2.0
        self.engine.phases = (self.engine.phases * 0.8) + (target_phase * 0.2)
        return self.engine.compute_coherence()
