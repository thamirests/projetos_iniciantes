import os
from flask import Flask, render_template, request
from src.services.anime_service import AnimeService

PYTHONPATH = "programacao/GaleriaAnimes/"

app = Flask(__name__, template_folder='src/web/templates', static_folder='src/web/static')

# Instancia o serviço de animes, ajustando o caminho do CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANIME_CSV_PATH = os.path.join(BASE_DIR, '..', 'data', 'test_anime_data.csv')
anime_service = AnimeService(ANIME_CSV_PATH)

@app.route('/')
def index():
    anime = anime_service.get_all_animes()
    return render_template('index.html', animes=anime)

@app.route('/search', methods=['GET'])
def search_animes():
    ### COMECE AQUI ###
    '''
    Implementa a lógica de busca de animes.
    A busca deve ser feita pelo nome do anime, que é passado como parâmetro na URL.
    Exemplo: /search?name=Naruto
    '''


@app.route('/anime/<mal_id>')
def show_anime_detail(mal_id):
    '''
    Exibe os detalhes de um anime específico.
    O mal_id é passado como parte da URL.
    Exemplo: /anime/1
    '''

if __name__ == '__main__':
    app.run(debug=True) # debug=True recarrega o servidor automaticamente em cada mudança