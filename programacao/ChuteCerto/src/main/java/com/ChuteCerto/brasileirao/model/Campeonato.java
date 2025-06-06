package com.ChuteCerto.brasileirao.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data; // Para getters, setters, toString, equals e hashCode
import lombok.NoArgsConstructor; // Para construtor sem argumentos
import lombok.AllArgsConstructor; // Para construtor com todos os argumentos

import java.time.LocalDate;
import java.util.List;

@Data // Gera automaticamente getters, setters, toString, equals e hashCode
@NoArgsConstructor // Gera construtor sem argumentos
@AllArgsConstructor // Gera construtor com todos os argumentos
@JsonIgnoreProperties(ignoreUnknown = true) // Ignora propriedades do JSON que não têm correspondência aqui
public class Campeonato {
    @JsonProperty("campeonato_id") // Mapeia o campo "campeonato_id" do JSON para "id"
    private Long id;
    @JsonProperty("nome")
    private String nome;
    @JsonProperty("slug")
    private String slug;
    @JsonProperty("nome_popular")
    private String nomePopular;
    @JsonProperty("sigla")
    private String sigla;
    @JsonProperty("tipo")
    private String tipo; // Ex: "nacional", "regional"
    @JsonProperty("fase_atual")
    private FaseAtual faseAtual;
    @JsonProperty("rodada_atual")
    private Rodada rodadaAtual; // A API pode retornar a rodada atual aninhada
    @JsonProperty("status")
    private String status; // Ex: "ativo"


    // Uma lista de rodadas pode ser obtida por outro endpoint,
    // mas se a API aninhar, pode ser adicionado aqui.
    // private List<Rodada> rodadas;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class FaseAtual {
        @JsonProperty("fase_id")
        private Long id;

        @JsonProperty("nome")
        private String nome;

        @JsonProperty("slug")
        private String slug;

        @JsonProperty("tipo")
        private String tipo;

        @JsonProperty("status")
        private String status;

    }
}
