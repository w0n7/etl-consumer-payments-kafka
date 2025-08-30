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

Setup Rápido
1. Docker Compose

Arquivo docker-compose.yml já inclui:

Kafka + Zookeeper

Postgres

Grafana

docker-compose up -d

2. Producer (Spring Boot)

Endpoint: POST /payments/generate

Payload exemplo:

{
  "amount": 150.0,
  "method": "pix"
}


Resposta do servidor:

{
  "paymentId": "f5c6f769-c24f-464d-a972-c409311fc83a",
  "paymentDate": "2025-08-29T19:39:23+00:00",
  "amount": 150.0,
  "method": "pix"
}

3. Kafka

Broker: localhost:29092

Tópico: payments-topic

Mensagens JSON com campos: paymentId, paymentDate (UTC), amount, method.

4. ETL Python

Instale dependências:

pip install confluent-kafka psycopg2-binary python-dateutil


Configure .env:

KAFKA_BROKER=localhost:29092
POSTGRES_URL=postgresql://postgres:postgres@localhost:5435/payments-kafka-db


Execute:

python etl.py


Converte paymentDate para UTC.

Evita duplicidade (ON CONFLICT DO NOTHING).

Logs mostram pagamentos processados.

5. Postgres

Banco: payments-kafka-db

Tabela payments:

Campo	Tipo
payment_id	VARCHAR PRIMARY KEY
payment_date	TIMESTAMP WITH TIME ZONE
amount	NUMERIC
method	VARCHAR
6. Grafana

URL: http://localhost:3000

User: admin / Password: admin

Configure datasource apontando para Postgres

Dashboards sugeridos:

Total de pagamentos por método

Valor acumulado diário

Média de valores por método
