# GenAI / Deep-Agents Skill Roadmap — Bangalore market, tied to your edge

Built from a scan of live Bengaluru/India GenAI & LLM-engineer postings (Naukri, Indeed, LinkedIn) in June 2026. Goal: close the gap between your **DS/MLOps strength** and what **GenAI/agentic roles actually ask for**, using your **AI-hedgefund finance project + 9 yrs domain** as the authentic substrate (hiring managers spend more time on your GitHub than your resume).

---

## 1. Most-common JD asks, ranked by frequency

| Tier | Ask (appears in ~most JDs) | What it concretely means | Your status |
|------|----------------------------|--------------------------|-------------|
| **Must-have** | **RAG pipelines** | Chunking, embeddings, vector store, retrieval, reranking, grounding/citations | 🟡 Partial — you do "RAG-style" data context, not a real vector-DB RAG yet |
| **Must-have** | **Agent / multi-agent frameworks** | LangGraph (leader), LangChain, CrewAI, AutoGen, OpenAI Agents SDK, **Claude Agent SDK** | 🟡 You hand-rolled tool orchestration; need a named framework |
| **Must-have** | **Vector databases** | FAISS, Chroma, Pinecone, Qdrant, Weaviate | 🔴 Gap |
| **Must-have** | **Python + API serving** | FastAPI/Flask, function-calling, JSON/structured output, streaming (SSE/WebSockets) | 🟢 Strong Python; 🟡 need FastAPI serving habit |
| **Must-have** | **LLM APIs** | OpenAI, Anthropic/Claude, Gemini, AWS Bedrock, Azure OpenAI | 🟢 Claude API (your project) |
| **High** | **Prompt engineering** | System prompts, few-shot, structured output, tool-use design | 🟢 Good (your tool suite) |
| **High** | **Evaluation & observability** | "Single best signal of real LLM experience" — retrieval precision/recall, faithfulness, relevance, LLM-as-judge, tracing (LangSmith/Langfuse) | 🔴 Gap — highest-leverage thing to add |
| **High** | **Guardrails / safety** | Input+output filtering, prompt-injection defense, tool-scope limits, Llama Guard / NeMo Guardrails | 🔴 Gap |
| **High** | **MLOps / deployment** | Docker, K8s, CI/CD, monitoring, cost tracking, vLLM/Triton serving | 🟢 Strong (ADF/MLflow/Terraform/Databricks) — your differentiator |
| **Medium** | **Fine-tuning** | LoRA/QLoRA, when-to-fine-tune-vs-RAG judgment | 🔴 Gap (nice-to-have, not gating) |
| **Medium** | **MCP (Model Context Protocol)** | Standard for exposing tools/data to agents | 🔴 Gap (fast-rising) |
| **Medium** | **Cost optimization** | Token budgeting, caching, model routing (small vs frontier) | 🟡 You do caching; frame it |
| **High (frontier)** | **Deep agents / AgentOps** | LangChain `deepagents` harness — middleware, subagents/agent teams, persistent backends, context compression + prompt caching; operating agents with guardrails/evals/memory/tracing | 🔴 Gap — covered in §2b + P7 (staff-level differentiator) |

**Read:** Your moat is **MLOps + finance domain + production discipline** — most GenAI applicants can call an API but can't ship/operate. Your gaps are all on the **agentic-framework, vector-RAG, eval, and guardrails** axis. The projects below are sequenced to close exactly those, in priority order, each producing a GitHub repo + demo.

---

## 2. Project ladder (each = 1 GitHub repo + README + demo link)

Every project deliberately reuses your finance domain so it reads as *depth*, not a tutorial clone. Ship each with: a README (problem, architecture diagram, eval numbers), a `Dockerfile`, a FastAPI endpoint, and a short Loom/GIF.

### P1 — Production RAG over financial filings *(closes: RAG, vector DB, FastAPI, grounding)*
**Build:** Ingest SEC 10-K/10-Q + earnings transcripts (you already pull EDGAR in the suite) → chunk → embed → **Chroma/FAISS** → retrieval + **reranking** → answer with **inline citations**. Add **hybrid search** (semantic + keyword).
- Stack: LangChain or LlamaIndex, Chroma → then swap to Pinecone/Qdrant to show portability, FastAPI, OpenAI/Claude.
- Resume line: *"Built a production RAG system over SEC filings with hybrid retrieval + reranking, served via FastAPI, grounded answers with citations."*
- Effort: ~1 week. **Start here.**

