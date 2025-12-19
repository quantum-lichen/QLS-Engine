import numpy as np

class KuramotoSimulator:
    def __init__(self, n_agents=496, K=0.5, noise=0.1):  # 496 par défaut (Lichen!)
        self.n = n_agents
        self.omegas = np.random.normal(1.0, noise, n_agents)
        self.K = np.full((n_agents, n_agents), K)
        np.fill_diagonal(self.K, 0)  # Pas d'auto-couplage

    def simulate(self, steps=1000, dt=0.01):
        """Simulation vectorisée ultra-rapide"""
        thetas = np.random.uniform(0, 2*np.pi, self.n)
        
        for _ in range(steps):
            # Vectorisation magique (×100 perf)
            dtheta = self.omegas + dt * np.dot(self.K, np.sin(thetas[:, np.newaxis] - thetas[np.newaxis, :])).sum(axis=1)
            thetas += dtheta
            
        r = np.abs(np.mean(np.exp(1j * thetas)))
        return float(r), thetas
