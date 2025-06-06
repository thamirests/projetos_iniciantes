package com.ChuteCerto.brasileirao.service;

import com.ChuteCerto.brasileirao.model.Campeonato;
import com.ChuteCerto.brasileirao.model.Rodada;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@Component // Indica que esta classe é um componente Spring (útil para injeção de dependência)
public class ApiFutebolClient {

    // URL base da API
    @Value("${api.futebol.base-url}") // Lê do application.properties
    private String baseUrl;

    // Token de acesso da API
    @Value("${api.futebol.api-key}") // Lê do application.properties
    private String apiKey;

    private final RestTemplate restTemplate;

    public ApiFutebolClient(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    // Método auxiliar para adicionar o cabeçalho de autenticação
    private HttpEntity<String> createHeaders() {
        HttpHeaders headers = new HttpHeaders();
        headers.set("Authorization", "Bearer " + apiKey); // Assumindo que a API usa Bearer Token
        return new HttpEntity<>(headers);
    }

    /**
     * Retorna a lista de campeonatos disponíveis na API.
     * Endpoint: /v1/campeonatos
     * @return Lista de objetos Campeonato.
     */
    public List<Campeonato> getCampeonatos() {
        String url = baseUrl + "/v1/campeonatos";
        // ParameterizedTypeReference é usado para deserializar para Listas ou tipos genéricos
        return restTemplate.exchange(url, HttpMethod.GET, createHeaders(),
                new ParameterizedTypeReference<List<Campeonato>>() {}).getBody();
    }

    /**
     * Retorna a lista de rodadas para um campeonato específico.
     * Este endpoint já deve incluir os jogos dentro de cada rodada.
     * Endpoint: /v1/campeonatos/{campeonato_id}/rodadas
     * @param campeonatoId O ID do campeonato.
     * @return Lista de objetos Rodada.
     */
    public List<Rodada> getRodadasPorCampeonato(Long campeonatoId) {
        String url = baseUrl + "/v1/campeonatos/" + campeonatoId + "/rodadas";
        return restTemplate.exchange(url, HttpMethod.GET, createHeaders(),
                new ParameterizedTypeReference<List<Rodada>>() {}).getBody();
    }

    // Você pode adicionar mais métodos para outros endpoints da API, como:
    // public List<Atleta> getElencoDoTime(Long timeId) { ... }
    // public Time getDetalhesDoTime(Long timeId) { ... }
}