### P2 — RAG Evaluation Framework *(closes: eval & observability — the #1 differentiator)*
**Build:** Wrap P1 with an eval harness measuring **retrieval precision/recall, answer faithfulness, answer relevance** using **RAGAS** + an **LLM-as-judge**, traced in **LangSmith or Langfuse**. Produce a dashboard of scores across a labeled question set.
- Resume line: *"Designed an eval framework (RAGAS + LLM-as-judge, Langfuse tracing) measuring faithfulness/precision/recall; caught and fixed a 22% hallucination rate on ambiguous queries."*
- Effort: ~3–4 days. **Highest signal-per-hour — do it second.**

### P3 — Multi-agent equity-research crew *(closes: agentic frameworks, multi-agent design, tool-use)*
**Build:** Refactor your existing 30-tool suite into an explicit **LangGraph** (or **CrewAI**) graph: *Planner → Fundamentals agent → Technicals agent → Macro agent → Risk/Editor agent*, each calling your existing tools, producing a research memo. Add **Human-in-the-Loop interrupt** before "publish."
- This is the project that converts your hand-rolled orchestration into a *named, hireable* architecture.
- Resume line: *"Architected a LangGraph multi-agent research system (planner + specialist agents + HITL approval) orchestrating 30+ financial tools."*
- Effort: ~1.5 weeks. **Your flagship — leans on work you've already done.**

### P4 — Guardrails + safety layer *(closes: guardrails, prompt-injection, structured output)*
**Build:** Add a defense layer to P3: input filtering, **prompt-injection** tests, **output schema validation** (Pydantic/structured outputs), tool-scope restrictions, and **NeMo Guardrails or Llama Guard**. Write a short red-team report.
- Resume line: *"Implemented layered guardrails (input/output filtering, schema validation, tool-scope limits) + a prompt-injection red-team suite."*
- Effort: ~3–4 days.

### P5 — MCP server for your finance tools *(closes: MCP, modern tool exposure)*
**Build:** Expose a few of your tools (GEX profile, sector rotation) as an **MCP server** so any MCP-compatible agent (Claude Desktop, etc.) can call them. Small but very current — few candidates have shipped MCP.
- Resume line: *"Published an MCP server exposing financial-analysis tools to any MCP-compatible LLM client."*
- Effort: ~2–3 days.

### P6 *(optional, medium priority)* — LoRA/QLoRA fine-tune *(closes: fine-tuning)*
**Build:** Fine-tune a small open model (Llama/Mistral 7-8B) with **QLoRA** on a narrow finance task (e.g., classify filing sentiment or tag risk factors), and write up **"when fine-tuning beat RAG and when it didn't."** The *judgment* write-up matters more than the weights.
- Effort: ~1 week, needs a GPU (Colab/Modal/RunPod). Do only if a target role explicitly asks for fine-tuning.

---

## 2b. Deep Agents & AgentOps — the advanced frontier (2026)

