# Prakhar Goyal
**AI Engineer — Multi-Agent Systems & Applied Finance AI**

Bengaluru, India · prakhar3949@gmail.com · +91 [—— to fill] · [linkedin.com/in/prakhar3949](https://linkedin.com/in/prakhar3949) · [prakhar3949.github.io](https://prakhar3949.github.io)

---

## Summary
Data scientist and AI engineer with **9+ years** building and shipping ML systems end-to-end — from modeling to production MLOps. Drove **$150M+ in incremental revenue** at FedEx through ML-powered retention and lifetime-value products. Now focused on **multi-agent systems**: agents that debate, critique, and revise each other's outputs (reflexion), orchestrated with LangGraph and grounded in a 30+ tool quantitative-finance suite — plus a deep-agent research platform with a full AgentOps layer. MS in Business Analytics (GPA 3.96).

---

## Core Skills
**GenAI / LLM:** LLM application & agent design, ReAct agentic frameworks (LangGraph), Retrieval-Augmented Generation (RAG), prompt engineering, embeddings, tool-use/function-calling, Claude & OpenAI APIs, multi-agent orchestration
**Agent Orchestration:** Multi-agent debate/collaboration patterns, reflexion (self-critique-and-revise loops), supervisor/hierarchical agent teams, LangChain `deepagents`, human-in-the-loop (HITL) approval gates, MCP servers
**Evaluation & Guardrails:** RAGAS, LLM-as-judge, Langfuse/LangSmith tracing, prompt-injection defense, Pydantic structured-output validation
**MLOps & Engineering:** MLflow, Azure Data Factory (ADF), Terraform (IaC), Databricks, CI/CD for ML, model monitoring/alerting, PySpark, Python, SQL, Snowflake
**Machine Learning:** Forecasting & time series (ARIMA, UCM), gradient boosting (LightGBM, XGBoost), BTYD/CLV modeling, SVM, random forests, recommendation/collaborative filtering, A/B testing
**Cloud & Data:** Azure, Databricks, Snowflake, MSSQL, vector DBs (Chroma/Pinecone/Qdrant), large-scale data mining, Tableau

---

## Experience

### Independent AI Engineering — Applied GenAI Projects · 2025 – Present · Bengaluru

### Applied AI Project — Bull/Bear Thesis Debate Agents · 2026
- Built a **multi-agent debate system (LangGraph)** — a Bull agent and Bear agent argue opposing investment theses on a ticker using the existing 30+ tool suite, with a Judge agent scoring argument strength and producing a balanced research memo.
- Added a **reflexion loop**: each agent critiques and revises its own prior argument round before the next, instead of a single-shot take.
- Reused the **HITL approval gate** pattern from the multi-agent research platform before publishing the final memo.

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
