# 🎬 CinePipeline — Engenharia de Dados com TMDb API

Projeto educacional de engenharia de dados que utiliza a API pública da TMDb para construir uma pipeline completa: da ingestão à previsão de notas de filmes futuros com técnicas de Machine Learning.

---

## 📌 Objetivo

Criar uma pipeline profissional para:
- Ingerir dados públicos de filmes (API TMDb)
- Normalizar, tratar e transformar os dados
- Prever notas de filmes futuros com base em gênero, elenco, diretor e estúdio
- Visualizar os dados e previsões em um painel interativo

---

## 🧭 Premissas

- Projeto educacional
- Sem custos
- Stack em Python
- Engenharia de dados realista
- Com visão de ML e visualização final
- De forma alguma possuir fins comerciais

---

## 🚧 Status do Projeto

✅ Iniciado | 🔄 Em desenvolvimento

---

## 🏗️ Arquitetura da Solução

![Arquitetura do Projeto](docs/architecture.png)

> A arquitetura segue o padrão bronze → silver → gold com ingestão via Python, transformação com dbt + DuckDB e visualização com Streamlit.

---

## 📦 Tecnologias Utilizadas

| Camada                      | Tecnologia                                | Justificativa técnica                                                                  |
| --------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------- |
| 🌐 Origem dos Dados         | `APIs da TMDb`                            | Fonte pública e gratuita com dados ricos sobre filmes                                  |
| 🧪 Ingestão (API)           | `Python + requests`                       | Ideal para capturar dados da TMDb, leve e direto                                       |
| 🔐 Segredos                 | `dotenv`                                  | Evita expor API Keys. Padrão em projetos Python                                        |
| 🧺 Armazenamento bruto      | `MinIO`                                   | Armazenamento local compatível com S3, gratuito e ideal para desenvolvimento           |
| 🧮 Processamento e ETL      | `Pandas`                                  | Biblioteca robusta e consagrada para manipulação de dados tabulares                    |
| ⚙️ Orquestração             | `Airflow (local)`                         | Profissional e gratuito; pode rodar local com Docker                                   |
| ✨ Transformações analíticas | `dbt (com DuckDB)`                       | `dbt-core` com `DuckDB` para evitar custos com warehouses                              |
| 💾 Data Warehouse local     | `DuckDB`                                  | Data Warehouse leve e local                                                            |
| 📊 Visualização             | `Streamlit`                               | Roda local sem servidor, 100% Python. Visualização interativa                          |
| 🤖 Machine Learning         | `scikit-learn` + `pandas`                 | Conjunto padrão para modelagem supervisionada com ótimo desempenho                     |
| 📐 Modelagem Conceitual     | `dbdiagram.io`                            | Ferramenta online para criar diagramas ER claros e colaborativos                       |
| 🔄 Linhagem de Dados        | `OpenLineage`                             | Padrão aberto para rastreamento e controle de linhagem de dados                        |
| 📖 Glossário de Dados       | `Notion`, `Google Docs` ou Markdown       | Plataformas colaborativas para manter definição clara de termos e métricas             |
| 🏗 Arquitetura da Solução   | `Lucidchart`                              | Ferramenta visual para diagramas técnicos e fluxos, fácil de usar e compartilhar       |

---

## 🧾 Documentação Auxiliar

- 🧩 Modelagem Conceitual
- 📚 Glossário de Dados
- 🔗 Linhagem de Dados
- 🗺️ Roadmap do Projeto
- 🔧 Boas Práticas de Git

---

## ⚙️ Como rodar o projeto

```bash
1. Configurar variáveis de ambiente
Crie seu arquivo `.env` baseado no `.env.example`:
cp .env.example .env
Preencha sua TMDb API Key e demais configurações.

2. Instalar dependências
pip install -r requirements.txt

3. Rodar ingestão de dados
python ingestao_tmdb.py

4. Rodar transformação (com dbt + DuckDB)
cd transform/
dbt run

5. Rodar previsão de nota (ML)
python predict.py

6. Visualizar painel com resultados
streamlit run dashboard.py
```
---

## 👨‍💻 Autor
Leonardo Santiago  
- [LinkedIn](https://www.linkedin.com/in/leonardo-sposito-santiago)  
- [GitHub](https://github.com/LeoSantiag0)

---

## 🛡️ Licença
Este projeto é para fins exclusivamente educacionais e não possui fins comerciais. Utiliza a API pública da [TMDb](https://www.themoviedb.org/), porém **não é endossado ou certificado pela TMDb**.  
O uso da API respeita os [termos de uso da TMDb](https://www.themoviedb.org/documentation/api/terms-of-use) e é estritamente educacional e sem fins comerciais.