import sqlite3
from pathlib import Path
from datetime import datetime
import json


class StateStore:
    def __init__(self, state_dir: Path):
        self.state_dir = Path(state_dir).resolve()
        self.state_dir.mkdir(parents=True, exist_ok=True)

        self.db_path = self.state_dir / "pipeline_state.db"

        self._init_db()

    def _connect(self):
        return sqlite3.connect(str(self.db_path))

    def _init_db(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pipeline_runs (
                    run_id TEXT PRIMARY KEY,
                    start_time TEXT,
                    end_time TEXT,
                    status TEXT,
                    log_file TEXT
                )
            """)
            conn.commit()

    def create_run(self, run_id, log_file):
        with self._connect() as conn:
            conn.execute("""
                INSERT INTO pipeline_runs (run_id, start_time, status, log_file)
                VALUES (?, ?, ?, ?)
            """, (run_id, datetime.utcnow().isoformat(), "RUNNING", log_file))
            conn.commit()

    def update_run(self, run_id, status):
        with self._connect() as conn:
            conn.execute("""
                UPDATE pipeline_runs
                SET status = ?, end_time = ?
                WHERE run_id = ?
            """, (status, datetime.utcnow().isoformat(), run_id))
            conn.commit()