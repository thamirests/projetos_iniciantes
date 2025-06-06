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
public class Atleta {
    @JsonProperty("atleta_id")
    private Long id;
    @JsonProperty("nome_popular")
    private String nomePopular;
    @JsonProperty("posicao")
    private String posicao; // Ex: "atacante", "zagueiro"
    @JsonProperty("status")
    private String status; // Ex: "titular", "reservista", "lesionado"
    @JsonProperty("numero_camisa")
    private Integer numeroCamisa;
    // Adicione outros campos como "foto", "nacionalidade", etc.
}