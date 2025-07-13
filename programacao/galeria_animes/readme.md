# Projeto Galeria de Animes

Esse projeto tem por objetivo expandir o conhecimento e mostrar caminhos para pensar e se desenvolver como programador, por meio de problemas lúdicos que simulam recursos usados em sistemas reais. 

## 📚 Escopo

Este projeto é uma **Galeria de Animes** desenvolvida em Python, utilizando o framework web **Flask** para a interface. O objetivo principal é consumir dados de animes a partir de um arquivo `.csv` e exibi-los de forma organizada em uma página web local com um estilo de galeria.

Ele foi concebido como um projeto para iniciantes, focando em conceitos fundamentais como:
- **Programação Orientada a Objetos (POO):** Modelagem de entidades como `Anime` usando classes.
- **Organização de Código:** Estruturação modular do projeto (`models`, `services`, `web`).
- **Desenvolvimento Web Básico:** Criação de rotas, renderização de templates HTML com Jinja2 e uso de arquivos estáticos (CSS/JS).
- **Consumo de Dados:** Leitura e processamento de informações a partir de arquivos `.csv`.
- **Testes Unitários (Opcional/Plus):** Garantia da qualidade e correção da lógica de negócio.


## ✨ Funcionalidades

-   **Listagem de Animes:** Exibe todos os animes carregados do arquivo `.csv` em um formato de galeria.
-   **Detalhes do Anime:** (Opcional, pode ser adicionado depois) Exibir informações mais detalhadas de um anime ao clicar em seu card.
-   **Busca/Filtro de Animes:** (Opcional, pode ser adicionado depois) Funcionalidade para pesquisar animes por título, gênero, etc.
-   **Interface Web Amigável:** Página HTML com CSS básico para uma visualização agradável.


## 🚀 Tecnologias Utilizadas

-   **Python 3.x:** Linguagem de programação principal.
-   **Flask:** Micro-framework web para construção da aplicação.
-   **HTML5:** Estrutura das páginas web.
-   **CSS3:** Estilização da galeria.
-   **CSV:** Formato do arquivo de dados dos animes.
-   **`unittest` (ou `pytest`):** Para testes unitários (se implementados).

## 📊 Fonte dos Dados

