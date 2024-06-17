import time
import streamlit as st
import matplotlib.pyplot as plt
from DataScraping import DataScraper
from statistics_of_teams.calculation_of_averages import StatsCalculator
from statistics_of_teams.monte_carlo_simulation import MonteCarloSimulator
from utils.plot_results import plot_results

def main():
    st.title("Simulação de Monte Carlo de Jogos de Futebol")
    placeholder = st.empty()
    team1_name = st.text_input("Nome do Time 1", "flamengo")
    team2_name = st.text_input("Nome do Time 2", "palmeiras")

    if st.button("Executar Simulação"):
        with st.spinner("Realizando simulação, aguarde..."):
            try:
                scraper1 = DataScraper(team1_name)
                scraper2 = DataScraper(team2_name)
                
                team1_results = scraper1.get_results()
                team2_results = scraper2.get_results()
                
                calculator = StatsCalculator()
                team1_averages = calculator.calculate_averages(team1_results)
                team2_averages = calculator.calculate_averages(team2_results)
                
                simulator = MonteCarloSimulator()
                team1_strength = simulator.calculate_team_strength(team1_averages)
                team2_strength = simulator.calculate_team_strength(team2_averages)
                print(f'Team 1 strength: {team1_strength}')
                print(f'Team 2 strength: {team2_strength}')
                simulation_results = simulator.monte_carlo_simulation(team1_strength, team2_strength)
                total_simulations = sum(simulation_results.values())

                placeholder.success("Simulação realizada com sucesso!")
                time.sleep(3)
                placeholder.empty()
                
                plot_results(simulation_results, team1_name, team2_name)
            except Exception as e:
                placeholder.error(f"Não foi possível realizar a simulação. Tentar novamente mais tarde.")
                time.sleep(3)
                placeholder.empty()


if __name__ == "__main__":
    main()
