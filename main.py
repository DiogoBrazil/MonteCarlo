import numpy as np


# Simular o resultado de um jogo entre dois times
def simulate_game(team1_strength, team2_strength):
    team1_score = np.random.poisson(team1_strength)
    team2_score = np.random.poisson(team2_strength)
    if team1_score > team2_score:
        return 'team1'
    elif team2_score > team1_score:
        return 'team2'
    else:
        return 'draw'


# Executar a simulação de Monte Carlo
def monte_carlo_simulation(team1_strength, team2_strength, num_simulations=10000):
    results = {'team1': 0, 'team2': 0, 'draw': 0}
    for _ in range(num_simulations):
        result = simulate_game(team1_strength, team2_strength)
        results[result] += 1
    return results


# Exemplo de uso
team1_strength = 1.5  # Força do time 1 (exemplo)
team2_strength = 1.2  # Força do time 2 (exemplo)

results = monte_carlo_simulation(team1_strength, team2_strength)
total_simulations = sum(results.values())

print(f"Team 1 Win Probability: {results['team1'] / total_simulations:.2%}")
print(f"Team 2 Win Probability: {results['team2'] / total_simulations:.2%}")
print(f"Draw Probability: {results['draw'] / total_simulations:.2%}")
