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
- Learning resources: [Production RAG with LangChain & Vector DBs — Full Course](https://www.youtube.com/watch?v=mHxLXzYjQRE) (start here) · [Hybrid Search (BM25) + Re-ranking + HyDE](https://www.youtube.com/watch?v=YNcoFoRwoc8) · [LangGraph RAG + FastAPI (sessions, history, vector DB)](https://www.youtube.com/watch?v=t209A887UpY) · [Pinecone + Cohere re-ranking + OpenAI](https://www.youtube.com/watch?v=zKjh6Y7OZiM) · [RAG from scratch — ingestion to vector DB](https://www.youtube.com/watch?v=MykcjWPJ6T4)

### P2 — RAG Evaluation Framework *(closes: eval & observability — the #1 differentiator)*
**Build:** Wrap P1 with an eval harness measuring **retrieval precision/recall, answer faithfulness, answer relevance** using **RAGAS** + an **LLM-as-judge**, traced in **LangSmith or Langfuse**. Produce a dashboard of scores across a labeled question set.
- Resume line: *"Designed an eval framework (RAGAS + LLM-as-judge, Langfuse tracing) measuring faithfulness/precision/recall; caught and fixed a 22% hallucination rate on ambiguous queries."*
- Effort: ~3–4 days. **Highest signal-per-hour — do it second.**
- Learning resources: [Intro to RAGAS — LLM vs Non-LLM metrics](https://www.youtube.com/watch?v=gqei4BhDT1E) (start here) · [Evaluating RAG Pipelines with Ragas](https://www.youtube.com/watch?v=2ReYkiz2Jyc) · [RAG Observability & Evals with Langfuse](https://www.youtube.com/watch?v=h5hqelg0_wc) · [Dataset creation + LLM-as-a-Judge (RAGAS + Qdrant)](https://www.youtube.com/watch?v=pX9xzZNJrak) · [LLM-as-a-Judge in Langfuse](https://www.youtube.com/watch?v=JOGMn5nqCSM)

### P3 — Multi-agent equity-research crew *(closes: agentic frameworks, multi-agent design, tool-use)*
**Build:** Refactor your existing 30-tool suite into an explicit **LangGraph** (or **CrewAI**) graph: *Planner → Fundamentals agent → Technicals agent → Macro agent → Risk/Editor agent*, each calling your existing tools, producing a research memo. Add **Human-in-the-Loop interrupt** before "publish."
- This is the project that converts your hand-rolled orchestration into a *named, hireable* architecture.
- Resume line: *"Architected a LangGraph multi-agent research system (planner + specialist agents + HITL approval) orchestrating 30+ financial tools."*
- Effort: ~1.5 weeks. **Your flagship — leans on work you've already done.**
- Learning resources: [LangChain Academy — Intro to LangGraph (free, official)](https://academy.langchain.com/courses/intro-to-langgraph) (start here — canonical; state, checkpointing, HITL) · [LangGraph workflows & multi-agent patterns — supervisor / hierarchical / collaborative (docs)](https://docs.langchain.com/oss/python/langgraph/workflows-agents) (read the **supervisor** pattern — that's your Planner→specialists topology) · [LangGraph Complete Course For Beginners — Zero to Hero](https://www.youtube.com/watch?v=DtW_Lc9hYoU) · [Complete LangGraph Tutorial Beginner→Advanced 2026](https://www.youtube.com/watch?v=Hz21KVo0t4E) · [Building Human-in-the-Loop Agentic Workflows (Towards Data Science)](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows/) — for the pre-publish approval gate · [Multi-Agent AI end-to-end: LangGraph + MCP + A2A](https://appscale.blog/en/blog/build-multi-agent-ai-system-langgraph-mcp-a2a-beginner-tutorial-2026) (supervisor + SQLite checkpointing + HITL; also previews P5)
- Detail worth getting right: `interrupt_before` on **write/publish** nodes (approve *before* it acts), `interrupt_after` on the Editor node (review the memo *after* it drafts). Interviewers probe this distinction.

### P4 — Guardrails + safety layer *(closes: guardrails, prompt-injection, structured output)*
**Build:** Add a defense layer to P3: input filtering, **prompt-injection** tests, **output schema validation** (Pydantic/structured outputs), tool-scope restrictions, and **NeMo Guardrails or Llama Guard**. Write a short red-team report.
- Resume line: *"Implemented layered guardrails (input/output filtering, schema validation, tool-scope limits) + a prompt-injection red-team suite."*
- Effort: ~3–4 days.
- Learning resources: [Essential Guide to LLM Guardrails — Llama Guard vs NeMo (Medium)](https://medium.com/data-science-collective/essential-guide-to-llm-guardrails-llama-guard-nemo-d16ebb7cbe82) (start here — frames the layers before you pick a tool) · [NeMo Guardrails — official docs](https://docs.nvidia.com/nemo/guardrails/latest/index.html) + [GitHub](https://github.com/NVIDIA-NeMo/Guardrails) (Colang 2.0 rails) · [IBM LLM-guardrails hands-on notebook](https://github.com/IBM/ibmdotcom-tutorials/blob/main/generative-ai/llm-guardrails.ipynb) · [Langfuse — LLM Security & Guardrails](https://langfuse.com/docs/security-and-guardrails) (wires straight into your P2 tracing) · [LLM Guardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-reference-2026)
- Red-team suite: [Promptfoo LLM red-teaming guide (official)](https://www.promptfoo.dev/docs/red-team/) + [How to red-team RAG apps](https://www.promptfoo.dev/docs/red-team/rag/) (50+ vuln types — this *is* your red-team report) · [Promptfoo Red Teaming — beginner walkthrough (video)](https://www.youtube.com/watch?v=y6Dlsz5P8s8) · [Garak + PyRIT + Promptfoo compared (tutorial)](https://ransomnews.com/red-team-llm-app-garak-pyrit-promptfoo-tutorial/)
- Practical stack to land on: **Prompt Guard 2 (86M)** as the cheap fast first filter (~20–50ms), **Llama Guard** for hazard classification, **NeMo** for dialogue-flow rails, **Pydantic** for output schema. Note in the README that NVIDIA still labels NeMo beta/"not production as-is" — saying that out loud reads as judgment, not ignorance.

**What red teaming actually is:** deliberately attacking your own system to find failure modes before a real adversary or user does — the adversarial counterpart to normal evals. Normal eval (P2/RAGAS) asks "does it work on typical inputs?"; red teaming asks "can it be made to misbehave under intentional, worst-case pressure?" For a RAG/agent system specifically, that means testing: **jailbreaks** (bypassing refusal behavior), **prompt injection** (malicious instructions hidden in a retrieved doc, e.g. a poisoned 10-K filing telling the agent to ignore its system prompt), **data exfiltration** (tricking the agent into leaking context/secrets), **excessive agency** (agent taking an irreversible action — like actually placing a trade — without the HITL gate from P3 catching it), and **bias/harmful-content elicitation**. Output is a report of found vulnerabilities feeding back into guardrails/system-prompt hardening — it's continuous, not a one-time checkbox. The Promptfoo links above (50+ vuln types, RAG-specific guide) are literally a red-team suite you can point P4's report at.
- Learning resources: [Red Teaming LLM Applications — DeepLearning.AI × Giskard (free)](https://www.deeplearning.ai/courses/red-teaming-llm-applications) (start here — hands-on manual + automated red-teaming, prompt injection, OWASP Top 10 for LLMs, open-source Giskard tooling) · [DeepTeam — free open-source LLM red-teaming framework](https://appsecsanta.com/deepteam) · [8-Week AI Red Teaming Transition Course (GitHub, free)](https://github.com/Vect0rdecay/ai-red-team-course)

### P5 — MCP server for your finance tools *(closes: MCP, modern tool exposure)*
**Build:** Expose a few of your tools (GEX profile, sector rotation) as an **MCP server** so any MCP-compatible agent (Claude Desktop, etc.) can call them. Small but very current — few candidates have shipped MCP.
- Resume line: *"Published an MCP server exposing financial-analysis tools to any MCP-compatible LLM client."*
- Effort: ~2–3 days.
- Learning resources: [Anthropic — Introduction to MCP (free, official course)](https://anthropic.skilljar.com/introduction-to-model-context-protocol) (start here — servers *and* clients from scratch in Python; the three primitives) · [Anthropic — MCP Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) (sampling, notifications, transports) · [MCP docs — Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) · [DeepLearning.AI × Anthropic — MCP: Build Rich-Context AI Apps](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) · [Building Agents with MCP — full workshop, Mahesh Murag/Anthropic](https://www.youtube.com/watch?v=kQmXtrmQ5Zg) (the best single talk on *why* MCP) · [FastMCP in Python: build a real MCP server](https://www.danilchenko.dev/posts/fastmcp-mcp-server/) · [MCP server with Python, Docker & Claude Code (freeCodeCamp)](https://www.freecodecamp.org/news/how-to-build-an-mcp-server-with-python-docker-and-claude-code/) (the Docker angle plays to your MLOps edge)
- Build with **FastMCP** (ships inside the official `mcp` SDK; powers most MCP servers in the wild). `pip install "mcp[cli]"` — the `[cli]` extra gives you `mcp dev` (hot-reload + Inspector) and `mcp install` (one-shot Claude Desktop registration).
- Scope it right: expose GEX profile / sector rotation as **tools**, `watchlist.json` + `etf-holdings.json` as **resources**, and a canned "analyze this ticker" as a **prompt** — hitting all three primitives is what separates this from a toy.

### P6 *(optional, medium priority)* — LoRA/QLoRA fine-tune *(closes: fine-tuning)*
**Build:** Fine-tune a small open model (Llama/Mistral 7-8B) with **QLoRA** on a narrow finance task (e.g., classify filing sentiment or tag risk factors), and write up **"when fine-tuning beat RAG and when it didn't."** The *judgment* write-up matters more than the weights.
- Effort: ~1 week, needs a GPU (Colab/Modal/RunPod). Do only if a target role explicitly asks for fine-tuning.

---

## 1b. RAG architecture variants — beyond naive RAG

P1 ships naive RAG (retrieve → stuff → generate). These are the named architectures interviewers probe for once you claim "RAG experience" — know what each solves and where it'd slot into P1/P7.

| Architecture | How it works | Failure mode it fixes |
|---|---|---|
| **Naive/Standard RAG** | Embed query → top-k retrieve → stuff into prompt → generate | Baseline (what P1 ships) |
| **Corrective RAG (CRAG)** | Grades retrieval quality (relevant/ambiguous/irrelevant); falls back to web search or query rewrite when retrieval is weak | Bad retrieval silently producing a bad answer |
| **Adaptive RAG** | Router decides per-query whether to skip retrieval, do single-step, or multi-step retrieval | Wasted latency/cost on queries that don't need retrieval |
| **Self-RAG** | Model emits reflection tokens critiquing its own retrieval/output; can re-retrieve or discard | Self-critique without a separate grader model |
| **Autonomous/Agentic RAG** | Agent plans which retrievers/tools to call and how many hops, decides when to stop | Complex multi-step research beyond one vector store |
| **Cache-Augmented RAG** | Caches frequent chunks or precomputed KV-cache states so repeat/similar queries skip retrieval | Latency/cost on high-traffic or repetitive queries |
| **RAG + persistent memory** | Adds a long-term memory store (facts about user/session) alongside the corpus retriever | Standard RAG is stateless per-query; this adds continuity across sessions — this *is* the "BaseStore persistent memory" swap in P7 |
| **GraphRAG** | Builds a knowledge graph (entities + relations) from the corpus, retrieves via graph traversal/community summaries | Multi-hop reasoning and whole-corpus summarization that flat vector search handles poorly |
| **HyDE** | LLM generates a hypothetical answer first, embeds *that*, retrieves against it | Query/answer embedding-space mismatch |
| **Fusion RAG (RAG-Fusion)** | Generates multiple query variants, retrieves per variant, merges via reciprocal rank fusion | Sensitivity to a single poorly-phrased query |
| **Modular RAG** | Retrieval/routing/reranking/generation as swappable pipeline modules, not a fixed chain | The production shape most LlamaIndex/LangGraph RAG pipelines actually take |

**Where to land it:** P1 ships naive + hybrid search + reranking. Pick **one** of Corrective or Adaptive RAG as a P1 stretch goal (both are a LangGraph conditional edge, not a rebuild) to preempt the "have you gone beyond naive RAG?" interview question. GraphRAG is a good P7 add-on if a role's JD mentions knowledge graphs.

- Learning resources: [NirDiamant/RAG_Techniques (GitHub — free, notebook-per-technique)](https://github.com/NirDiamant/rag_techniques) (start here — covers CRAG, Self-RAG, Adaptive RAG, HyDE, RAG-Fusion, GraphRAG each as a standalone runnable notebook) · [Implementing Corrective RAG (CRAG) with LangGraph](https://www.coursesidekick.com/computer-science/32909672) · [7 Free Courses to Master RAG 2026 (Turing Post roundup)](https://www.turingpost.com/p/7-free-courses-to-master-rag) · [12 Best RAG Courses 2026, Free & Paid (Class Central)](https://www.classcentral.com/report/best-rag-courses/) · [Agentic Knowledge Graph Construction — DeepLearning.AI (free)](https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/information) (GraphRAG-adjacent, teaches agent-built knowledge graphs) · [The Complete Guide to RAG Architectures: Naive → Agentic (Medium, free)](https://atul4u.medium.com/the-complete-guide-to-rag-architectures-from-naive-to-agentic-c90c8a87cf56)

---

## 1c. Agent memory types

Distinct from the RAG corpus above — this is what an *agent* remembers about itself/the user across turns and sessions. Maps directly onto the P7 "persistent BaseStore memory" line and the memory categories your own dev tooling uses.

| Type | What it stores | Example | Maps to |
|---|---|---|---|
| **Episodic memory** | Specific past events/interactions — "what happened, when" | "User asked me to re-run the GEX profile on 2026-07-20" | Session/conversation history, LangGraph checkpointer |
| **Semantic memory** | General facts, decoupled from when/how learned | "User is a data scientist," "the portfolio benchmark is Nifty 50" | A fact store / user-profile memory |
| **Procedural memory** | *How* to do things — learned skills, workflows, corrected behavior | "When the user says 'don't mock the DB,' always hit the real DB in tests" | Learned system-prompt rules, fine-tuned policy |
| **Working memory** | Short-term, in-context only, cleared after the task | The current conversation's context window | LLM context window itself |

**Why it matters for the roadmap:** P7's "ephemeral → BaseStore persistent" backend swap is exactly semantic + episodic memory becoming durable across runs. If a JD mentions "agent memory," this taxonomy (not just "vector DB") is the vocabulary they're checking for.

- Learning resources: [Long-Term Agentic Memory With LangGraph — DeepLearning.AI (free, taught by Harrison Chase)](https://www.deeplearning.ai/courses/long-term-agentic-memory-with-langgraph) (start here — explicitly teaches semantic/episodic/procedural memory in LangGraph agents) · [Agent Memory: Building Memory-Aware Agents — DeepLearning.AI (free)](https://www.deeplearning.ai/courses/agent-memory-building-memory-aware-agents) (tools-as-procedural-memory, episodic→semantic consolidation) · [LLMs as Operating Systems: Agent Memory — DeepLearning.AI × Letta (free)](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory/) · [NirDiamant/Agent_Memory_Techniques (GitHub — free, 30 notebooks)](https://github.com/NirDiamant/Agent_Memory_Techniques) (MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks) · [Memory for agents (LangChain blog, free)](https://www.langchain.com/blog/memory-for-agents) · [A Practical Guide to Memory for Autonomous LLM Agents (Towards Data Science, free)](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/)

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
