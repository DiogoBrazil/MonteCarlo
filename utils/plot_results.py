import matplotlib.pyplot as plt
import streamlit as st

def plot_results(results, team1_name, team2_name):
    labels = [f"Vitória do {team1_name}", "Empate", f"Vitória do {team2_name}"]
    counts = [results['team1'], results['draw'], results['team2']]
    total = sum(counts)
    probabilities = [count / total for count in counts]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(labels, probabilities, color=['blue', 'gray', 'red'])
    ax.set_ylabel('Probabilidade')
    ax.set_title('Resultado da Simulação de Monte Carlo')
    ax.set_ylim(0, 1)  # Define o limite do eixo y de 0 a 1
    ax.set_yticks([i * 0.1 for i in range(11)])  # Define os ticks do eixo y de 0 a 1 com passos de 0.1
    for i, v in enumerate(probabilities):
        ax.text(i, v + 0.02, f"{v:.2%}", ha='center')  # Adiciona texto com a probabilidade acima das barras

    st.pyplot(fig)