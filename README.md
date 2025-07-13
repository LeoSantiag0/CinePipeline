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

## 🏗 Arquitetura da Solução

![Arquitetura do Projeto](docs/architecture.png)

> A arquitetura segue o padrão bronze → silver → gold com ingestão via Python, transformação com dbt + DuckDB e visualização com Streamlit.

---

## 📊 Modelagem Conceitual

| Tabela             | Tipo     | Descrição                                 |
|--------------------|----------|-------------------------------------------|
| `filmes_raw`       | Bronze   | Dados brutos extraídos da API             |
| `filmes`           | Silver   | Filmes com atributos normalizados         |
| `generos`          | Silver   | Dimensão com os gêneros dos filmes        |
| `elenco`           | Silver   | Atores principais extraídos por filme     |
| `filme_elenco`     | Silver   | Tabela de relacionamento N:N (filme ↔ ator) |
| `diretores`        | Silver   | Diretores por filme                       |
| `estudios`         | Silver   | Estúdios produtores                       |
| `filmes_trusted`   | Gold     | Base final consolidada para análise/ML    |
| `filmes_previstos` | Gold     | Filmes futuros com notas previstas        |

---

## ⚙️ Como rodar o projeto

### 1. Configurar variáveis de ambiente

Crie seu arquivo `.env` baseado no `.env.example`:

```bash
cp .env.example .env
Preencha sua TMDb API Key e demais configurações.

2. Instalar dependências
bash
Copiar
Editar
pip install -r requirements.txt
3. Rodar ingestão de dados
bash
Copiar
Editar
python ingestao_tmdb.py
4. Rodar transformação (com dbt + DuckDB)
bash
Copiar
Editar
cd transform/
dbt run
5. Rodar previsão de nota (ML)
bash
Copiar
Editar
python predict.py
6. Visualizar painel com resultados
bash
Copiar
Editar
streamlit run dashboard.py
🧾 Documentação Auxiliar
📘 Glossário de Dados

🔄 Linhagem de Dados

🛣️ Roadmap do Projeto

🔧 Boas Práticas de Git

📦 Tecnologias Utilizadas
Python (requests, pandas, scikit-learn, streamlit)

API TMDb (dados públicos de filmes)

S3 / MinIO (armazenamento de dados)

DuckDB (data warehouse leve e local)

dbt (transformações SQL com versionamento)

Streamlit (painel de visualização interativa)

Airflow (opcional) (orquestração local)

📌 Status do Projeto
✅ Iniciado | 🔄 Em desenvolvimento | 📈 Em breve: dashboard com previsões

👨‍💻 Autor
Leonardo Santiago
LinkedIn
GitHub: @leonardosantiago

📄 Licença
Este projeto é para fins exclusivamente educacionais e não possui fins comerciais.