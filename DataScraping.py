import requests
from bs4 import BeautifulSoup
import re

class DataScraper:
    def __init__(self, team_name):
        self.team_name = team_name
        self.base_url = f"https://www.placardefutebol.com.br/time/{team_name}/ultimos-jogos"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.links_with_statistics = []
        self.results = []

    def fetch_game_links(self):
        main_page = requests.get(self.base_url, headers=self.headers)
        main_soup = BeautifulSoup(main_page.content, 'html.parser')
        main_search = main_soup.find_all('a', class_='match__lg')
        self.links_with_statistics = [link['href'] for link in main_search]

    def scrape_data(self):
        self.fetch_game_links()
        for link_with_statistics in self.links_with_statistics:
            page_with_statistics = requests.get(link_with_statistics, headers=self.headers)
            soup_with_statistics = BeautifulSoup(page_with_statistics.content, 'html.parser')

            match = re.search(r'(\d{2}-\d{2}-\d{4}-.+?-x-.+?).html', link_with_statistics)
            if match:
                relevant_part = match.group(1)
                teams = relevant_part.split('-x-')
                team1 = teams[0].split('-', 3)[-1]
                team2 = teams[1]

            if self.team_name == team1:
                td_tag = soup_with_statistics.find_all('td', class_='stats-home-team')
            else:
                td_tag = soup_with_statistics.find_all('td', class_='stats-away-team')

            small_texts = [td.find('small').get_text() for td in td_tag]

            stats_dict = {
                "Posse de bola (%)": int(small_texts[0]),
                "Total de passes": int(small_texts[1]),
                "Passes corretos (%)": int(small_texts[2]),
                "Total de chutes": int(small_texts[3]),
                "Chutes no gol": int(small_texts[4]),
                "Escanteios": int(small_texts[5]),
                "Faltas cometidas": int(small_texts[6])
            }

            self.results.append(stats_dict)

    def get_results(self):
        self.scrape_data()
        return self.results
