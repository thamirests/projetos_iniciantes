# Projeto Chute Certo

Esse projeto tem por objetivo expandir o conhecimento e mostrar caminhos para pensar e se desenvolver como programador, por meio de problemas lúdicos que simulam recursos usados em sistemas reais.

---

## Escopo

Vamos criar um site de análises de partidas de futebol.
O campeonato, jogos e times são reais e os resultados também.
Por meio de entregas incrementais, vamos consumir, exibir, construir elementos e por fim realizar análises de partidas passadas, tendências e resultados prováveis.
Todas as análises são de cunho especulativo e têm como objetivo o aprendizado e aplicação de conceitos utilizados em desenvolvimento de software.
Para este projeto, focaremos inicialmente no **Campeonato Brasileiro de 2025**.

---

## API e Responsabilidades

Vamos trabalhar com a **[API Futebol](https://www.api-futebol.com.br/documentacao)**. Ela está em português, o que facilita o entendimento da documentação, além de ter excelentes opções para uma API gratuita.

Nossa organização de dados visa garantir a facilidade de entendimento e consumo da API. Funciona assim:

* Um **Campeonato** é composto de **Rodadas**.
* Uma **Rodada** é composta de **Partidas**.
* Uma **Partida** envolve **Times** (mandante e visitante).
* Um **Time** é composto por **Atletas**.

---

## Entidades Principais e seus Atributos

Abaixo, algumas informações gerais sobre as entidades para um entendimento de contexto. Perceba que a API fornece **IDs** e mais detalhes que nos ajudarão a fazer o relacionamento entre as entidades e facilitar o mapeamento do comportamento do usuário.

### Entidade Campeonato
* `id` (ID do Campeonato, crucial para relacionamentos)
* `Nome`
* `Fase` (Fase atual do campeonato)
* `Rodada` (Rodada atual do campeonato)
* `Status`

### Entidade Partida
* `id` (ID da Partida)
* `Campeonato_id` (ID do Campeonato a que pertence)
* `Rodada_id` (ID da Rodada a que pertence)
* `Placar_mandante`
* `Placar_visitante`
* `Data/Hora de Realização`
* `Estádio`
* `Time Mandante` (Objeto Time aninhado)
* `Time Visitante` (Objeto Time aninhado)
* `Status` (Ex: "encerrada", "agendada")
* *(Opcional/Futuro: Substituições, Cartões - A API oferece, mas vamos focar no essencial primeiro.)*

### Entidade Time
* `id` (ID do Time)
* `Nome` (Nome oficial)
* `Nome Popular`
* `Sigla`
* `URL do Escudo`

### Entidade Atleta
* `id` (ID do Atleta)
* `Nome Popular`
* `Posição`
* `Número da Camisa`
* `Status` (Ex: "titular", "lesionado")

---

## Linguagem e Frameworks

O projeto será construído utilizando as seguintes tecnologias:

* **Java**: A linguagem de programação principal.
* **Spring Boot**: Um framework que simplifica o desenvolvimento de aplicações Java, especialmente para a criação de APIs e aplicações web.
* **Maven**: Uma ferramenta de automação de construção para gerenciar dependências e o ciclo de vida do projeto.
* **Thymeleaf**: Um motor de templates para criar páginas HTML dinâmicas diretamente no lado do servidor, facilitando a exibição dos dados da API.

---

## Organização do Projeto (Padrão MVC)

Adotaremos o padrão **MVC (Model-View-Controller)** para organizar o código, o que facilita a manutenção e a compreensão:

* **`Controller`**: Responsável por receber as requisições do usuário, interagir com a camada de `Service` e decidir qual `View` (página HTML) será exibida.
* **`Service`**: Contém a lógica de negócio do aplicativo, orquestrando as operações e fazendo a ponte com a camada de integração de dados (neste caso, a API).
* **`Model`**: Representa os dados da nossa aplicação (as entidades como Campeonato, Partida, Time, Atleta). São objetos simples que armazenam as informações.
* **`ApiFutebolClient`**: Uma classe dedicada dentro da camada de `Service` para realizar as chamadas HTTP para a API externa, buscando os dados brutos.
* **`View`**: Corresponde às páginas web (arquivos HTML com Thymeleaf) que o usuário interage e onde os dados são exibidos de forma visual.

---

## Versionamento

Para gerenciar o código-fonte e colaborar no projeto, utilizaremos:

* **Git**: Um sistema de controle de versão distribuído que nos permite registrar o histórico de todas as alterações no código.
* **GitHub**: Uma plataforma de hospedagem de repositórios Git, onde nosso projeto estará armazenado.

Aprenderemos a usar o Git para salvar nosso progresso em "commits" e o GitHub para compartilhar as entregas e gerenciar as diferentes versões do projeto através de "branches" e "pull requests".

---

## Entregas (Roadmap Inicial)

O projeto será desenvolvido em etapas incrementais, cada uma com um objetivo claro:

1.  **Conectando e Consumindo a API (Console)**:
    * Configurar o projeto Spring Boot básico.
    * Criar o `ApiFutebolClient` e os primeiros `Model`s (`Campeonato`, `Rodada`).
    * Consumir um endpoint da API (ex: listar campeonatos ou rodadas).
    * Exibir as informações básicas no **console** para verificar a conexão.

2.  **Estruturando Entidades e Navegando no Console**:
    * Refinar os `Model`s (`Partida`, `Time`, `Atleta`) com mais atributos.
    * Implementar o `CampeonatoService` para orquestrar as chamadas da API e construir os objetos de domínio.
    * Criar um **menu simples no console** que permita ao usuário listar campeonatos, rodadas e jogos de uma rodada específica.

3.  **A Primeira Página Web (View Simples)**:
    * Configurar o Thymeleaf.
    * Criar o `CampeonatoController`.
    * Desenvolver a primeira página HTML (`index.html`) que utiliza o Thymeleaf para exibir dados simples (ex: uma lista de campeonatos) provenientes da API.

4.  **Detalhes e Navegação Web**:
    * Permitir a navegação entre as páginas (ex: de campeonatos para rodadas, de rodadas para jogos).
    * Criar páginas HTML para exibir detalhes das rodadas e dos jogos, com links funcionais.

---