# Resume Component Library — Prakhar Goyal

Single source of truth for every resume variant. When a new JD or project lands, edit a block **here first**, then copy into whichever `Prakhar-Goyal-Resume-*.md` file(s) need it — keeps all variants consistent instead of drifting. `md_to_docx.py` only reads the final per-variant `.md` files, not this one; this file is the reference/assembly layer.

Decision log: **CRAG over Adaptive RAG** as the flagship reliability pattern (see §Projects → P-Reliable-RAG). Reason: CRAG's self-grading + fallback loop is the more interview-legible story ("the system catches its own bad retrievals and fixes them") and pairs directly with the RAGAS/guardrails narrative. Adaptive RAG (skip/single/multi-hop routing) is one paragraph in the same project's README as a secondary technique, not a separate flagship.

---

## 1. Identity block (fixed — every resume)
```
# Prakhar Goyal

Bengaluru, India · prakhar3949@gmail.com · +91 [—— to fill] · [linkedin.com/in/prakhar3949](https://linkedin.com/in/prakhar3949) · [prakhar3949.github.io](https://prakhar3949.github.io)
```
Role subtitle (the `**bold**` line right after `# Prakhar Goyal`) changes per variant — see §5.

---

## 2. Experience blocks (fixed — reuse verbatim across all variants; this is real work history, don't touch)

### FedEx Services — Senior Data Scientist, Marketing · Dec 2022 – Apr 2025
```
*Stack: Databricks, PySpark, BTYD, LightGBM, MLflow, Azure Data Factory, Terraform*
- Built and productionized a **Proactive Retention model** (extended BTYD with a covariate-expansion layer) that drove **$150M+ net incremental revenue over two years**.
- Owned **end-to-end MLOps**: automated retraining pipelines via ADF + Terraform (IaC); MLflow experiment tracking for precision, revenue, and volume trends.
- Delivered a **new-customer Lifetime Value model** for accounts < 6 months old — full product build (pipelines, IaC, monitoring triggers/alarms) plus a monthly performance dashboard.
```

### Circle K — Data Scientist · Oct 2020 – Nov 2022
```
*Stack: PySpark, Databricks, time series (UCM), clustering, XGBoost, collaborative filtering*
- Developed price-elasticity + UCM time-series models powering a **localized pricing program across 21 business units**; built a nonlinear optimization process and an expected-vs-observed lift measurement framework.
- Built an **assortment recommendation engine** specifying per-store add/drop decisions.
```

### AIG Analytics & Services — Business Analyst (Data Scientist) · Jul 2015 – Oct 2018
```
*Stack: Random Forest, LightGBM, SVM, TF-IDF, Python, MSSQL, Snowflake, Tableau, A/B testing*
- **Policy-churn model** (SVM + TF-IDF on policy attributes) predicting cancellation pre-expiry — accuracy, precision, recall, and F-score all **> 95%**.
- **Propensity model** (gradient boosting) identifying high-conversion customers + driver analysis with A/B validation; cut marketing spend **~10%**.
- **Fraud-detection model** (Random Forest on historical claims + global CLUE data) reducing false positives and improving Claims resource allocation **~20%**.
```

## 3. Education block (fixed)
```
## Education
**M.S., Business Analytics** — University of Cincinnati, Lindner College of Business · 2020 · **GPA 3.96/4.0**
**B.Tech, Electronics & Communication** — The LNM Institute of Information Technology, Jaipur · 2014
```

## 4. Legacy "Selected Projects" block (fixed, optional filler — use only if space allows)
```
## Selected Projects
- **Optical Digit Recognition** — CNN (Keras) achieving **99.42%** accuracy with hyperparameter tuning; packaged as a Python/tkinter app.
- **Bitcoin Price Forecasting** — seasonal ARIMA model with EDA-driven differencing; deployed via R/Shiny.
```

---

## 5. Skill-category blocks (mix per variant)

**GenAI / LLM — core (all variants):**
`LLM application & agent design, ReAct agentic frameworks (LangGraph), Retrieval-Augmented Generation (RAG), prompt engineering, embeddings, tool-use/function-calling, Claude & OpenAI APIs, multi-agent orchestration`

**RAG architectures (variant-dependent — pick per flagship project):**
`Corrective RAG (CRAG), Adaptive RAG, Self-RAG, Agentic/autonomous RAG, GraphRAG, Modular RAG, HyDE, RAG-Fusion, hybrid search (BM25 + vector), reranking, persistent-memory RAG`

**Evaluation & Observability:**
`RAGAS, LLM-as-judge, faithfulness/precision/recall metrics, retrieval eval design, Langfuse / LangSmith tracing`

