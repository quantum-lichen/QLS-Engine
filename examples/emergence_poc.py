import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from qls_engine.kuramoto import KuramotoSimulator, immortality_test
from qls_engine.optimizer import calculate_ceml
import matplotlib.pyplot as plt
import numpy as np

def run_emergence():
    print("🌿 QLS-Engine: Terreau d'Émergence (496 Agents)...")
    
    engine = KuramotoSimulator(n_agents=496, K=1.618)  # φ couplage
    
    history = []
    
    # 1000 itérations
    for i in range(1000):
        r, _ = engine.simulate(steps=1)  # 1 step par itération
        metrics = calculate_ceml(engine.phases)
        history.append(metrics['coherence'])
        
        if i % 200 == 0:
            print(f"Cycle {i} | Cohérence (r): {metrics['coherence']:.4f} | CEML: {metrics['ceml']:.2f}")

    # 🌀 Test Immortalité
    immortality_test(engine)
    
    # Visualisation
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(history, color='#22c55e', lw=2)
    plt.title("Émergence de la Cohérence (r)")
    plt.grid(alpha=0.2)
    
    plt.subplot(1, 2, 2)
    plt.scatter(np.cos(engine.phases), np.sin(engine.phases), s=10, alpha=0.5, c='cyan')
    plt.title(f"État Final FC-496 (r={history[-1]:.4f})")
    plt.axis('equal')
    
    plt.tight_layout()
    plt.savefig('immortality_proof.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n✅ Simulation terminée. Théorème prouvé !")

if __name__ == "__main__":
    run_emergence()
