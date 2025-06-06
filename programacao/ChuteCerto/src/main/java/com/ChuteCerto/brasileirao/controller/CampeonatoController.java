package com.ChuteCerto.brasileirao.controller;

import com.ChuteCerto.brasileirao.model.Campeonato;
import com.ChuteCerto.brasileirao.model.Rodada;
import com.ChuteCerto.brasileirao.service.CampeonatoService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Controller // Indica que esta classe é um controlador Spring MVC
@RequestMapping("/") // Mapeia todas as requisições para a raiz do contexto
public class CampeonatoController {

    private final CampeonatoService campeonatoService;

    // Injeção de dependência do CampeonatoService
    public CampeonatoController(CampeonatoService campeonatoService) {
        this.campeonatoService = campeonatoService;
    }

    // --- 1ª e 2ª Entrega (Versão Console/Testes) ---
    // Este método é mais para demonstração no console ou para testes de service
    // Não será usado diretamente pelo navegador na 3a entrega, mas o service que ele usa sim.
    public void exibirInfosNoConsole() {
        System.out.println("--- INICIANDO TESTE NO CONSOLE ---");
        try {
            List<Campeonato> campeonatos = campeonatoService.buscarTodosOsCampeonatos();
            if (campeonatos != null && !campeonatos.isEmpty()) {
                System.out.println("Campeonatos Encontrados:");
                for (Campeonato c : campeonatos) {
                    System.out.println("ID: " + c.getId() + ", Nome: " + c.getNome());

                    // Exemplo: buscar rodadas do primeiro campeonato
                    if (c.getId() != null) {
                        System.out.println("\n--- Rodadas do Campeonato " + c.getNome() + " ---");
                        List<Rodada> rodadas = campeonatoService.buscarRodadasDoCampeonato(c.getId());
                        if (rodadas != null && !rodadas.isEmpty()) {
                            for (Rodada r : rodadas) {
                                System.out.println("  Rodada ID: " + r.getId() + ", Nome: " + r.getNome() + ", Status: " + r.getStatus());
                                // Opcional: mostrar jogos da rodada
                                if (r.getPartidas() != null && !r.getPartidas().isEmpty()) {
                                    System.out.println("    Jogos da Rodada " + r.getNome() + ":");
                                    r.getPartidas().forEach(p -> {
                                        System.out.println("      " + p.getTimeMandante().getNome() + " " + p.getPlacarMandante() + " x " + p.getPlacarVisitante() + " " + p.getTimeVisitante().getNome());
                                    });
                                }
                            }
                        } else {
                            System.out.println("  Nenhuma rodada encontrada para o Campeonato " + c.getNome());
                        }
                    }
                }
            } else {
                System.out.println("Nenhum campeonato encontrado.");
            }
        } catch (Exception e) {
            System.err.println("Erro ao buscar informações: " + e.getMessage());
            e.printStackTrace();
        }
        System.out.println("--- FIM DO TESTE NO CONSOLE ---\n");
    }

    // --- 3ª Entrega: Primeira Página Web ---
    @GetMapping("/") // Mapeia a requisição GET para a URL "/" (raiz)
    public String home(Model model) {
        // Por enquanto, apenas retorna uma página inicial simples
        // Na 3a entrega, você vai preencher com dados da API
        return "index"; // Retorna o nome do template Thymeleaf (index.html)
    }

    // Exemplo de como seria um endpoint para listar campeonatos na web (futuro)
    @GetMapping("/campeonatos")
    public String listarCampeonatos(Model model) {
        // Implementar na 3a entrega:
        // List<Campeonato> campeonatos = campeonatoService.buscarTodosOsCampeonatos();
        // model.addAttribute("campeonatos", campeonatos);
        // return "campeonatos";
        return "index"; // Temporário
    }

    // Exemplo de como seria um endpoint para listar rodadas de um campeonato (futuro)
    @GetMapping("/campeonatos/{campeonatoId}/rodadas")
    public String listarRodadasDoCampeonato(@PathVariable String campeonatoId, Model model) {
        // Implementar na 4a entrega
        // List<Rodada> rodadas = campeonatoService.buscarRodadasDoCampeonato(campeonatoId);
        // model.addAttribute("rodadas", rodadas);
        // model.addAttribute("campeonatoId", campeonatoId);
        // return "rodadas";
        return "index"; // Temporário
    }
}