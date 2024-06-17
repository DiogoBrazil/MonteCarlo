import numpy as np

class MonteCarloSimulator:
    @staticmethod
    def calculate_team_strength(stats):
        strength = (0.2 * stats["Posse de bola (%)"] +
                    0.2 * stats["Total de passes"] / 100 +
                    0.2 * stats["Passes corretos (%)"] +
                    0.1 * stats["Total de chutes"] +
                    0.1 * stats["Chutes no gol"] +
                    0.1 * stats["Escanteios"] -
                    0.1 * stats["Faltas cometidas"])
        return strength

    @staticmethod
    def simulate_game(team1_strength, team2_strength):
        # Isto gera um número aleatório que representa o número de gols do Time
        team1_score = np.random.poisson(team1_strength)
        team2_score = np.random.poisson(team2_strength)
        if team1_score > team2_score:
            return 'team1'
        elif team2_score > team1_score:
            return 'team2'
        else:
            return 'draw'

    @staticmethod
    def monte_carlo_simulation(team1_strength, team2_strength, num_simulations=1000):
        results = {'team1': 0, 'team2': 0, 'draw': 0}
        for _ in range(num_simulations):
            result = MonteCarloSimulator.simulate_game(team1_strength, team2_strength)
            results[result] += 1
        return results
