import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Week_12_Final_Project_Full_Code.ipynb"
TARGET = ROOT / "Week_12_Final_Project_Colab_Ready.ipynb"

with SOURCE.open("r", encoding="utf-8") as f:
    nb = json.load(f)


def md_cell(text, cell_id):
    return {
        "cell_type": "markdown",
        "id": cell_id,
        "metadata": {},
        "source": [line + "\n" for line in text.strip().splitlines()],
    }


def code_cell(code, cell_id):
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": cell_id,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in code.strip().splitlines()],
    }

bootstrap_md = md_cell(
    """# Colab bootstrap and project checks

When this notebook is opened directly from GitHub in Google Colab, the first cell clones or refreshes the `week-12-execution-results` branch, changes into the project directory, and verifies the required project data files.

The Great Learning API key and endpoint are read only from Google Colab Secrets and are never printed or committed.""",
    "colab-bootstrap-heading",
)

bootstrap_code = code_cell(
    r'''import os
import subprocess
from pathlib import Path

REPO_URL = "https://github.com/mschemerii/UT-Austin.git"
REPO_BRANCH = "week-12-execution-results"
REPO_DIR = Path("/content/UT-Austin")
PROJECT_DIR = REPO_DIR / "week-12-final-project"

def run_git(args, cwd=None, check=True):
    p = subprocess.run(["git", *args], cwd=cwd, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if check and p.returncode != 0:
        raise RuntimeError(p.stdout)
    return p.stdout.strip()

if not (REPO_DIR / ".git").exists():
    print(run_git(["clone", "--branch", REPO_BRANCH, "--single-branch", REPO_URL, str(REPO_DIR)]))
else:
    run_git(["fetch", "origin", REPO_BRANCH], cwd=REPO_DIR)
    run_git(["checkout", REPO_BRANCH], cwd=REPO_DIR)
    print(run_git(["pull", "--ff-only", "origin", REPO_BRANCH], cwd=REPO_DIR, check=False))

os.chdir(PROJECT_DIR)
required = [
    "data/delivery_logs.csv",
    "data/ground_truth.csv",
    "data/customers.csv",
    "data/lockers.csv",
    "data/exception_resolution_playbook.txt",
]
missing = [p for p in required if not Path(p).exists()]
if missing:
    raise FileNotFoundError("Missing project files: " + ", ".join(missing))

print("Working directory:", os.getcwd())
for p in required:
    print("✓", p)
print("Branch:", run_git(["branch", "--show-current"], cwd=REPO_DIR))
print("Commit:", run_git(["rev-parse", "--short", "HEAD"], cwd=REPO_DIR))''',
    "colab-bootstrap",
)

# Remove any previous generated bootstrap cells from the source copy.
nb["cells"] = [
    c for c in nb["cells"]
    if c.get("id") not in {"colab-bootstrap-heading", "colab-bootstrap", "api-auth-check"}
]
nb["cells"] = [bootstrap_md, bootstrap_code] + nb["cells"]

# Harden the existing credential/model cell without disturbing the rest of the notebook.
for cell in nb["cells"]:
    if cell.get("cell_type") != "code":
        continue
    src = "".join(cell.get("source", []))
    if "OPENAI_API_KEY" in src and "ChatOpenAI" in src:
        # Keep existing secret names but force standard env vars and explicit Authorization headers.
        if "AUTH_HEADERS" not in src:
            marker = "if not OPENAI_API_KEY or not OPENAI_API_BASE:\n    raise ValueError('Add OPENAI_API_KEY and OPENAI_API_BASE to Colab Secrets and enable notebook access.')\n"
            insert = marker + "\nos.environ['OPENAI_API_KEY'] = OPENAI_API_KEY.strip()\nos.environ['OPENAI_BASE_URL'] = OPENAI_API_BASE.strip().rstrip('/')\nOPENAI_API_KEY = os.environ['OPENAI_API_KEY']\nOPENAI_API_BASE = os.environ['OPENAI_BASE_URL']\nAUTH_HEADERS = {'Authorization': f'Bearer {OPENAI_API_KEY}'}\n"
            if marker in src:
                src = src.replace(marker, insert)
            else:
                src += "\nos.environ['OPENAI_API_KEY'] = OPENAI_API_KEY.strip()\nos.environ['OPENAI_BASE_URL'] = OPENAI_API_BASE.strip().rstrip('/')\nOPENAI_API_KEY = os.environ['OPENAI_API_KEY']\nOPENAI_API_BASE = os.environ['OPENAI_BASE_URL']\nAUTH_HEADERS = {'Authorization': f'Bearer {OPENAI_API_KEY}'}\n"

        # Add default_headers to every ChatOpenAI construction that already uses the key.
        src = re.sub(
            r"ChatOpenAI\(([^\n]*?)api_key=OPENAI_API_KEY,base_url=OPENAI_API_BASE,max_retries=2\)",
            r"ChatOpenAI(\1api_key=OPENAI_API_KEY,base_url=OPENAI_API_BASE,max_retries=3,default_headers=AUTH_HEADERS)",
            src,
        )
        src = re.sub(
            r"ChatOpenAI\((.*?)\n\)",
            lambda m: m.group(0) if "api_key=OPENAI_API_KEY" not in m.group(0) or "default_headers=" in m.group(0)
            else m.group(0).replace("\n)", ",\n    default_headers=AUTH_HEADERS,\n)"),
            src,
            flags=re.S,
        )

        # Use the gateway-supported model for both generation and evaluation to avoid model-specific auth routing.
        src = src.replace("model='gpt-4o'", "model='gpt-4o-mini'")
        src = src.replace('model="gpt-4o"', 'model="gpt-4o-mini"')
        cell["source"] = [line + "\n" for line in src.splitlines()]

        auth_check = code_cell(
            '''print("Testing Great Learning API authentication...")
for label, client in [("generation", llm), ("evaluation", judge)]:
    response = client.invoke(f"Reply exactly: {label} connection successful")
    print(f"{label} API test:", response.content.strip())''',
            "api-auth-check",
        )
        idx = nb["cells"].index(cell)
        nb["cells"].insert(idx + 1, auth_check)
        break

# Make the generated notebook clean for a fresh Colab run.
for cell in nb["cells"]:
    if cell.get("cell_type") == "code":
        cell["execution_count"] = None
        cell["outputs"] = []

nb.setdefault("metadata", {}).setdefault("colab", {})
nb["metadata"]["colab"]["name"] = TARGET.name
nb["metadata"]["colab"]["provenance"] = []

with TARGET.open("w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

# Basic safety validation.
with TARGET.open("r", encoding="utf-8") as f:
    check = json.load(f)
text = "\n".join("".join(c.get("source", [])) for c in check["cells"])
for required in [
    "week-12-execution-results",
    "OPENAI_API_KEY",
    "OPENAI_API_BASE",
    "AUTH_HEADERS",
    "default_headers=AUTH_HEADERS",
    "delivery_logs.csv",
    "Running",
]:
    if required not in text:
        raise RuntimeError(f"Generated notebook validation failed: {required} not found")

print(f"Generated {TARGET} with {len(check['cells'])} cells")
