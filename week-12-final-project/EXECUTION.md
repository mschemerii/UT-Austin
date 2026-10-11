# Week 12 Execution and Final Results

This branch is reserved for the real Google Colab execution, any fixes discovered during that run, and the final evaluated results.

## Colab setup

Store the Great Learning OpenAI-compatible credentials only in Google Colab Secrets and enable notebook access:

- `OPENAI_API_KEY`
- `OPENAI_API_BASE`

Do not commit the key or endpoint URL to GitHub.

## Run procedure

1. In Colab, clone this execution branch:

```python
!git clone --branch week-12-execution-results https://github.com/mschemerii/UT-Austin.git
%cd /content/UT-Austin/week-12-final-project
```

2. Open `Week_12_Final_Project_Full_Code.ipynb`.
3. Run every cell sequentially from top to bottom.
4. If a cell fails, fix the defect on this branch and repeat the full run from a clean runtime.
5. Review all 10 shipment results, critic traces, playbook citations, and aggregate metrics.
6. Commit the fully executed `.ipynb` to this branch only after the notebook completes without errors.
7. Export the clean executed notebook to HTML for the Great Learning submission.

## Acceptance checklist

- [ ] All cells execute without warnings/errors that affect results.
- [ ] All 10 unique shipment test cases run.
- [ ] Task completion uses classification + resolution + tone as an all-or-nothing metric.
- [ ] Escalation accuracy is calculated against applicable ground-truth labels.
- [ ] Tool-call accuracy is displayed.
- [ ] Reasoning-trajectory coherence is displayed.
- [ ] End-to-end latency is displayed.
- [ ] Per-case playbook citations and traces are present.
- [ ] Aggregate metrics are reviewed for plausibility.
- [ ] Conclusions/recommendations reflect the actual executed metrics.
- [ ] No API key or endpoint URL appears in notebook output.
- [ ] Final HTML is produced only after the clean run.
