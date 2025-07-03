from flask import Flask, render_template, request
from app.src.services.anime_service import AnimeService

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

# Instancia o serviço de animes, ajustando o caminho do CSV
anime_service = AnimeService('data/anime_data.csv')

@app.route('/')
def index():
    all_animes = anime_service.get_all_animes()
    return render_template('index.html', animes=all_animes)

@app.route('/search', methods=['GET'])
def search():
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


if __name__ == '__main__':
    app.run(debug=True) # debug=True recarrega o servidor automaticamente em cada mudança