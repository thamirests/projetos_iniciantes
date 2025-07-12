# app/src/services/manga_service.py
import csv
from app.src.models.manga import Manga # Importe a classe Manga

class MangaService:
    def __init__(self, csv_filepath):
        self.csv_filepath = csv_filepath
        self.mangas = []
        self._load_mangas_from_csv()

    def _load_mangas_from_csv(self):
        self.mangas = []
        manga_id_counter = 0
        try:
            with open(self.csv_filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    manga_id_counter += 1
                    # TODO: Mapear as colunas do CSV para os atributos do objeto Manga.
                    # Lembre-se de tratar tipos (int, float) e valores ausentes.
                    # Exemplo: title = row.get('Title', 'Título Desconhecido')
                    # Crie uma instância de Manga:
                    # manga = Manga(manga_id=manga_id_counter, ...)
                    # self.mangas.append(manga)
                    pass # Remova esta linha ao implementar
        except FileNotFoundError:
            print(f"Erro: O arquivo CSV '{self.csv_filepath}' não foi encontrado.")
            self.mangas = []
        except Exception as e:
            print(f"Erro inesperado ao carregar o CSV de mangás: {e}")
            self.mangas = []

    # TODO: Implementar get_all_mangas(), get_mangas_paged(), get_manga_by_id(), search_mangas()
    # A lógica será similar à do AnimeService.
    # Lembre-se de adaptar os parâmetros e a lista 'self.mangas'.