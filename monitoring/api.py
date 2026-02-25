from __future__ import annotations

import subprocess
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from orchestrator.state_store import StateStore

app = FastAPI(title="Smart Retail Analytics v2 - Monitoring API")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
STORE = StateStore(PROJECT_ROOT / "orchestrator" / "state" / "pipeline_runs.db")


class TriggerResponse(BaseModel):
    message: str


@app.get("/health")
def health():
    # Basic checks: state DB + docker
    db_ok = (PROJECT_ROOT / "orchestrator" / "state" / "pipeline_runs.db").exists()
    try:
        subprocess.run(["docker", "ps"], check=True, capture_output=True, text=True)
        docker_ok = True
    except Exception:
        docker_ok = False

    return {"ok": True, "db_ok": db_ok, "docker_ok": docker_ok}


@app.get("/runs")
def runs(limit: int = 50):
    return {"runs": STORE.list_runs(limit=limit)}


@app.get("/last-run")
def last_run():
    r = STORE.last_run()
    if not r:
        return {"last_run": None}
    return {"last_run": r}


@app.post("/run-pipeline", response_model=TriggerResponse)
def run_pipeline():
    """
    Triggers pipeline run in background using subprocess.
    """
    engine_path = PROJECT_ROOT / "orchestrator" / "pipeline_engine.py"
    python_path = PROJECT_ROOT / ".venv" / "bin" / "python"

    if not engine_path.exists():
        raise HTTPException(status_code=500, detail="pipeline_engine.py not found")

    if not python_path.exists():
        # fallback
        python_path = Path("python3")

    subprocess.Popen(
        [str(python_path), str(engine_path)],
        cwd=str(PROJECT_ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return TriggerResponse(message="Pipeline started in background. Check /last-run and logs/ folder.")