Os dados de animes utilizados para o desenvolvimento desse projeto são provenientes do dataset "**anime-dataset**" disponível no [GitHub](https://github.com/meesvandongen/anime-dataset).<br>
Fique a vontade para procurar datasets mais completos para utilizar nesse projeto.


## ⚙️ Estrutura do Projeto

A estrutura do projeto segue uma organização modular para facilitar a manutenção e o entendimento:
<pre>
galeria_de_animes/
├── app/
│   ├── main.py                # Ponto de entrada da aplicação Flask
│   ├── src/
│   │   ├── models/            # Contém as classes de modelo (ex: anime.py)
│   │   │   └── anime.py       # Definição da classe Anime
│   │   └── services/          # Contém a lógica de negócio e manipulação de dados
│   │       └── anime_service.py # Serviço para carregar e gerenciar animes
│   └── web/
│       ├── templates/         # Arquivos HTML (Jinja2 templates)
│       │   └── index.html     # Template principal da galeria
│       └── static/            # Arquivos estáticos (CSS, JavaScript, imagens)
│           ├── css/
│           │   └── style.css  # Folha de estilo da aplicação
│           └── js/
│               └── script.js  # Scripts JavaScript (se houver)
├── data/
│   └── sample_anime.csv         # Arquivo CSV com os dados dos animes
└── tests/
├── unit/                  # Testes unitários para classes e serviços
│   └── test_anime_service.py
└── integration/           # Testes de integração (ex: para a aplicação web)
└── test_web_app.py
</pre>

Vamos traduzir essa estrutura para o contexto do nosso projeto e, se você estiver familiarizado, para uma arquitetura tradicional:

* **`main.py` (Nosso "Controlador" - *Controller*):**
    * Este é o coração da sua aplicação Flask. Ele **recebe as requisições** dos usuários (quando eles acessam uma URL), **conversa com os serviços** (para obter os dados necessários) e, finalmente, **renderiza os templates HTML** (as "Views") para mostrar a resposta ao usuário. É o maestro que coordena tudo.

* **`models/` (Nossos "Objetos" - *Models*):**
    * Aqui definimos a **estrutura** dos dados com que trabalhamos. No `anime.py`, por exemplo, dizemos "um Anime tem um título, uma sinopse, um ID, uma URL de imagem, etc.". É a **representação dos nossos dados** no código.

* **`services/` (A Lógica de Dados - *Service Layer*):**
    * Os arquivos dentro de `services/` são responsáveis por toda a **lógica de manipulação dos dados**. O `anime_service.py` sabe como **ler as informações do seu arquivo CSV**, como **criar objetos `Anime`** a partir dessas informações, como **paginar** a lista de animes e como **buscar** animes específicos. Eles servem os dados para o `main.py`.

* **`web/templates/` (Nossa Interface - *Views*):**
    * São os arquivos HTML (`.html`) que o Flask usa para **montar a página que o usuário verá**. Eles recebem os dados do `main.py` (que por sua vez pegou do `services/`) e os exibem de forma bonita.

## 🧑‍💻 Seu Desafio!

As estruturas básicas estão prontas para que você possa focar no mais importante: **entender a lógica e conectar as peças!**

* **`anime.py`:** Seu primeiro passo é **ajustar as características** (atributos e propriedades) da classe `Anime` para que ela corresponda exatamente às **colunas do novo dataset** que você está usando (`AnimeList.csv`), incluindo a `image_url` e o `anime_id`.
* **`anime_service.py`:** Aqui, seu trabalho é **ajustar a função de carregamento** (`_load_animes_from_csv`) para ler as informações do `AnimeList.csv` e preencher corretamente os objetos `Anime`. Além disso, **implemente as funções de paginação e busca** para Animes, usando o `anime_id` do dataset.
* **`main.py`:** Você precisará **ajustar as chamadas** para o `anime_service.py` (usando os novos nomes de atributos e o `anime_id`) e **garantir que os dados corretos sejam passados** para os templates (`anime_search.html` e `anime_detail.html`).
* **Templates (`anime_search.html` e `anime_detail.html`):** Você vai precisar **adaptar estes templates** para exibir as novas colunas do seu dataset (ex: `title_english`, `episodes`, `score`, `synopsis` e, claro, a **`image_url`**!).

Não se preocupe com as rotas principais (`/`, `/animes`, `/anime/<id>`), nem com a estrutura base dos templates e o `style.css` para a tabela e paginação. Isso já está preparado!


## 🏁 Como Executar o Projeto

Siga os passos abaixo para configurar e executar a Galeria de Animes em sua máquina local:

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em seu sistema.

### 1. Clonar o Repositório (ou Criar a Estrutura)

```bash
# Se você estiver usando Git:
git clone [URL_DO_SEU_REPOSITORIO]
cd galeria_de_animes

# Se você estiver criando do zero:
mkdir galeria_de_animes
cd galeria_de_animes
# Em seguida, crie as pastas e arquivos conforme a estrutura acima.
```
### 2. É uma boa prática usar ambientes virtuais para isolar as dependências do seu projeto
```
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```
### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias:
```
pip install Flask
# pip install pytest # Se você planeja usar pytest para testes
```

### 4.  Preparar os Dados
Existe uma amostra de dados de animes dentro da pasta `data/`<br>
Caso queira usar sua propria fonte de dados coloque o seu arquivo .csv de animes na pasta `data/`. Certifique-se de que ele esteja nomeado como sample_anime.csv ou ajuste o nome no código do main.py.

Exemplo de estrutura do sample_anime.csv (colunas):
id,title,titleJa,titleEn,image,mean,rank,num_list_users,num_scoring_users,num_episodes,start_date,end_date,media_type,status,rating,average_episode_duration,genres,studios

### 5. Executar a Aplicação

Navegue até o diretório galeria_de_animes/app e execute o main.py:

```
# certifique-se que esteja dentro da pasta app
python main.py
```
Após executar, o Flask irá iniciar um servidor de desenvolvimento. Você verá uma mensagem no terminal indicando o endereço local, geralmente http://127.0.0.1:5000/. Abra este endereço em seu navegador.

# 🧪 Como Rodar os Testes
Para executar os testes unitários (se implementados):
```
# Navegue até a pasta raiz do projeto
cd galeria_de_animes

# Execute os testes (se estiver usando unittest)
python -m unittest discover tests/unit

# Ou, se estiver usando pytest
# pytest tests/unit
```

## 💡[BÔNUS] O Projeto `Manga` (Para os mais Curiosos!)

Como um desafio extra, você pode replicar toda essa estrutura para um novo tipo de objeto: o **`Manga`**! Isso envolveria:

* Criar `manga.py` em `models/`.
* Criar `manga_service.py` em `services/`.
* Adicionar novas rotas no `main.py` (ex: `/mangas`, `/manga/<id>`).
* Criar novos templates (`manga_search.html`, `manga_detail.html`).

# 🤝 Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou quiser melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

# 📝 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

# 👨‍💻 Autor
[Thamires Trindade](https://github.com/thamirests/)
<br>Discord: thamyts

**Observações para você:**

* **Preenchimento:** As seções `✨ Funcionalidades`, `⚙️ Estrutura do Projeto` e `🏁 Como Executar o Projeto` (especialmente o exemplo de CSV) precisarão de pequenos ajustes conforme você avança na implementação real.
* **Imagens:** Se o seu CSV tiver URLs de imagem, você pode adicionar uma coluna `image_url` e ajustar o `Anime` model e o `index.html` para exibí-las.
* **Testes:** A seção de testes é "plus", mas é muito valiosa para um iniciante!

Este `README.md` oferece um guia completo para você e para qualquer pessoa que queira entender e executar seu projeto.