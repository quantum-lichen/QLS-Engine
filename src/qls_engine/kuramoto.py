import numpy as np

class KuramotoSimulator:
    def __init__(self, n_agents=496):
        self.n = n_agents
        # Fréquences naturelles ωi (Normal distribution)
        self.omegas = np.random.normal(1.0, 0.1, n_agents)
        # Matrice de couplage Kij initialisée à 0.5
        self.K = np.ones((n_agents, n_agents)) * 0.5

    def simulate(self, steps=1000, dt=0.01):
        """Équation : dθi/dt = ωi + Σ Kij * sin(θj - θi)"""
        thetas = np.random.uniform(0, 2*np.pi, self.n)
        
        for _ in range(steps):
            # Calcul des interactions
            # Utilisation de la vectorisation pour la performance
            theta_grid = np.tile(thetas, (self.n, 1))
            diff = theta_grid.T - theta_grid
            interactions = np.sum(self.K * np.sin(diff), axis=1)
            
            thetas += (self.omegas + interactions) * dt
            thetas = np.mod(thetas, 2 * np.pi)

        # Calcul de l'ordre global r
        r = np.abs(np.mean(np.exp(1j * thetas)))
        return float(r), thetas