**Guardrails & Safety:**
`Input/output filtering, prompt-injection defense, Pydantic structured-output validation, NeMo Guardrails, Llama Guard, red-teaming (Promptfoo), OWASP Top 10 for LLMs`

**LLM Gateways & Cost Ops:**
`Multi-provider LLM gateway routing (LiteLLM-style), fallback/failover across models, token budgeting, cost & latency monitoring, prompt caching`

**Agent Orchestration / Deep Agents:**
`LangGraph, LangChain deepagents (planning + filesystem + subagent middleware), MCP (Model Context Protocol) servers, persistent agent memory (episodic/semantic/procedural, BaseStore backend), human-in-the-loop (HITL) approval gates`

**Machine Learning (all variants):**
`Forecasting & time series (ARIMA, UCM), gradient boosting (LightGBM, XGBoost), BTYD/CLV modeling, SVM, random forests, recommendation/collaborative filtering, A/B testing, NLP (TF-IDF), CNNs`

**MLOps & Engineering (all variants):**
`MLflow, Azure Data Factory (ADF), Terraform (IaC), Databricks, CI/CD for ML, model monitoring/alerting, PySpark, Python, SQL, Snowflake`

**Cloud & Data (all variants):**
`Azure, Databricks, Snowflake, MSSQL, vector DBs (Chroma/Pinecone/Qdrant), Neo4j (graph), large-scale data mining, Tableau`

---

## 6. Flagship project blocks (target-state — write these once each project in `genai-skill-roadmap.md` P1/P2/P3/P4/P7 actually ships)

### P-Reliable-RAG — "Reliable RAG Platform" (CRAG + RAGAS + guardrails + gateway) → anchors **Future-RAGReliability** variant
```
### Applied AI Project — Reliable RAG Platform for Financial Filings · 2026
- Built a **Corrective RAG (CRAG)** pipeline over SEC filings/earnings transcripts that self-grades retrieval relevance and falls back to query rewrite or web search on weak retrieval, cutting hallucinations on ambiguous queries.
- Designed a **RAGAS + LLM-as-judge eval harness** (faithfulness, answer relevance, context precision/recall) traced through **Langfuse**, used to measure and drive down hallucination rate on a labeled question set.
- Layered **guardrails** (input/output filtering, Pydantic schema validation, prompt-injection defenses) and ran a **red-team suite (Promptfoo)** against the pipeline; documented findings and fixes.
- Routed all model traffic through an **LLM gateway** for multi-provider fallback, token budgeting, and cost/latency monitoring.
```

### P-Agentic-Memory — "Agentic RAG with Persistent Memory" → anchors **Future-AgenticMemory** variant
```
### Applied AI Project — Agentic RAG with Persistent Memory · 2026
- Architected an **agentic RAG system (LangGraph)** that plans multi-hop retrieval and decides when to stop, instead of a fixed single-shot retrieve-then-generate loop.
- Added **persistent long-term memory** (episodic + semantic, BaseStore backend) so follow-up queries reuse prior research findings across sessions rather than re-retrieving from scratch.
- Carried the full reliability stack from the Reliable RAG Platform project into the agent loop: **CRAG self-correction, RAGAS/LLM-as-judge evals, guardrails, and LLM-gateway routing.**
```

### P-Modular-GraphRAG — "Modular RAG + GraphRAG" → anchors **Future-ModularGraphRAG** variant
```
### Applied AI Project — Modular RAG + Knowledge-Graph Retrieval · 2026
- Built a **modular RAG pipeline** (swappable retrieval/routing/reranking/generation stages) over a multi-source finance corpus, enabling component-level A/B testing without pipeline rewrites.
- Extended it with **GraphRAG** — a knowledge graph (companies/sectors/events as entities and relations, Neo4j) enabling multi-hop, whole-corpus questions that flat vector retrieval couldn't answer.
```

### P7 — Deep-Agent Research Platform (shared skill/project — include in **every** variant, verbatim)
```
### Applied AI Project — Deep-Agent Research Platform · 2026
- Built a deep-agent research platform (LangChain `deepagents`) with a **4-subagent team**, custom **middleware** (context compression, prompt caching), **persistent BaseStore memory**, and a full **AgentOps layer** — guardrails, RAGAS evals, tracing, and cost monitoring.
```

