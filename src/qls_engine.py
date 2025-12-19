from .kuramoto import KuramotoSimulator
from .ceml import calculate_ceml

class QLSEngine:
    def __init__(self, n_agents=496):
        self.simulator = KuramotoSimulator(n_agents)
    
    def run_simulation(self, steps=1000):
        r, thetas = self.simulator.simulate(steps)
        ceml = calculate_ceml(thetas)
        return {"coherence": r, "ceml": ceml, "phases": thetas}
