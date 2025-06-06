package com.ChuteCerto.brasileirao;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import com.ChuteCerto.brasileirao.controller.CampeonatoController; // Importar
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext; // Importar

@SpringBootApplication
public class BrasileiraoApplication {

    public static void main(String[] args) {
        SpringApplication.run(BrasileiraoApplication.class, args);
        // Ao rodar, o Spring Boot irá iniciar um servidor web (Tomcat embarcado)
        // Você verá logs de inicialização e o servidor estará disponível em http://localhost:8080 (padrão)

        // Ao rodar, o Spring Boot irá iniciar um servidor web (Tomcat embarcado)
        ConfigurableApplicationContext context = SpringApplication.run(BrasileiraoApplication.class, args);

        // --- 1ª e 2ª Entrega: Teste no Console ---
        // Para executar o teste no console, você precisa obter uma instância do controlador.
        // Isso deve ser feito depois que o contexto Spring estiver totalmente carregado.
        // Este é um método um pouco "não-padrão" para chamar um bean Spring diretamente do main,
        // mas é útil para fins de demonstração no console para a primeira entrega.
        CampeonatoController controller = context.getBean(CampeonatoController.class);
        controller.exibirInfosNoConsole();
        // Opcional: fechar o contexto se você quiser que o app pare após o teste do console
        // context.close();
        // Se você quiser que o servidor web continue rodando, remova context.close()
        // e mantenha apenas SpringApplication.run(BrasileiraoApplication.class, args);
            }

        }
    }

}
