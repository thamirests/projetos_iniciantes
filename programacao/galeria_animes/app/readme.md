# Entendendo a Estrutura do Projeto "Galeria de Animes"

Olá! Este `README.md` foi criado para te guiar pela estrutura do nosso projeto de Galeria de Animes, especialmente a pasta `app/` onde a magia acontece. Nosso objetivo é que você entenda como as peças se encaixam e se sinta à vontade para modificá-las.

---

## Estrutura da Pasta `app/`

Dentro da pasta principal do seu projeto, `galeria_de_animes/`, você encontrará a pasta `app/`. É aqui que reside a maior parte do código da nossa aplicação Flask, organizada de uma forma que chamamos de **Modular** ou, em aplicações maiores, **MVC (Model-View-Controller)**.

Vamos ver como ela está organizada:

app/
├── main.py                     # O "Controlador" principal da sua aplicação Flask <br>
├── src/                        # Código fonte da sua lógica de negócio<br>
│   ├── models/                 # Onde definimos como nossos "objetos" são<br>
│   │   ├── anime.py            # Nosso objeto Anime<br>
│   │   └── manga.py            # [BÔNUS] Nosso objeto Manga<br>
│   └── services/               # Onde a lógica de busca e manipulação de dados acontece<br>
│       ├── anime_service.py    # Serviço para Animes (lê do CSV, etc.)<br>
│       └── manga_service.py    # [BÔNUS] Serviço para Mangas<br>
└── web/                        # Parte da aplicação voltada para a interface web<br>
├── templates/              # Onde ficam nossos arquivos HTML (as "Views")<br>
│   ├── base.html           # Template base (reutilizável)<br>
│   ├── index.html          # Página inicial com botões<br>
│   ├── anime_search.html   # Página de listagem/busca de Animes<br>
│   ├── anime_detail.html   # Página de detalhes de um Anime<br>
│   ├── manga_search.html   # [BÔNUS] Página de listagem/busca de Mangas<br>
│   └── manga_detail.html   # [BÔNUS] Página de detalhes de um Manga<br>
└── static/                 # Onde ficam arquivos estáticos (CSS, imagens, JS)<br>
├── css/<br>
│   └── style.css       # Nossos estilos<br>
└── img/                # Para imagens (ex: placeholders)<br>

---

## Entendendo os Componentes Principais

Vamos traduzir essa estrutura para o contexto do nosso projeto e, se você estiver familiarizado, para uma arquitetura tradicional:

* **`main.py` (Nosso "Controlador" - *Controller*):**
    * Este é o coração da sua aplicação Flask. Ele **recebe as requisições** dos usuários (quando eles acessam uma URL), **conversa com os serviços** (para obter os dados necessários) e, finalmente, **renderiza os templates HTML** (as "Views") para mostrar a resposta ao usuário. É o maestro que coordena tudo.

* **`models/` (Nossos "Objetos" - *Models*):**
    * Aqui definimos a **estrutura** dos dados com que trabalhamos. No `anime.py`, por exemplo, dizemos "um Anime tem um título, uma sinopse, um ID, uma URL de imagem, etc.". É a **representação dos nossos dados** no código.

* **`services/` (A Lógica de Dados - *Service Layer*):**
    * Os arquivos dentro de `services/` são responsáveis por toda a **lógica de manipulação dos dados**. O `anime_service.py` sabe como **ler as informações do seu arquivo CSV**, como **criar objetos `Anime`** a partir dessas informações, como **paginar** a lista de animes e como **buscar** animes específicos. Eles servem os dados para o `main.py`.

* **`web/templates/` (Nossa Interface - *Views*):**
    * São os arquivos HTML (`.html`) que o Flask usa para **montar a página que o usuário verá**. Eles recebem os dados do `main.py` (que por sua vez pegou do `services/`) e os exibem de forma bonita.

---

## Seu Desafio!

As estruturas básicas estão prontas para que você possa focar no mais importante: **entender a lógica e conectar as peças!**

* **`anime.py`:** Seu primeiro passo é **ajustar as características** (atributos e propriedades) da classe `Anime` para que ela corresponda exatamente às **colunas do novo dataset** que você está usando (`AnimeList.csv`), incluindo a `image_url` e o `anime_id`.
* **`anime_service.py`:** Aqui, seu trabalho é **ajustar a função de carregamento** (`_load_animes_from_csv`) para ler as informações do `AnimeList.csv` e preencher corretamente os objetos `Anime`. Além disso, **implemente as funções de paginação e busca** para Animes, usando o `anime_id` do dataset.
* **`main.py`:** Você precisará **ajustar as chamadas** para o `anime_service.py` (usando os novos nomes de atributos e o `anime_id`) e **garantir que os dados corretos sejam passados** para os templates (`anime_search.html` e `anime_detail.html`).
* **Templates (`anime_search.html` e `anime_detail.html`):** Você vai precisar **adaptar estes templates** para exibir as novas colunas do seu dataset (ex: `title_english`, `episodes`, `score`, `synopsis` e, claro, a **`image_url`**!).

Não se preocupe com as rotas principais (`/`, `/animes`, `/anime/<id>`), nem com a estrutura base dos templates e o `style.css` para a tabela e paginação. Isso já está preparado!

---

### [BÔNUS] O Projeto `Manga` (Para os mais Curiosos!)

Como um desafio extra, você pode replicar toda essa estrutura para um novo tipo de objeto: o **`Manga`**! Isso envolveria:

* Criar `manga.py` em `models/`.
* Criar `manga_service.py` em `services/`.
* Adicionar novas rotas no `main.py` (ex: `/mangas`, `/manga/<id>`).
* Criar novos templates (`manga_search.html`, `manga_detail.html`).

---

Espero que você se divirta muito aprendendo e construindo este projeto! Se tiver dúvidas, estamos aqui para ajudar.

---
