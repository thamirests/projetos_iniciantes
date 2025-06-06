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
public class Rodada {
    @JsonProperty("rodada_id")
    private Long id;
    @JsonProperty("nome")
    private String nome;
    @JsonProperty("slug")
    private String slug;
    @JsonProperty("status")
    private String status; // Ex: "encerrada", "agendada"
    @JsonProperty("numero")
    private Integer numero;
    @JsonProperty("jogos") // Mapeia a lista de jogos/partidas dentro da rodada
    private List<Partida> partidas;
}