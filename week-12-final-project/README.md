# Project 3 - AI-Powered Last-Mile Delivery Exception Handling Automation

Full-code submission for the UT Austin / Great Learning Agentic AI program (Week 12).

## What is here

```text
week-12-final-project/
├── README.md
├── Project_3_Last_Mile_Delivery_Exception_Handling.ipynb   # the deliverable (built from the supplied starter notebook)
├── config.example.json                                     # credential template (copy to config.json, which is git-ignored)
└── data/
    ├── customers.db                                        # SQLite: customers (12) + lockers (6)
    ├── delivery_logs.csv                                   # 13 raw shipment events, 10 unique shipments
    ├── ground_truth.csv                                    # reference labels for evaluation
    └── exception_resolution_playbook.pdf                   # RAG source (10 pages)
```

## Architecture (LangGraph)

`preprocessor -> orchestrator <-> {resolution_agent, critic_resolution, communication_agent, critic_communication} -> finalize`

- **Deterministic:** dedup, noise filtering, prompt-injection guardrail, escalation rule engine, routing, revision-loop cap.
- **LLM:** Resolution Agent and Communication Agent (`gpt-4o-mini`); Critics and the coherence judge (`gpt-4o`).
- **Tools:** delivery-log reader, customer profile (PII redacted by default), locker eligibility, playbook RAG (Chroma + MiniLM, page citations), escalation rules.
- **Security:** injection scan on inputs and retrieved chunks, per-agent state views, PII only for the Communication Agent, read-only parameterized SQLite, Pydantic-validated outputs, secrets never printed.
- **Metrics:** Task Completion, Escalation Accuracy, Tool Call Accuracy, Reasoning Trajectory Coherence (LLM-as-a-Judge), Latency.

## Running it

1. Open the notebook in Google Colab (or Jupyter/VS Code) and run top to bottom.
2. Provide credentials by **one** of: `config.json` next to the notebook, Colab Secrets (`OPENAI_API_KEY`, `OPENAI_API_BASE`, optional `LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT`), or environment variables. Nothing secret is stored in the notebook or in Git.
3. If the data files are not next to the notebook, the first data cell fetches them from this repository (Colab only).
4. LangSmith tracing turns on automatically when a LangSmith key is present; otherwise it is disabled cleanly.

The notebook is committed **without outputs**. Every results section (per-case traces and citations, observations, aggregate metrics, results-driven conclusions) is generated from the live run, so run it once, then export the executed notebook (HTML) for submission.
