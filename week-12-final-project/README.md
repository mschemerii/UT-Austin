# Week 12 Final Project

## AI-Powered Last-Mile Delivery Exception Handling Automation

This folder contains the Week 12 full-code final project for the UT Austin / Great Learning Agentic AI coursework.

## Project objective

Build a proof-of-concept multi-agent system that processes last-mile delivery exceptions end to end. The solution classifies delivery exceptions, selects an appropriate resolution action using operational policy and customer/package context, determines when supervisor escalation is required, generates customer communication, and evaluates the resulting workflow.

## Submission path

This project uses the **full-code** submission path. The final deliverable will be an executed Jupyter notebook exported to **HTML** after all cells run successfully from top to bottom.

## Folder structure

```text
week-12-final-project/
├── README.md
├── Project 3 - Full-code Notebook.ipynb
├── config.example.json
└── data/
    ├── customers.db
    ├── delivery_logs.csv
    ├── exception_resolution_playbook.pdf
    └── ground_truth.csv
```

## Credentials

Do not commit API keys. Copy `config.example.json` to `config.json` locally and populate the required values before running the notebook. `config.json` is ignored by Git.

## Workflow

1. Develop changes on a feature branch.
2. Run and validate the notebook sequentially.
3. Commit only project code, data, and non-secret configuration examples.
4. Open a pull request into `main` for review.
5. After the final run, export the executed notebook to HTML for submission.

## Current status

The starter notebook has been completed with the multi-agent workflow, retrieval setup, prompts, evaluation logic, test-case execution scaffolding, aggregate metrics, and business conclusions/recommendations. The next step is to run the notebook against the Great Learning OpenAI-compatible endpoint and validate the real outputs before final submission.
