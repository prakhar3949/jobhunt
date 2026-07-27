# Prakhar Goyal
**GenAI Engineer — Knowledge Systems & RAG Architecture**

Bengaluru, India · prakhar3949@gmail.com · +91 [—— to fill] · [linkedin.com/in/prakhar3949](https://linkedin.com/in/prakhar3949) · [prakhar3949.github.io](https://prakhar3949.github.io)

---

## Summary
Data scientist and AI engineer with **9+ years** building and shipping ML systems end-to-end — from modeling to production MLOps. Drove **$150M+ in incremental revenue** at FedEx through ML-powered retention and lifetime-value products. Now focused on **knowledge-centric RAG architecture**: modular, swappable retrieval pipelines and knowledge-graph-based retrieval (GraphRAG) for multi-hop reasoning over large corpora — plus a deep-agent research platform with a full AgentOps layer. MS in Business Analytics (GPA 3.96).

---

## Core Skills
**GenAI / LLM:** LLM application & agent design, ReAct agentic frameworks (LangGraph), Retrieval-Augmented Generation (RAG), prompt engineering, embeddings, tool-use/function-calling, Claude & OpenAI APIs, multi-agent orchestration
**RAG Architectures:** Modular RAG, GraphRAG, hybrid search (BM25 + vector), reranking, HyDE, RAG-Fusion
**Knowledge & Graph Systems:** Knowledge-graph construction (entities/relations), graph traversal & community-summary retrieval, Neo4j, multi-hop reasoning over unstructured corpora
**Evaluation & Observability:** RAGAS, LLM-as-judge, faithfulness/precision/recall metrics, Langfuse/LangSmith tracing
**Guardrails & Cost Ops:** Prompt-injection defense, Pydantic structured-output validation, multi-provider LLM gateway routing, prompt caching, cost & latency monitoring
**MLOps & Engineering:** MLflow, Azure Data Factory (ADF), Terraform (IaC), Databricks, CI/CD for ML, model monitoring/alerting, PySpark, Python, SQL, Snowflake
**Cloud & Data:** Azure, Databricks, Snowflake, MSSQL, vector DBs (Chroma/Pinecone/Qdrant), Neo4j, large-scale data mining, Tableau

---

## Experience

### Independent AI Engineering — Applied GenAI Projects · 2025 – Present · Bengaluru

### Applied AI Project — Modular RAG + Knowledge-Graph Retrieval · 2026
- Built a **modular RAG pipeline** (swappable retrieval/routing/reranking/generation stages) over a multi-source finance corpus, enabling component-level A/B testing without pipeline rewrites.
- Extended it with **GraphRAG** — a knowledge graph (companies/sectors/events as entities and relations, Neo4j) enabling multi-hop, whole-corpus questions that flat vector retrieval couldn't answer.

### Applied AI Project — Deep-Agent Research Platform · 2026
- Built a deep-agent research platform (LangChain `deepagents`) with a **4-subagent team**, custom **middleware** (context compression, prompt caching), **persistent BaseStore memory**, and a full **AgentOps layer** — guardrails, RAGAS evals, tracing, and cost monitoring.

**AI Hedge-Fund Tooling Suite** — agentic, LLM-driven quantitative research system
- Architected an **agentic LLM system (Claude API)** orchestrating 30+ specialized analysis tools across market, options, macro, and fundamentals data — tool routing, function-calling, and automated multi-step reasoning.
- Engineered production-grade reliability: parallelized fetching, caching, scheduled CI runs (GitHub Actions), and per-component error isolation across the full suite.

### FedEx Services — Senior Data Scientist, Marketing · Dec 2022 – Apr 2025
*Stack: Databricks, PySpark, BTYD, LightGBM, MLflow, Azure Data Factory, Terraform*
- Built and productionized a **Proactive Retention model** (extended BTYD with a covariate-expansion layer) that drove **$150M+ net incremental revenue over two years**.
- Owned **end-to-end MLOps**: automated retraining pipelines via ADF + Terraform (IaC); MLflow experiment tracking for precision, revenue, and volume trends.
- Delivered a **new-customer Lifetime Value model** for accounts < 6 months old — built the full product (pipelines, IaC, monitoring triggers/alarms) and a monthly performance dashboard.

### Circle K — Data Scientist · Oct 2020 – Nov 2022
*Stack: PySpark, Databricks, time series (UCM), clustering, XGBoost, collaborative filtering*
- Developed price-elasticity + UCM time-series models powering a **localized pricing program across 21 business units**; built a nonlinear optimization process for product pricing and an expected-vs-observed lift framework.
- Built an **assortment recommendation engine** specifying per-store add/drop decisions.

### AIG Analytics & Services — Business Analyst (Data Scientist) · Jul 2015 – Oct 2018
*Stack: Random Forest, LightGBM, SVM, TF-IDF, Python, MSSQL, Snowflake, Tableau, A/B testing*
- **Policy-churn model** (SVM + TF-IDF on policy attributes) predicting cancellation pre-expiry — accuracy, precision, recall, and F-score all **> 95%**.
- **Propensity model** (gradient boosting) for high-conversion customers + driver analysis with A/B validation; cut marketing spend **~10%**.
- **Fraud-detection model** (Random Forest on historical claims + global CLUE data) that reduced false positives and improved Claims resource allocation **~20%**.

---

## Selected Projects
- **Optical Digit Recognition** — CNN (Keras) achieving **99.42%** accuracy with hyperparameter tuning; packaged as a Python/tkinter app.
- **Bitcoin Price Forecasting** — seasonal ARIMA model with EDA-driven differencing; deployed via R/Shiny.

---

## Education
**M.S., Business Analytics** — University of Cincinnati, Lindner College of Business · 2020 · **GPA 3.96/4.0**
**B.Tech, Electronics & Communication** — The LNM Institute of Information Technology, Jaipur · 2014
