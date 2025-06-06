package com.ChuteCerto.brasileirao.service;

import com.ChuteCerto.brasileirao.model.Campeonato;
import com.ChuteCerto.brasileirao.model.Rodada;
import org.springframework.stereotype.Service;

import java.util.List;

@Service // Indica que esta classe é um serviço (lógica de negócio)
public class CampeonatoService {

    private final ApiFutebolClient apiFutebolClient;

    // Injeção de dependência do ApiFutebolClient
    public CampeonatoService(ApiFutebolClient apiFutebolClient) {
        this.apiFutebolClient = apiFutebolClient;
    }

    /**
     * Busca todos os campeonatos disponíveis na API.
     * @return Uma lista de objetos Campeonato.
     */
    public List<Campeonato> buscarTodosOsCampeonatos() {
        // O serviço chama o cliente da API e pode adicionar lógica de negócio aqui.
        // Por exemplo, filtrar campeonatos ativos, ordenar, etc.
        return apiFutebolClient.getCampeonatos();
    }

    /**
     * Busca as rodadas de um campeonato específico na API, incluindo os jogos.
     * @param campeonatoId O ID do campeonato.
     * @return Uma lista de objetos Rodada, com os jogos aninhados.
     */
    public List<Rodada> buscarRodadasDoCampeonato(Long campeonatoId) {
        // Aqui você chamaria o cliente da API para buscar as rodadas
        // e se necessário, faria alguma transformação ou agregação de dados.
        return apiFutebolClient.getRodadasPorCampeonato(campeonatoId);
    }

    /**
     * Busca os detalhes de uma rodada específica, incluindo seus jogos.
     * Útil se você quiser carregar apenas uma rodada específica, ou se a API
     * tiver um endpoint para isso. A API que você informou já retorna os jogos
     * dentro da lista de rodadas do campeonato, então este método pode ser
     * um refinamento ou simplificação dependendo de como você quer exibir.
     * @param campeonatoId O ID do campeonato.
     * @param rodadaId O ID da rodada.
     * @return O objeto Rodada com seus jogos.
     */
    public Rodada buscarRodadaPorId(Long campeonatoId, Long rodadaId) {
        // Exemplo: Buscar todas as rodadas e encontrar a específica
        List<Rodada> rodadas = apiFutebolClient.getRodadasPorCampeonato(campeonatoId);
        return rodadas.stream()
                .filter(r -> r.getId().equals(rodadaId))
                .findFirst()
                .orElse(null); // Ou lançar uma exceção
    }

    // Você pode adicionar mais métodos de negócio aqui, como:
    // public List<Partida> buscarJogosDeUmTime(Long timeId) {...}
    // public Time buscarDetalhesDoTime(Long timeId) {...}
}
