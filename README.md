# Integração de APIs para CRM e recuperação de carrinhos abandonados

## Repositório do Trabalho de Conclusão de Curso

Este repositório contém OS códigos utilizados no Trabalho de Conclusão de Curso do MBA em Engenharia de Software da USP/ESALQ.

O trabalho analisa uma arquitetura de integração baseada em APIs para conectar plataformas de e-commerce, processamento em nuvem e sistemas de Customer Relationship Management (CRM), com foco na recuperação de carrinhos abandonados e na otimização financeira das operações digitais.

A arquitetura analisada envolve a integração entre:

- Shopify (e-commerce)
- Google Cloud Platform (middleware e processamento)
- Apache Kafka (mensageria orientada a eventos)
- Salesforce Marketing Cloud (ativação de CRM)

## Objetivo do repositório

O objetivo deste repositório é apresentar os códigos que representam etapas importantes da arquitetura proposta no trabalho.

Os scripts aqui disponibilizados ilustram como ocorre a coleta de dados via API, o envio de eventos para uma plataforma de mensageria e a identificação de carrinhos abandonados em ambiente analítico.

## Estrutura do repositório

O repositório contém três arquivos principais:

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
