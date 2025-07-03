import csv
from app.src.models.anime import Anime

class AnimeService:
    def __init__(self, csv_filepath):
        self.csv_filepath = csv_filepath
        self.animes = []
        self._load_animes_from_csv()

    def _load_animes_from_csv(self):
        try:
            with open(self.csv_filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Assumindo que seu CSV tem colunas como 'title', 'genre', 'episodes', 'synopsis'
                    anime = Anime(
                        title=row['title'],
                        genre=row['genre'],
                        episodes=int(row['episodes']), # Converter para int
                        synopsis=row['synopsis']
                    )
                    self.animes.append(anime)
        except FileNotFoundError:
            print(f"Erro: O arquivo CSV '{self.csv_filepath}' não foi encontrado.")
            self.animes = [] # Garante que a lista está vazia em caso de erro
        except KeyError as e:
            print(f"Erro: Coluna '{e}' não encontrada no CSV. Verifique o cabeçalho do arquivo.")
            self.animes = []
        except ValueError as e:
            print(f"Erro de valor ao processar o CSV: {e}. Verifique o formato dos dados.")
            self.animes = []


    def get_all_animes(self):
        return self.animes

    def search_animes_by_genre(self, genre):
        return [anime for anime in self.animes if genre.lower() in anime.genre.lower()]

    def get_anime_by_title(self, title):
        for anime in self.animes:
            if anime.title.lower() == title.lower():
                return anime
        return None