package com.ChuteCerto.brasileirao.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
public class Partida {
    @JsonProperty("partida_id")
    private Long id;
    @JsonProperty("campeonato_id")
    private Long campeonatoId;
    @JsonProperty("rodada_id")
    private Long rodadaId;
    @JsonProperty("status")
    private String status; // Ex: "encerrada", "agendada"
    @JsonProperty("data_realizacao")
    private String dataRealizacao; // Pode ser String ou LocalDate, dependendo da formatação
    @JsonProperty("hora_realizacao")
    private String horaRealizacao; // Pode ser String ou LocalTime
    @JsonProperty("estadio")
    private String estadio;
    @JsonProperty("placar_mandante")
    private Integer placarMandante;
    @JsonProperty("placar_visitante")
    private Integer placarVisitante;
    @JsonProperty("time_mandante") // Objeto Time aninhado
    private Time timeMandante;
    @JsonProperty("time_visitante") // Objeto Time aninhado
    private Time timeVisitante;
    // Adicione outros campos como "previsao_resultado", "url_confronto", etc.
}