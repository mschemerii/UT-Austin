# Week 12 Final Project

## AI-Powered Last-Mile Delivery Exception Handling Automation

This folder contains the Week 12 full-code final project for the UT Austin / Great Learning Agentic AI coursework.

## Project objective

Build a proof-of-concept multi-agent system that processes last-mile delivery exceptions end to end. The solution classifies exceptions, selects policy-grounded resolution actions, determines supervisor escalation, generates customer communication, validates agent output, and evaluates the complete workflow.

## Submission path

This project uses the **full-code** submission path. The final deliverable will be an executed Jupyter notebook exported to **HTML** only after every cell runs successfully from top to bottom.

## Folder structure

```text
week-12-final-project/
├── README.md
├── Week_12_Final_Project_Full_Code.ipynb
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

Clone the repository and move into the project directory before running the notebook:

```python
!git clone https://github.com/mschemerii/UT-Austin.git
%cd /content/UT-Austin/week-12-final-project
```

Then open/run `Week_12_Final_Project_Full_Code.ipynb` and execute all cells sequentially. If execution exposes a defect, make the correction on the execution-results branch rather than editing `main` directly.

## Git workflow

1. Scaffold changes are merged through PR #1.
2. Project data and the reviewed notebook are developed and reviewed through PR #2.
3. Execution fixes and real model results use a separate follow-up branch/PR.
4. The final executed notebook is exported to HTML only after the run is clean and the metrics have been reviewed.

## Current status

The data/notebook branch contains the project implementation, evaluation logic, security controls, critic retries, document citations, and all ten test-case execution logic. API credentials and the endpoint remain in Colab only. Quantitative conclusions will be based on the real executed results, not fabricated values.
