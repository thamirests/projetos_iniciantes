class Anime:
    def __init__(self, title, genre, episodes, synopsis):
        self._title = title
        self._genre = genre
        self._episodes = episodes
        self._synopsis = synopsis

    @property
    def title(self):
        return self._title

    @property
    def genre(self):
        return self._genre

    @property
    def episodes(self):
        return self._episodes

    @property
    def synopsis(self):
        return self._synopsis

    def display_info(self):
        return f"Título: {self.title}\nGênero: {self.genre}\nEpisódios: {self.episodes}\nSinopse: {self.synopsis[:100]}..."

    def __str__(self):
        return f"Anime(Título: {self.title}, Gênero: {self.genre})"