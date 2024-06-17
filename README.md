# Simulação de Monte Carlo para Previsão de Resultados de Jogos de Futebol

O projeto tem por objetivo realizar o cálculo da simulação de Monte Carlo e ter como resultado a probabilidade de um confronto entre dois times, prevendo a vitória de um deles ou o empate.

## Descrição do Projeto

Os parâmetros passados para realizar os cálculos são a possível força do time. Uma raspagem de dados na web é feita, trazendo as seguintes estatísticas dos últimos 5 jogos de cada time:

- Posse de bola (%)
- Total de passes
- Passes corretos (%)
- Total de chutes
- Chutes no gol
- Escanteios
- Faltas cometidas

Uma média é calculada desses últimos 5 jogos. Em seguida, usando esses parâmetros, é calculada a força do time aplicando graus de importância para cada parâmetro (0.2 e 0.1).

Essa força é repassada para a função que faz o cálculo de Monte Carlo para prever um número aleatório que representa a quantidade de gols, usando para isso a distribuição de Poisson.

As probabilidades de vitória de cada time e de empate são calculadas dividindo o número de ocorrências de cada resultado pelo número total de simulações

Ao final, é gerado um gráfico com as probabilidades.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/DiogoBrazil/monte-carlo-simulation.git

2. Navegue até o diretório do projeto:

```bash
cd monte-carlo-simulation

3. Crie um ambiente virtual e ative-o:

```bash
python -m venv env
source env/bin/activate  # No Windows, use `env\\Scripts\\activate`

4. Instale as dependências:

```bash
pip install -r requirements.txt

## Autor

- **Diogo Ribeiro** - [GitHub](https://github.com/DiogoBrazil)
