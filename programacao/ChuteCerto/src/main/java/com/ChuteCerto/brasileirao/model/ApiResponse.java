package com.ChuteCerto.brasileirao.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.util.List;

// Esta classe é um exemplo. A estrutura exata dependerá da API para cada endpoint.
// Para o endpoint de campeonatos, por exemplo, a resposta pode ser uma lista direta de Campeonatos.
// Para rodadas, pode ser uma lista de Rodadas.
// Você pode precisar de classes de resposta mais específicas para cada endpoint.

@Data
@NoArgsConstructor
@AllArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
public class ApiResponse<T> { // T pode ser Campeonato, Rodada, etc.
    // Esta é uma suposição. Verifique a documentação da API ou o JSON real.
    // Se a API retornar uma lista diretamente, você não precisará desta classe wrapper.
    // Ex: {"campeonatos": [...]} ou {"rodadas": [...]}
    @JsonProperty("campeonatos")
    private List<Campeonato> campeonatos;

    @JsonProperty("rodadas")
    private List<Rodada> rodadas;

    @JsonProperty("partidas") // Pode ser para um endpoint que retorna apenas partidas
    private List<Partida> partidas;

    // Se a API tiver uma estrutura mais genérica, como:
    // @JsonProperty("data")
    // private List<T> data;
    // seria usado com `ApiResponse<Campeonato>` por exemplo.
}
