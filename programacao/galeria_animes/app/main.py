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
    return render_template('anime_index.html', animes=anime)

@app.route('/search', methods=['GET'])
def search_animes():
    query = request.args.get('query', '').strip()
    if query:
        # Aqui você pode escolher se quer buscar por título, gênero, etc.
        # Por exemplo, uma busca simples por título ou gênero
        results = [
            anime for anime in anime_service.get_all_animes()
            if query.lower() in anime.title.lower() or query.lower() in anime.genre.lower()
        ]
    else:
        results = [] # Ou todos os animes, dependendo da sua preferência

    return render_template('index.html', animes=results, search_query=query)


@app.route('/anime/<mal_id>')
def show_anime_detail(mal_id):
    # Busca o anime pelo MAL_ID usando o serviço
    anime = anime_service.get_anime_by_mal_id(mal_id)

    if anime:
        # Se o anime for encontrado, renderiza o template anime_detail.html
        return render_template('anime_detail.html', anime=anime)
    else:
        # Se o anime não for encontrado, você pode redirecionar para uma página de erro
        # ou para a página principal com uma mensagem.
        return "Anime não encontrado!", 404 # Retorna um erro 404 - Not Found

if __name__ == '__main__':
    app.run(debug=True) # debug=True recarrega o servidor automaticamente em cada mudança