### P-MultiAgent-Debate — "Bull/Bear Thesis Debate Agents" → anchors **Future-MultiAgentDebate** variant
Pattern adapted from [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) — `agents/20-multi-agent-debate` and LangGraph's official "Multi-Agent Collaboration" / "Reflexion" tutorials — applied to the AI-hedgefund domain instead of copied as-is.
```
### Applied AI Project — Bull/Bear Thesis Debate Agents · 2026
- Built a **multi-agent debate system (LangGraph)** — a Bull agent and Bear agent argue opposing investment theses on a ticker using the existing 30+ tool suite, with a Judge agent scoring argument strength and producing a balanced research memo.
- Added a **reflexion loop**: each agent critiques and revises its own prior argument round before the next, instead of a single-shot take.
- Reused the **HITL approval gate** pattern from the multi-agent research platform before publishing the final memo.
```

### P-CareerOps-Agent — "Career-Ops Resume & Fit-Scoring Agent" → anchors **Future-CareerOpsAgent** variant
Pattern adapted from [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) industry use case **NextRole** ("tailors a resume to a JD and generates interview prep via a multi-agent system") and `agents/21-pii-sanitization-agent` — extends the JD→resume `generate_resume.py` tool already shipped in this repo into a real multi-agent LangGraph system.
```
### Applied AI Project — Career-Ops Resume & Fit-Scoring Agent · 2026
- Extended a keyword-matching JD→resume generator into a **multi-agent LangGraph system**: a JD-parsing agent extracts requirements, a fit-scoring agent weighs them against a resume component library, and an assembly agent drafts the tailored resume + a battlecard of gaps to address.
- Added a **PII-sanitization guardrail** stage before any JD/resume text is sent to an LLM provider, and **persistent memory** of past applications/outcomes to improve future fit-scoring.
- Grounded a PDF/document RAG stage over past job descriptions and interview notes (pattern from a PDF-QA agent), enabling "have I seen a role like this before?" queries.
```

---

## 7. Variant map

| Variant file | Target role framing | Flagship project (from §6) | + shared P7 project | + skill blocks used |
|---|---|---|---|---|
| `Prakhar-Goyal-Resume-Future-RAGReliability.md` | GenAI Engineer — RAG Reliability, Evaluation & Safety | P-Reliable-RAG | Yes | GenAI core, RAG architectures (CRAG-focused), Eval/Observability, Guardrails, LLM Gateways |
| `Prakhar-Goyal-Resume-Future-AgenticMemory.md` | AI Engineer — Agentic Systems & Applied GenAI | P-Agentic-Memory | Yes | GenAI core, RAG architectures (agentic/persistent-memory-focused), Agent Orchestration, Eval/Guardrails/Gateway (condensed) |
| `Prakhar-Goyal-Resume-Future-ModularGraphRAG.md` | GenAI Engineer — Knowledge Systems & RAG Architecture | P-Modular-GraphRAG | Yes | GenAI core, RAG architectures (modular/GraphRAG-focused), Cloud & Data (Neo4j emphasis) |
| `Prakhar-Goyal-Resume-Future-MultiAgentDebate.md` | AI Engineer — Multi-Agent Systems & Applied Finance AI | P-MultiAgent-Debate | Yes | GenAI core, Agent Orchestration, Eval/Guardrails (condensed) |
| `Prakhar-Goyal-Resume-Future-CareerOpsAgent.md` | AI Engineer — Applied Agentic Tooling | P-CareerOps-Agent | Yes | GenAI core, RAG architectures (condensed), Agent Orchestration, Guardrails (PII focus), Persistent memory |
| `Prakhar-Goyal-Resume-GenAI-2026.md` (existing, current) | Current-state GenAI resume — do not touch until P1–P4 actually ship | — (current AI-hedgefund line only) | No | current |
| `Prakhar-Goyal-Resume-SeniorDS-2026.md` (existing, current) | Current-state Senior DS resume | — | No | current |

**Important:** all `Future-*` variants describe projects **not yet built** (P1/P2/P3/P4/P7 in `genai-skill-roadmap.md`, plus P-MultiAgent-Debate and P-CareerOps-Agent, are still open). Do not send these out until the corresponding project has a real repo + demo — swap "2026" project dates and bullet specifics for actuals once shipped, and move the file out of "Future" naming at that point.

**Source reference:** [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) is a curated list of 500+ agent project patterns across LangGraph/CrewAI/AutoGen/Agno. Two blocks above (P-MultiAgent-Debate, P-CareerOps-Agent) adapt patterns from it to Prakhar's own finance/job-hunt domain — they are **not** claims of having built or contributed to that repo itself. Its `agents/` folder (self-contained runnable examples: PDF-QA, SQL-query, data-analysis, stock-research, PII-sanitization, multi-agent-debate, etc.) and its LangGraph framework table (official Adaptive/Agentic/Corrective/Self-RAG tutorial notebooks) are also useful **reference code** for the P-Reliable-RAG / P-Agentic-Memory / P-Modular-GraphRAG projects above when actually building them.
