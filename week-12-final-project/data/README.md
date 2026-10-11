# Project Data

The Week 12 final project is based on the supplied Great Learning data archive.

Files committed for the Colab workflow:

- `delivery_logs.csv` — supplied shipment status events and free-text driver notes.
- `ground_truth.csv` — supplied expected exception, resolution, escalation, and tone labels.
- `customers.csv` — customer table exported from the supplied `customers.db` SQLite database.
- `lockers.csv` — locker table exported from the supplied `customers.db` SQLite database.
- `exception_resolution_playbook.txt` — text extracted from the supplied `exception_resolution_playbook.pdf`; page markers are retained so retrieval results can still cite the source page.

The CSV/text representations allow the project to run directly from GitHub/Colab without committing credentials or requiring binary-file handling in the notebook. They preserve the records and policy content used by the supplied database and playbook.

The original Great Learning archive remains the authoritative source. No API keys or endpoint URLs belong in this folder or anywhere in the repository.
