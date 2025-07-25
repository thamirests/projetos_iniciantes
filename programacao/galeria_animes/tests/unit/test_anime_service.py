import unittest
import os
from app.src.services.anime_service import AnimeService
from app.src.models.anime import Anime

# Criar um CSV de teste temporário para os testes
TEST_CSV_PATH = 'data/test_anime_data.csv'
PYTHONPATH = "programacao/GaleriaAnimes/"

class TestAnimeService(unittest.TestCase):

    @classmethod
    # def setUpClass(cls):
    #     # Cria um arquivo CSV de teste antes de todos os testes
    #     # os.makedirs(os.path.dirname(TEST_CSV_PATH), exist_ok=True)
    #     # with open(TEST_CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    #     #     f.write('title,genre,episodes,synopsis\n')
    #     #     f.write('One Piece,Aventura,1100,A história de Monkey D. Luffy...\n')
    #     #     f.write('Naruto,Aventura,720,A história de Naruto Uzumaki...\n')
    #     #     f.write('Attack on Titan,Ação,88,A humanidade é forçada a viver...\n')

    # @classmethod
    # def tearDownClass(cls):
    #     # Remove o arquivo CSV de teste depois de todos os testes
    #     if os.path.exists(TEST_CSV_PATH):
    #         os.remove(TEST_CSV_PATH)
    #     # Remover o diretório 'data' se estiver vazio
    #     data_dir = os.path.dirname(TEST_CSV_PATH)
    #     if not os.listdir(data_dir):
    #         os.rmdir(data_dir)


    def setUp(self):
        # Cada teste terá sua própria instância de AnimeService
        self.anime_service = AnimeService('data/AnimeList.csv')

    # def test_load_animes_from_csv(self):
    #     animes = self.anime_service.get_all_animes()
    #     self.assertEqual(len(animes), 3)
    #     self.assertIsInstance(animes[0], Anime)
    #     self.assertEqual(animes[0].title, 'One Piece')

    # def test_get_all_animes(self):
    #     animes = self.anime_service.get_all_animes()
    #     self.assertEqual(len(animes), 3)

    # def test_search_animes_by_genre(self):
    #     adventure_animes = self.anime_service.search_animes_by_genre('Aventura')
    #     self.assertEqual(len(adventure_animes), 2)
    #     self.assertEqual(adventure_animes[0].title, 'One Piece')

    # def test_get_anime_by_title(self):
    #     anime = self.anime_service.get_anime_by_title('Naruto')
    #     self.assertIsNotNone(anime)
    #     self.assertEqual(anime.genre, 'Aventura')

    #     non_existent_anime = self.anime_service.get_anime_by_title('Dragon Ball')
    #     self.assertIsNone(non_existent_anime)

    # def test_csv_not_found(self):
    #     service_with_invalid_path = AnimeService('non_existent.csv')
    #     self.assertEqual(len(service_with_invalid_path.get_all_animes()), 0)
    
    def test_get_anime_by_title(self):
        anime = self.anime_service.get_anime_by_mal_id(11013)
        self.assertIsNotNone(anime)
        self.assertIsInstance(str)
        # self.assertEqual(anime.genre, 'Aventura')
    def test_search_animes(self):
        # Teste de busca por título
        animes = self.anime_service.search_animes(query='One Piece')
        self.assertEqual(len(animes), 1)
        self.assertEqual(animes[0].title, 'One Piece')

        # Teste de busca por gênero
        animes = self.anime_service.search_animes(query='Aventura')
        self.assertGreater(len(animes), 0)

        # Teste de busca com query vazia
        animes = self.anime_service.search_animes(query='')
        self.assertGreater(len(animes), 0)

if __name__ == '__main__':
    unittest.main()