# Projeto Minhas Lista de Animes

E aí, galera! Bora mergulhar no mundo dos dados? Este projeto é seu trampolim pra ter aquele contato massa com a transformação e análise de dados, algo super requisitado no mercado de TI.

Aqui, a gente vai pegar dados de uma fonte, dar aquela organizada neles (normalizar) e depois jogar tudo numa tabela que você mesmo vai criar. A partir daí, vamos fazer umas análises simples que, na vida real, são a base pra dashboards e ajudam as empresas a tomar decisões importantes.

---

## Contexto

No dia a dia do mundo dos dados, a gente constrói o que chamamos de **pipelines de dados**. Pensa nisso como um "encanamento" que leva os dados de um lugar para outro, seja pra ajudar nas decisões de negócio ou pra refinar esses dados e alimentar modelos de inteligência artificial. Esses modelos, por sua vez, podem gerar insights incríveis, desde recomendações personalizadas pra clientes até a aprovação de recursos financeiros, e muito mais!

Aqui, nosso foco vai ser mais direto: vamos consumir uma base em formato `.csv`, dar aquela organizada nos dados e, em seguida, colocá-los em uma tabela. Tudo isso usando **Pandas**, que é uma biblioteca super versátil e amigável pra quem tá começando em Python.

Como a ideia é você botar a mão na massa e entender que, na vida real, a gente usa ferramentas diferentes pra funções diferentes, vamos usar o Pandas tanto para o consumo e normalização quanto para as análises. Mas ó: se você já manja de **PySpark** ou quer se aventurar nele, sinta-se à vontade para usar essa ferramenta poderosa para a parte de consumo e transformação. A base do projeto é adaptável!

Vamos usar dados de anime/mangá pra deixar tudo mais divertido, mas sinta-se livre pra aplicar esse projeto em qualquer tipo de base de dados que você curtir!

Nosso desenvolvimento vai seguir esse fluxo principal:

```
Fonte de Dados → Consumo → Armazenamento → Análises → Insights
```

---

## Detalhes do Projeto

### Fonte de Dados

- **Formato:** Arquivos `.csv`

### Consumo e Armazenamento

- **Ferramenta:** Python + Pandas
- **Observação:** Se você já tem familiaridade ou quer explorar, pode usar PySpark aqui para consumir e normalizar os dados, e depois seguir com Pandas para as análises. A escolha é sua!
- **Armazenamento:** MongoDB (um banco de dados NoSQL bem fácil de usar para iniciantes).

### Análises e Insights

- **Análises:** Python + Pandas (pra manipular e explorar seus dados).
- **Insights:** Python + Plotly (pra criar visualizações iradas e transformar seus dados em histórias!).

---

## Importante!

Pra esse projeto, você não precisa ser um expert em nada! O fundamental é já ter tido algum contato com Python e estar com aquela vontade de pesquisar e estudar mais sobre os recursos e informações que vamos usar.

**Dica de ouro:** Pratique a construção do projeto junto com um assistente de IA! Ele vai te ajudar a criar prompts melhores e agilizar as respostas para suas dúvidas. É um jeito muito legal de aprender!

---

## Organização do Repositório

Nesse repositório Git, você vai encontrar duas pastas com as fases do projeto. As entregas serão feitas através de branches específicas com o número da entrega. Desse jeito, você pratica entregas incrementais (que é o que o mercado faz!) e vê o valor do seu projeto crescendo desde o primeiro dia, além de turbinar suas habilidades com Git.

---

## Entregas por Fase

### Fase 1: Consumo e Armazenamento

- **Recursos Utilizados:** Python, Pandas, MongoDB
- **Fonte de Dados:** Arquivos `.csv`
- **Linguagem:** Python
- **Frameworks/Bibliotecas:** Pandas, Pymongo (para conectar ao MongoDB)

**Entregas:**
- Código Python para ler o arquivo `.csv` usando Pandas.
- Código Python para normalizar os dados (ex: tratar valores nulos, padronizar formatos, converter tipos de dados).
- Código Python para carregar os dados normalizados em uma coleção do MongoDB.
- Documentação simples explicando os passos e as transformações realizadas.

---

### Fase 2: Análises e Insights

- **Recursos Utilizados:** Python, Pandas, Plotly
- **Fonte de Dados:** Dados armazenados no MongoDB
- **Linguagem:** Python
- **Frameworks/Bibliotecas:** Pandas, Plotly

**Entregas:**
- Código Python para consumir os dados do MongoDB usando Pandas.
- Códigos Python para realizar análises exploratórias simples (ex: contagem de itens, média de valores, distribuição de categorias).
- Geração de pelo menos 3 gráficos usando Plotly para visualizar os insights (ex: um gráfico de barras para contagem de gêneros, um de pizza para distribuição de tipos, um de linha para tendências).
- Breve relatório (em um arquivo Markdown ou Jupyter Notebook) descrevendo as análises e os insights obtidos.

---

Bons estudos e mãos à obra! 🚀