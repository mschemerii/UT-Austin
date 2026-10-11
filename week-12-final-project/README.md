# Week 12 Final Project

## AI-Powered Last-Mile Delivery Exception Handling Automation

This folder contains the Week 12 full-code final project for the UT Austin / Great Learning Agentic AI coursework.

## Project objective

Build a proof-of-concept multi-agent system that processes last-mile delivery exceptions end to end. The solution classifies exceptions, selects policy-grounded resolution actions, determines supervisor escalation, generates customer communication, validates agent output, and evaluates the complete workflow.

## Submission path

This project uses the **full-code** submission path. The final deliverable will be an executed Jupyter notebook exported to **HTML** only after every cell runs successfully from top to bottom.

## Canonical execution branch

All active execution work stays on:

`week-12-execution-results`

Do not use the older project-data branch for Colab runs.

## Canonical notebook

Use only:

`week-12-final-project/Week_12_Final_Project_Colab_Ready.ipynb`

The older duplicate notebook has been removed from this branch to prevent opening the wrong file.

## Folder structure

```text
week-12-final-project/
├── README.md
├── EXECUTION.md
├── Week_12_Final_Project_Colab_Ready.ipynb
├── config.example.json
└── data/
    ├── README.md
    ├── customers.csv
    ├── lockers.csv
    ├── delivery_logs.csv
    ├── exception_resolution_playbook.txt
    └── ground_truth.csv
```

`customers.csv` and `lockers.csv` are table exports from the supplied SQLite database. `exception_resolution_playbook.txt` is a page-marked text extraction of the supplied playbook PDF so retrieval citations retain source page numbers.

## Google Colab credentials

The OpenAI-compatible API key and Great Learning endpoint are kept **only in Google Colab Secrets**. Nothing secret is committed to GitHub.

Create these secrets in Colab and enable notebook access:

- `OPENAI_API_KEY`
- `OPENAI_API_BASE`

The notebook also accepts `OPENAI_BASE_URL` as an alternate endpoint secret name.

## Running in Colab

Open the canonical notebook from the `week-12-execution-results` branch. Its first cell clones or refreshes that same branch into `/content/UT-Austin`, moves into `week-12-final-project`, and verifies the required project data files.

The notebook then validates Colab secrets, explicitly configures Bearer authentication for the Great Learning OpenAI-compatible endpoint, and runs an API connection test before the multi-agent workflow begins.

## Git workflow

1. Scaffold changes were merged through PR #1.
2. Project data and the reviewed notebook were merged through PR #2.
3. All execution fixes and real model results stay on `week-12-execution-results` in PR #3.
4. The final executed notebook is exported to HTML only after the run is clean and the metrics have been reviewed.

## Current status

The execution branch contains one canonical Colab notebook, the project data, the evaluation logic, security controls, critic retries, document citations, and all ten test-case execution logic. API credentials and the endpoint remain in Colab only. Quantitative conclusions will be based on the real executed results, not fabricated values.
