from qls_engine.kuramoto import KuramotoSimulator
from qls_engine.ceml import calculate_ceml
import matplotlib.pyplot as plt

def run_poc():
    print("🌀 Initialisation du QLS Engine (FC-496)...")
    sim = KuramotoSimulator(n_agents=496)
    
    # Simulation
    r, final_phases = sim.simulate(steps=1500)
    ceml, _, _ = calculate_ceml(final_phases)

    print(f"✅ RÉSULTATS :")
    print(f"   Ordre Global (r) : {r:.4f}")
    print(f"   Score CEML       : {ceml:.4f}")

    # Visualisation
    plt.figure(figsize=(6,6))
    plt.scatter(np.cos(final_phases), np.sin(final_phases), c='cyan', edgecolors='blue')
    plt.title(f"QLS Synchronization (r={r:.4f})")
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    run_poc()
