import subprocess
import uuid
from pathlib import Path
from datetime import datetime
import sys

from orchestrator.state_store import StateStore


PROJECT_ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = PROJECT_ROOT / ".venv" / "bin" / "python"


class PipelineEngine:
    def __init__(self):
        self.project_root = PROJECT_ROOT
        self.logs_dir = self.project_root / "logs"
        self.logs_dir.mkdir(exist_ok=True)

        self.state_dir = self.project_root / "orchestrator" / "state"
        self.state_dir.mkdir(parents=True, exist_ok=True)

        self.state_store = StateStore(self.state_dir)

    def run_step(self, name, command, cwd=None, log_file=None):
        print(f"\n=== STEP: {name} ===")
        print(f"CMD: {' '.join(command)}")
        print(f"CWD: {cwd}")

        with open(log_file, "a") as log:
            process = subprocess.Popen(
                command,
                cwd=cwd,
                stdout=log,
                stderr=log,
                text=True
            )
            process.wait()

            if process.returncode != 0:
                raise Exception(f"Step failed: {name}")

    def run(self):
        run_id = str(uuid.uuid4())
        log_file = self.logs_dir / f"pipeline_run_{run_id}.log"

        print("=" * 60)
        print(" SMART RETAIL ANALYTICS v2 - PIPELINE RUN")
        print(" RUN_ID:", run_id)
        print("=" * 60)

        self.state_store.create_run(run_id, str(log_file))

        try:
            # Step 1
            self.run_step(
                "Generate Raw Data",
                [str(VENV_PYTHON), str(self.project_root / "etl/generate_raw_data.py")],
                cwd=self.project_root,
                log_file=log_file
            )

            # Step 2
            self.run_step(
                "Clean Transform",
                [str(VENV_PYTHON), str(self.project_root / "etl/clean_transform.py")],
                cwd=self.project_root,
                log_file=log_file
            )

            # Step 3 - Schema
            self.run_step(
                "Create Warehouse Schema",
                [
                    "docker", "exec", "-i", "sra_postgres",
                    "psql", "-U", "postgres",
                    "-d", "smart_retail_dw",
                    "-f", "sql/warehouse_star_schema.sql"
                ],
                cwd=self.project_root,
                log_file=log_file
            )

            # Step 4 - Load
            self.run_step(
                "Load to Postgres",
                [str(VENV_PYTHON), str(self.project_root / "etl/load_to_postgres.py")],
                cwd=self.project_root,
                log_file=log_file
            )

            self.state_store.update_run(run_id, "SUCCESS")

            print("\nPIPELINE COMPLETED SUCCESSFULLY")

        except Exception as e:
            self.state_store.update_run(run_id, "FAILED")
            print("\nPIPELINE FAILED:", e)
            print("Check log:", log_file)


def main():
    engine = PipelineEngine()
    engine.run()


if __name__ == "__main__":
    main()