from qls_engine.core import QLSCore
from qls_engine.optimizer import calculate_ceml

def test_quantum_stability():
    """Vérifie que le moteur atteint le seuil d'harmonie Bryan Ouellette."""
    engine = QLSCore(n_agents=496)
    
    # Simulation courte
    for _ in range(500):
        engine.step()
        
    metrics = calculate_ceml(engine.phases)
    # Le système doit converger vers r > 0.90 en 500 steps avec K=phi
    assert metrics['coherence'] > 0.90, f"Dissonance détectée : r={metrics['coherence']}"
    assert metrics['h_scale'] >= 0.618, "Le système n'a pas atteint l'Angle d'Or."
