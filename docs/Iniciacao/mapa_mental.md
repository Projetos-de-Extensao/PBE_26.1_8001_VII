---
id: mapa_mental
title: Mapas Mentais
---
 
## Introdução
 
<p align = "justify">
Mapa mental consiste em criar resumos cheios de símbolos, cores, setas e frases de efeito com o objetivo de organizar o conteúdo e facilitar associações entre as informações destacadas. Esse material é muito indicado para pessoas que têm facilidade de aprender de forma visual.
</p>
 
## Metodologia
 
<p align = "justify">
Foram levantados pontos chaves do nosso projeto para que possamos orgalizá-los de uma forma fácil e rápida de entender. Foi Utilizado o PlantUML.
</p>
 
## Mapa mental

```plantuml
@startmindmap
<style>
mindmapDiagram {
    .main {
        BackgroundColor #0000FF
        FontColor white
        FontSize 22
    }

    .5w2h {
        BackgroundColor #FF0080
    }
    .pesquisa {
        BackgroundColor #FFFF00
    }
    .entrega {
        BackgroundColor #00FF80
    }

}
</style>

* **Sistema de Validação de Estágio** <<main>>

** Objetivo <<entrega>>
*** Tornar mais fácil a validação de Estágio

** Brainstorm (Processo) <<pesquisa>>
*** Cadastrar Cliente
****_ Moderador faz login e autoriza cadastro
****_ Cliente preenche formulário
*** Cadastrar estágio
****_ Cliente insere contrato e os documentos
****_ Informações passam pela validação
****_ Estágio é aprovado ou não, indicando pendências

** Vantagens <<5w2h>>
***_ Acompanhamento em tempo real
***_ Rapidez e eficiência, além de segurança

left side

** 5W2H <<5w2h>>
*** What: Plataforma de validação de estágio
*** Why: Para facilitar a integração e tornar o processo de estágio mais eficiente
*** Who: IBMEC
*** How: Metodologia RUP/UP e Django/Python

** Pesquisa <<pesquisa>>
*** **Lei 11.788 do Estágio**
*** Relatório de Estágio Obrigatório
*** Legislação MEC
*** Regulamento IBMEC

** A entregar <<entrega>>
*** Documentação
*** Protótipo de Baixa Fidelidade

@enduml
```

## Referências

> PlantUML. Disponível em: https://www.planttext.com/
 

## Versionamento
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 07/04/2026 | 1.0 | Criação do documento | Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Avarenga |
