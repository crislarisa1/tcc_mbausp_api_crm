# Integração de dados via APIs para otimização financeira

## Repositório do Trabalho de Conclusão de Curso

Este repositório contém os códigos utilizados no Trabalho de Conclusão de Curso do MBA em Engenharia de Software da USP/ESALQ.

O trabalho analisa uma arquitetura de integração baseada em APIs para conectar plataformas de e-commerce, processamento em nuvem e sistemas de Customer Relationship Management (CRM), com foco na recuperação de carrinhos abandonados e na otimização financeira das operações digitais.

A arquitetura analisada envolve a integração entre:

- Shopify (e-commerce)  
- Google Cloud Platform (middleware e processamento)  
- Apache Kafka (mensageria orientada a eventos)  
- Salesforce Marketing Cloud (ativação de CRM)

---

## Objetivo do repositório

O objetivo deste repositório é apresentar os códigos que representam etapas importantes da arquitetura proposta no trabalho.

Os scripts aqui disponibilizados ilustram como ocorre a coleta de dados via API, o envio de eventos para uma plataforma de mensageria e a identificação de carrinhos abandonados em ambiente analítico.

---

## Estrutura do repositório

O repositório contém quatro arquivos principais:

### main.py

Script Python responsável pela consulta de dados na **Shopify GraphQL Admin API**.

Este código demonstra como uma aplicação externa pode acessar informações de checkout da plataforma de e-commerce utilizando requisições HTTP autenticadas.

### kafka.py

Exemplo de publicação de eventos em um **cluster Apache Kafka**.

O script simula o envio de eventos de checkout para um tópico Kafka (`checkout-events`), permitindo o processamento assíncrono e desacoplado dos dados em arquiteturas orientadas a eventos.

### abandono_carrinho.sql

Consulta SQL utilizada para identificar **carrinhos abandonados** no ambiente analítico.

A regra considera:

- carrinhos não finalizados  
- tempo mínimo de inatividade de 1 hora  
- consentimento de marketing válido (RGPD)

Essa lógica permite selecionar apenas os registros elegíveis para estratégias de recuperação de carrinho no CRM.

### api_salesforce.py

Script Python responsável por demonstrar a integração com a **API REST do Salesforce Marketing Cloud**.

Este código exemplifica como os dados processados no ambiente analítico podem ser enviados para uma **Data Extension** no Salesforce Marketing Cloud utilizando requisições HTTP autenticadas.

O script realiza o envio de registros de carrinho abandonado contendo informações como a identificador do cliente (SubscriberKey), o identificador do checkout, o email do cliente, a data de criação do carrinho, o momento do abandono da compra e o valor estimado da compra.

Esse processo permite que os dados sejam posteriormente utilizados para ativação de jornadas automatizadas de recuperação de carrinho no CRM.

---

## Arquitetura simplificada do fluxo de dados

O fluxo de integração analisado no trabalho segue a seguinte lógica:
Shopify (GraphQL API) > Python Script (Cloud Function) > Apache Kafka (event streaming) > Google BigQuery (processamento e análise) > Python Script (API REST Salesforce) > Salesforce Marketing Cloud (ativação de CRM)
