# 🏦 Payment ETL Application

![Java](https://img.shields.io/badge/Java-17-blue)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.2-green)
![Python](https://img.shields.io/badge/Python-3.12-yellow)
![Kafka](https://img.shields.io/badge/Kafka-3.7-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Yes-lightgrey)
![Grafana](https://img.shields.io/badge/Grafana-11-red)

---

## 🌐 Visão Geral

Essa aplicação demonstra um **pipeline de dados de pagamentos em tempo real**:

<div align="center">
  <img src="https://raw.githubusercontent.com/yourusername/assets/main/payment-etl-diagram.png" alt="Diagrama Arquitetural" width="700"/>
</div>

**Descrição do fluxo:**

1. **Producer (Spring Boot)** gera pagamentos e publica no Kafka.
2. **Kafka** atua como broker, garantindo entrega confiável.
3. **ETL (Python)** consome, converte datas para UTC e insere no Postgres.
4. **Postgres** armazena os pagamentos.
5. **Grafana** exibe dashboards e métricas em tempo real.

---

## 🏗 Arquitetura com ícones

```mermaid
flowchart LR
    A["<img src='https://img.shields.io/badge/SpringBoot-Producer-blue?logo=springboot&logoColor=white' width='100'/>"] -->|JSON Payment| B["<img src='https://img.shields.io/badge/Kafka-Broker-orange?logo=apachekafka&logoColor=white' width='100'/>"]
    B -->|Message| C["<img src='https://img.shields.io/badge/Python-ETL-yellow?logo=python&logoColor=white' width='100'/>"]
    C -->|Insert| D["<img src='https://img.shields.io/badge/Postgres-DB-blue?logo=postgresql&logoColor=white' width='100'/>"]
    D --> E["<img src='https://img.shields.io/badge/Grafana-Dashboard-red?logo=grafana&logoColor=white' width='100'/>"]
