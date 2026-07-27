"""JD -> tailored resume picker/generator.

Compliant alternative to LinkedIn-API automation: you paste a JD (LinkedIn only
lets you copy the text anyway), this scores it against every
`Prakhar-Goyal-Resume-*.md` variant using each resume's own Core Skills /
RAG-architecture keywords, then copies the best-fit variant into
`generated/<Company>_<Role>.md` (title line swapped to the JD's role name)
and renders it to .docx via md_to_docx.convert().

Usage:
    python generate_resume.py path/to/jd.txt --company Acme --role "GenAI Engineer"
    python generate_resume.py path/to/jd.txt --company Acme --role "GenAI Engineer" --top 3

If --company/--role are omitted, the script tries to guess the role title from
the JD's first non-empty line and falls back to "Role" / "Company".
"""
import argparse
import re
from pathlib import Path

from md_to_docx import convert

HERE = Path(__file__).resolve().parent
GENERATED = HERE / "generated"

# Skill/keyword sets per resume variant, used to score a JD against it.
# Keep in sync with resume-lib.md §5/§7 when a new variant is added.
VARIANT_KEYWORDS = {
    "Prakhar-Goyal-Resume-Future-RAGReliability.md": [
        "corrective rag", "crag", "ragas", "llm-as-judge", "llm as judge",
        "faithfulness", "guardrail", "guardrails", "prompt injection",
        "red team", "red-team", "red teaming", "llm gateway", "gateway",
        "pydantic", "nemo guardrails", "llama guard", "langfuse", "langsmith",
        "hallucination", "evaluation", "eval harness", "observability",
        "reliability", "safety", "owasp",
    ],
    "Prakhar-Goyal-Resume-Future-AgenticMemory.md": [
        "agentic rag", "agentic", "autonomous agent", "persistent memory",
        "long-term memory", "long term memory", "episodic memory",
        "semantic memory", "procedural memory", "multi-hop", "multi hop",
        "langgraph", "deepagents", "deep agent", "subagent", "sub-agent",
        "basestore", "mcp", "model context protocol", "human-in-the-loop",
        "hitl", "agent orchestration", "multi-agent", "agent memory",
    ],
    "Prakhar-Goyal-Resume-Future-ModularGraphRAG.md": [
        "graphrag", "knowledge graph", "neo4j", "graph database",
        "modular rag", "entity", "entities", "relations", "hyde",
        "rag-fusion", "rag fusion", "hybrid search", "reranking", "rerank",
        "multi-hop reasoning", "graph traversal",
    ],
    "Prakhar-Goyal-Resume-Future-MultiAgentDebate.md": [
        "multi-agent debate", "debate", "reflexion", "self-critique",
        "critique and revise", "bull", "bear", "judge agent",
        "multi-agent collaboration", "supervisor agent", "hierarchical agent",
        "agent team", "orchestration", "collaborative agents",
    ],
    "Prakhar-Goyal-Resume-Future-CareerOpsAgent.md": [
        "pii", "pii sanitization", "pii redaction", "resume", "job description",
        "jd parsing", "fit scoring", "applicant tracking", "career", "ats",
        "resume tailoring", "interview prep", "document rag", "pdf qa",
    ],
    "Prakhar-Goyal-Resume-GenAI-2026.md": [
        "rag", "retrieval augmented generation", "langchain", "prompt engineering",
        "llm application", "generative ai", "genai", "openai", "claude",
        "anthropic", "embeddings", "tool use", "function calling", "vector db",
        "vector database", "chatbot", "conversational ai",
    ],
    "Prakhar-Goyal-Resume-SeniorDS-2026.md": [
        "data scientist", "forecasting", "time series", "arima", "lightgbm",
        "xgboost", "gradient boosting", "clv", "lifetime value", "churn",
        "propensity", "a/b testing", "ab testing", "mlops", "mlflow",
        "databricks", "azure data factory", "terraform", "pyspark",
        "recommendation", "clustering", "random forest", "svm",
    ],
}


def score_jd(jd_text: str) -> list[tuple[str, int, list[str]]]:
    text = jd_text.lower()
    results = []
    for variant, keywords in VARIANT_KEYWORDS.items():
        hits = [kw for kw in keywords if kw in text]
        results.append((variant, len(hits), hits))
    return sorted(results, key=lambda r: r[1], reverse=True)


def guess_role_title(jd_text: str) -> str:
    for line in jd_text.splitlines():
        line = line.strip()
        if line:
            return line[:80]
    return "Role"


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip()
    return re.sub(r"[\s]+", "_", text) or "Untitled"


def build_resume(variant_path: Path, role_title: str | None) -> str:
    lines = variant_path.read_text(encoding="utf-8").splitlines()
    if role_title:
        for i, line in enumerate(lines):
            if line.strip().startswith("**") and line.strip().endswith("**"):
                lines[i] = f"**{role_title}**"
                break
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("jd_file", help="Path to a .txt file containing the pasted job description")
    ap.add_argument("--company", default=None, help="Company name, used in the output filename")
    ap.add_argument("--role", default=None, help="Role title to put on the resume header (defaults to guessed JD title)")
    ap.add_argument("--top", type=int, default=1, help="How many ranked candidates to print (default 1)")
    ap.add_argument("--use", default=None, help="Force a specific variant filename instead of the top-scored one")
    args = ap.parse_args()

    jd_text = Path(args.jd_file).read_text(encoding="utf-8")
    ranked = score_jd(jd_text)

    print("Fit ranking (keyword-overlap score):")
    for variant, score, hits in ranked[: max(args.top, 1)]:
        hit_str = ", ".join(hits) if hits else "(no keyword hits)"
        print(f"  {score:>2}  {variant}")
        print(f"      matched: {hit_str}")

    winner = args.use or ranked[0][0]
    variant_path = HERE / winner
    if not variant_path.exists():
        raise SystemExit(f"Variant not found: {variant_path}")

    role_title = args.role or guess_role_title(jd_text)
    company = args.company or "Company"

    GENERATED.mkdir(exist_ok=True)
    out_name = f"{slugify(company)}_{slugify(role_title)}"
    out_md = GENERATED / f"Prakhar-Goyal-Resume-{out_name}.md"
    out_md.write_text(build_resume(variant_path, role_title), encoding="utf-8")

    convert(out_md)
    print(f"\nGenerated: {out_md.name} (based on {winner})")
    print(f"Docx: {out_md.with_suffix('.docx').name}")
    print("Review before sending — swap placeholder project dates for actuals once the flagship project is really built.")


if __name__ == "__main__":
    main()
