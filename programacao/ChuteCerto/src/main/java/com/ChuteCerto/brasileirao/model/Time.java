package com.ChuteCerto.brasileirao.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
public class Time {
    @JsonProperty("time_id")
    private Long id;
    @JsonProperty("nome_popular")
    private String nomePopular;
    @JsonProperty("sigla")
    private String sigla;
    @JsonProperty("escudo")
    private String urlEscudo; // URL do escudo do time
    @JsonProperty("nome")
    private String nomeCompleto; // Nome oficial do time

    // A API que você indicou retorna atletas em um endpoint separado para o elenco do time,
    // mas se fosse aninhado em alguma resposta de partida, seria assim:
    // @JsonProperty("atletas")
    // private List<Atleta> atletas;
}