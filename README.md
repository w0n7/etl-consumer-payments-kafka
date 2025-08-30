# 🏦 Payment ETL Application

![Java](https://img.shields.io/badge/Java-21-blue)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.2-green)
![Python](https://img.shields.io/badge/Python-3.12-yellow)
![Kafka](https://img.shields.io/badge/Kafka-3.7-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Yes-lightgrey)
![Grafana](https://img.shields.io/badge/Grafana-11-red)

---

## 🌐 Visão Geral

Essa aplicação demonstra um **pipeline de pagamentos em tempo real**, integrando:

- **Spring Boot Producer** → gera pagamentos e publica no Kafka  
- **Kafka** → mensageria confiável  
- **ETL Python** → consome Kafka, converte datas para UTC e insere no Postgres  
- **Postgres** → armazena os pagamentos  
- **Grafana** → dashboards e métricas

O fluxo garante **consistência de dados, escalabilidade e observabilidade**.

---

## 🏗 Arquitetura

```mermaid
flowchart LR
    A[Spring Boot Producer] -->|JSON Payment| B[Kafka Broker]
    B -->|Message| C[Python ETL Consumer]
    C -->|Insert| D[Postgres DB]
    D --> E[Grafana Dashboard]
```
## 🛠 Tecnologias

| Componente | Tecnologia  | Ícone                                                                                         |
| ---------- | ----------- | --------------------------------------------------------------------------------------------- |
| Producer   | Spring Boot | ![Spring](https://img.shields.io/badge/SpringBoot-3.2-green?logo=springboot\&logoColor=white) |
| Broker     | Kafka       | ![Kafka](https://img.shields.io/badge/Kafka-3.7-orange?logo=apachekafka\&logoColor=white)     |
| ETL        | Python      | ![Python](https://img.shields.io/badge/Python-3.12-yellow?logo=python\&logoColor=white)       |
| Banco      | PostgreSQL  | ![Postgres](https://img.shields.io/badge/Postgres-16-blue?logo=postgresql\&logoColor=white)   |
| Dashboards | Grafana     | ![Grafana](https://img.shields.io/badge/Grafana-11-red?logo=grafana\&logoColor=white)         |
| Contêiner  | Docker      | ![Docker](https://img.shields.io/badge/Docker-Yes-lightgrey?logo=docker\&logoColor=white)     |