Beyond basic agents, the hireable edge in 2026 is the **"deep agent"** pattern (LangChain's `deepagents` harness — the batteries-included successor to raw LangGraph loops) plus **AgentOps** (operating agents in production). These map directly to senior/staff GenAI roles.

### Deep Agents — concepts to learn
| Concept | What it is | Why it matters in JDs |
|---------|-----------|------------------------|
| **Deep agent** | An agent that can **plan, delegate, and reason across many steps** with built-in planning, a virtual filesystem for context, and subagent spawning — `create_deep_agent()` | Handles long-horizon tasks (research memos, multi-doc analysis) that single-shot agents can't |
| **Middleware** | How `deepagents` injects capabilities into a LangGraph agent — each feature is a separate middleware. Defaults: **to-do/planning middleware**, **filesystem middleware**, **subagent middleware** | "Middleware architecture" = the customization surface; knowing it signals real depth, not API-calling |
| **Customizing deep agents** | Add/remove/configure middleware, custom system prompts, custom tools, context-compression + prompt-caching middleware to cut latency/cost | Senior roles want agents *tuned* for a domain, not defaults |
| **Backend agents** | Two state backends: **BaseStore (persistent)** vs **agent-state (ephemeral)** for the agent filesystem/memory | Production memory/persistence is a recurring ask |
| **Subagents / agent teams** | `SubAgentMiddleware` adds a **task tool** to delegate multi-step subtasks to specialist subagents that return clean results to the orchestrator | This is "multi-agent system design" — top-3 most-requested skill |
| **AgentOps** | Operating agents in prod: **guardrails, LLM evals, memory, tracing/observability, cost & latency control, prompt caching** (the AgentOps course scope: AI guardrails + LLM evals + memory + AgentOps) | Eval + observability is the **single best signal of real LLM experience** per hiring managers |

### P7 — Deep-agent equity-research system + AgentOps (capstone) *(advanced)*
**Build:** Re-implement P3 using LangChain **`deepagents`** instead of a hand-built graph:
- `create_deep_agent()` orchestrator with **subagents** (fundamentals / technicals / macro / risk) via `SubAgentMiddleware` (this *is* your "agent team").
- **Customize the middleware:** domain system prompts, your finance tools, **context-compression + prompt-caching** middleware; swap the **backend** from ephemeral → **BaseStore persistent** so the agent remembers prior research runs (memory).
- **AgentOps wrap:** guardrails (P4), eval harness (P2), tracing (Langfuse/LangSmith), cost/latency dashboard, HITL approval before publish.
- Resume line: *"Built a deep-agent research platform (LangChain `deepagents`) with a 4-subagent team, custom middleware (context compression, prompt caching), persistent BaseStore memory, and a full AgentOps layer — guardrails, RAGAS evals, tracing, and cost monitoring."*
- Effort: ~2 weeks. **This is your staff-level showcase — do it after P1–P4.**

> Learning resources: LangChain [Deep Agents docs](https://docs.langchain.com/oss/python/deepagents/overview) · [deepagents GitHub](https://github.com/langchain-ai/deepagents) · [SubAgentMiddleware ref](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware) · AgentOps course: [AI Security / Guardrails / LLM Evals / Memory / AgentOps (8h)](https://www.youtube.com/watch?v=rQE3w8Qjx98).

---

## 3. Suggested sequence & timeline (part-time)
1. **Week 1:** P1 (RAG) → **Week 2:** P2 (Eval) — together these two make you immediately credible.
2. **Weeks 3–4:** P3 (multi-agent flagship).
3. **Week 5:** P4 (guardrails) + P5 (MCP) — both short.
4. **Weeks 6–7:** P7 (deep-agent + AgentOps capstone) — the staff-level showcase.
5. **Optional:** P6 (fine-tuning) when a role demands it.

After P1–P3, **rewrite the resume Projects section** to feature them (I'll update both variants), and they become your strongest interview talking points — far better than the current single AI-hedgefund line.

## 4. Concrete next setup steps (so you can start P1 today)
- `pip install langchain langchain-community llama-index chromadb sentence-transformers fastapi uvicorn ragas` (+ `langfuse`)
- Reuse your existing EDGAR fetch from `fundamentals-scanner.py` / `fundamental-thesis.py` for the document source.
- Repo naming: `genai-finance-rag`, `rag-eval-harness`, `equity-research-agents`, `finance-guardrails`, `finance-mcp-server`.

---

### Sources
- [Naukri — GenAI / RAG / LangChain jobs](https://www.naukri.com/gen-ai-jobs) · [Indeed India — LLM/GenAI/LangGraph](https://in.indeed.com/q-llm,gen-ai,-langchain,langgraph-jobs.html)
- [Agentic AI Engineer guide (NovelVista)](https://www.novelvista.com/blogs/ai-and-ml/agentic-ai-engineer-career-guide) · [LLM Engineer roadmap 2026 (KDnuggets)](https://www.kdnuggets.com/the-roadmap-to-becoming-an-llm-engineer-in-2026)
- [15 AI Engineer skills 2026 (AY Automate)](https://www.ayautomate.com/blog/ai-engineer-skills-2026) · [RAG Engineer JD (upGrad)](https://www.upgrad.com/blog/rag-engineer-job-description/)
- [10 AI-agent portfolio projects that get you hired (AgenticCareers)](https://agenticcareers.co/blog/ai-agent-portfolio-projects-get-hired-2026) · [Top AI agent projects (DataCamp)](https://www.datacamp.com/blog/top-ai-agent-projects) · [500-AI-Agents-Projects (GitHub)](https://github.com/ashishpatel26/500-AI-Agents-Projects)
