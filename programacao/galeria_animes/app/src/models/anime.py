class Anime:
    def __init__(self, anime_id, title, title_english, title_japanese, image_url,
                 type, episodes, status, airing, aired_string, duration,
                 rating, score, scored_by, rank, popularity, members,
                 favorites, synopsis, background, premiered, broadcast,
                 producer, licensor, studio, genre_string): # Nota: 'genre_string' é a string de gêneros
        # TODO: Inicializar os atributos da classe aqui, mapeando diretamente do CSV.
        # Exemplo:
        self._anime_id = anime_id
        self._title = title # Título original (pode ser o principal se english_title for nulo)
        self._title_english = title_english # Título em inglês
        self._title_japanese = title_japanese
        self._image_url = image_url
        self._type = type
        self._episodes = episodes
        self._status = status
        self._airing = airing
        self._aired_string = aired_string
        self._duration = duration
        self._rating = rating
        self._score = score
        self._scored_by = scored_by
        self._rank = rank
        self._popularity = popularity
        self._members = members
        self._favorites = favorites
        self._synopsis = synopsis
        self._background = background
        self._premiered = premiered
        self._broadcast = broadcast
        self._producer = producer # Pode ser uma lista ou string, dependendo do CSV
        self._licensor = licensor # Pode ser uma lista ou string
        self._studio = studio     # Pode ser uma lista ou string
        self._genre_string = genre_string # String de gêneros separada por vírgulas, ex: "Action, Comedy"


    # TODO: Adicionar propriedades (getters) para cada atributo.
    # Exemplo:
    # @property
    # def anime_id(self):
    #     return self._anime_id

    # @property
    # def title_english(self):
    #     return self._title_english

    # TODO: Opcional: Adicionar um método para obter o título mais apropriado para exibição.
    # Exemplo:
    # @property
    # def display_title(self):
    #     return self._title_english or self._title or self._title_japanese

    # TODO: Opcional: Adicionar um método __str__ para depuração.