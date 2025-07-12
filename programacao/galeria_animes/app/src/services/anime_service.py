import csv
from app.src.models.anime import Anime

class AnimeService:
    def __init__(self, csv_filepath):
        self.csv_filepath = csv_filepath
        self.animes = []
        self._load_animes_from_csv()

    def _load_animes_from_csv(self):
        self.animes = []
        try:
            with open(self.csv_filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # TODO: Converter e mapear cada coluna do CSV para o construtor da classe Anime.
                        # ATENÇÃO: Os NOMES das chaves (e.g., 'anime_id', 'title_english') DEVEM
                        # ser EXATAMENTE iguais aos cabeçalhos do seu CSV.
                        # Lembre-se de tratar tipos (int, float) e valores ausentes (usando .get()).

                        anime = Anime(
                            anime_id=int(row.get('anime_id')),
                            title=row.get('title', ''),
                            title_english=row.get('title_english', ''),
                            title_japanese=row.get('title_japanese', ''),
                            image_url=row.get('image_url', ''), # A imagem que você queria!
                            type=row.get('type', ''),
                            episodes=int(row.get('episodes', 0)) if row.get('episodes', '').isdigit() else 0,
                            status=row.get('status', ''),
                            airing=bool(row.get('airing', False)), # Convertendo para booleano
                            aired_string=row.get('aired_string', ''),
                            duration=row.get('duration', ''),
                            rating=row.get('rating', ''),
                            score=float(row.get('score', 0.0)) if row.get('score') else 0.0,
                            scored_by=int(row.get('scored_by', 0)) if row.get('scored_by', '').isdigit() else 0,
                            rank=int(row.get('rank', 0)) if row.get('rank', '').isdigit() else 0,
                            popularity=int(row.get('popularity', 0)) if row.get('popularity', '').isdigit() else 0,
                            members=int(row.get('members', 0)) if row.get('members', '').isdigit() else 0,
                            favorites=int(row.get('favorites', 0)) if row.get('favorites', '').isdigit() else 0,
                            synopsis=row.get('synopsis', ''),
                            background=row.get('background', ''),
                            premiered=row.get('premiered', ''),
                            broadcast=row.get('broadcast', ''),
                            producer=row.get('producer', ''),
                            licensor=row.get('licensor', ''),
                            studio=row.get('studio', ''),
                            genre_string=row.get('genre_string', '')
                        )
                        self.animes.append(anime)
                    except ValueError as ve:
                        print(f"Aviso: Pulando linha devido a erro de conversão de tipo: {ve} na linha: {row}")
                    except Exception as e:
                        print(f"Aviso: Pulando linha devido a erro inesperado: {e} na linha: {row}")
                        continue

        except FileNotFoundError:
            print(f"Erro: O arquivo CSV '{self.csv_filepath}' não foi encontrado.")
            self.animes = []
        except Exception as e:
            print(f"Erro inesperado ao carregar o CSV: {e}")
            self.animes = []

    def get_all_animes(self):
        return self.animes

    def show_anime_detail(self, anime_id): # Renomeado de get_anime_by_mal_id
        # TODO: Implementar a busca por anime_id (o ID do dataset).
        # Retorne o objeto Anime se encontrado, None caso contrário.
        for anime in self.animes:
            if anime.anime_id == anime_id:
                return anime
        return None

    def search_animes(self, query, page=1, per_page=10):
        # TODO: Implementar a busca por query.
        # Sugestão: Buscar em 'title_english', 'title_japanese', 'genre_string'.
        # Depois, aplicar a paginação aos resultados filtrados.
        # Retorne: animes_on_page, total_pages, total_filtered_animes
        pass