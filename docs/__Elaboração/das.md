---
id: documento_de_arquitetura
title: Documento de Arquitetura
---
## Documento de Arquitetura de Software (DAS)

### "Nome do Projeto"

#### Introdução

##### Proposta

Este documento apresenta uma visão geral da arquitetura do sistema, utilizando diferentes visões arquiteturais para destacar diferentes aspectos do sistema. É utilizado para capturar as decisões arquiteturais significativas que fizeram parte do sistema.

## Escopo

A aplicação "XXXX" tem o objetivo fornecer...

## Definições, Acrônimos e Abreviações

- MVC -
- MVT -
- SIGLA PARA O APP - Nome do Aplicativo

## Visão Geral

O Documento de Arquitetura de Software (DAS) trata-se de uma visão geral de toda a arquitetura do sistema, observando diferentes aspectos do mesmo. Neste documento serão abordadas as seguintes visões da aplicação TCM:

- Caso de Uso;
- Lógica;
- Implantação;
- Implementação;
- Dados;

### Representação Arquitetural

#### Cliente-Servidor

Cliente-Servidor é um modelo de arquitetura...

Cliente (Frontend):

- View: Consiste.....

Servidor (Backend):

- Controller: faz a conexão entre as camadas...
- Service: Responsável pela lógica...
- Model: Responsável pela persistência...

### Objetivos de Arquitetura e Restrições

#### Objetivos

Segurança:

-

Persistência:

-

Privacidade:

- Middlewares: Foi usado middlewares...

Desempenho:
   Requisições...
Reusabilidade:
   Componentes no Frontend...

## Restrições

Tamanho da tela:...

Portabilidade:...

| IE | Edge  | Firefox | Chrome | Safari | Googlebot |
| -- | ----- | ------- | ------ | ------ | --------- |
| 11 | >= 14 | >= 52   | >= 49  | >= 10  | Sim       |

Serviços: Os serviços oferecidos....

Acesso a internet: A aplicação está limitada apenas a conexão com internet

## Ferramentas Utilizadas

- XXX: Ambiente de execução...
- XXXX: Linguagem de programação...
  Typescript: XXXX
- XXXX: XXXX
- XXX: XXXX
- XXXX: XXXX
- XXXX: XXXX
- XXXX: XXXX
- XXXXX: XXXX.

### Visão de Caso de Uso

O primeiro caso de uso descreve a ação...

![Caso de uso 1](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

![Caso de uso 2](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

### Visão Lógica

#### Visão de Implantação

##### Visão de Implementação

##### Visão Geral I

![Diagrama de Componentes](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

### Visão de Dados

#### Modelo Entidade Relacionamento (MER)

##### Entidades e Relacionamentos

### Diagrama Entidade Relacionamento (DER)

## Tamanho e Desempenho

## Qualidade

### Referências Bibliográficas

#### Histórico de Versão

| Data       | Versão | Descrição                                                            | Autor(es)                                   |
| ---------- | ------- | ---------------------------------------------------------------------- | ------------------------------------------- |
| 08/11/2020 | 1.0     | Criada estrutura básica do documento                                  | xxx xxx, xxx xx, xxx xx, xxx xxx e xxx xxxx |
| 15/11/2020 | 1.1     | Representação arquitetural e objetivos e restrições arquiteturais. | Autores                                     |
| 19/11/2020 | 1.2     | Adição dos diagramas, visões, tamanho e desempenho e qualidade      | Autores                                     |
| 20/11/2020 | 1.3     | Adição da descrição de MER e DER                                   | Autores                                     |
| 20/11/2020 | 1.4     | Adição do tópico de qualidade                                       | Autores                                     |
| 20/11/2020 | 1.5     | Revisão                                                               | Autores                                     |
