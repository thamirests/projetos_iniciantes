package com.ChuteCerto.brasileirao.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
// Esta classe é para configurações da web, como ThymeLeaf.
// Por agora, não precisamos de configurações explícitas aqui,
// mas é bom ter o pacote para futuras expansões.
// Por exemplo, você pode configurar ViewResolvers personalizados, etc.

@Configuration
public class WebConfig implements WebMvcConfigurer {
    // Nenhuma configuração específica é necessária para Thymeleaf funcionar com Spring Boot defaults.
    // Mas esta classe pode ser usada para configurar:
    // - Adicionar View Controllers
    // - Configurar CORS
    // - Adicionar Resource Handlers para arquivos estáticos fora de /static
}
