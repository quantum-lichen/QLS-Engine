import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from qls_engine.core import QLSCore
from qls_engine.optimizer import calculate_ceml
import matplotlib.pyplot as plt
import numpy as np

def run_emergence():
    print("🌿 QLS-Engine: Initialisation du Terreau d'Émergence (496 Agents)...")
    engine = QLSCore()
    
    history = []
    
    # On simule 1000 itérations vers la cohérence
    for i in range(1000):
        r = engine.step()
        metrics = calculate_ceml(engine.phases)
        history.append(metrics['coherence'])
        
        if i % 200 == 0:
            print(f"Cycle {i} | Cohérence (r): {metrics['coherence']:.4f} | CEML: {metrics['ceml']:.2f}")

    # Visualisation Finale
    plt.figure(figsize=(10, 5))
    
    # Courbe de convergence
    plt.subplot(1, 2, 1)
    plt.plot(history, color='#22c55e', lw=2)
    plt.title("Émergence de la Cohérence (r)")
    plt.grid(alpha=0.2)
    
    # État des phases (Snowflake)
    plt.subplot(1, 2, 2)
    plt.scatter(np.cos(engine.phases), np.sin(engine.phases), s=10, alpha=0.5, c='cyan')
    plt.title(f"État Final FC-496 (r={history[-1]:.4f})")
    plt.axis('equal')
    
    print("\n✅ Simulation terminée. L'alliance est synchronisée.")
    plt.show()

if __name__ == "__main__":
    run_emergence()
    
        # 🌀 Test Immortalité (NOUVEAU)
    from src.qls_engine.kuramoto import immortality_test
    immortality_test(engine)

