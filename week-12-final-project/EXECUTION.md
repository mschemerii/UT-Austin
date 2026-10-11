# Week 12 Execution and Final Results

This branch is reserved for the real Google Colab execution, any fixes discovered during that run, and the final evaluated results.

## Branch

Use only:

`week-12-execution-results`

## Canonical notebook

Use only:

`week-12-final-project/Week_12_Final_Project_Colab_Ready.ipynb`

The stale duplicate notebook has been removed from this branch.

## Colab setup

Store the Great Learning OpenAI-compatible credentials only in Google Colab Secrets and enable notebook access:

- `OPENAI_API_KEY`
- `OPENAI_API_BASE`

Do not commit the key or endpoint URL to GitHub.

## Run procedure

1. Open `Week_12_Final_Project_Colab_Ready.ipynb` from the `week-12-execution-results` branch in Colab.
2. Run the notebook from the first cell. The notebook clones or refreshes this same branch into `/content/UT-Austin` and verifies all required data files.
3. The notebook validates the Colab secrets and explicitly sends Bearer authentication to the Great Learning OpenAI-compatible endpoint.
4. The notebook performs an API test before the multi-agent test cases run.
5. Run every remaining cell sequentially from top to bottom.
6. If a cell fails, fix the defect on this same branch and repeat the full run from a clean runtime.
7. Review all 10 shipment results, critic traces, playbook citations, and aggregate metrics.
8. Commit the fully executed `.ipynb` to this branch only after the notebook completes without errors.
9. Export the clean executed notebook to HTML for the Great Learning submission.

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
