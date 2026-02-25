#!/usr/bin/env bash
set -e
TS=$(date +"%Y%m%d_%H%M%S")
mkdir -p backups
pg_dump -h localhost -p 5432 -U postgres smart_retail_dw > "backups/smart_retail_dw_${TS}.sql"
echo "? Backup created: backups/smart_retail_dw_${TS}.sql"
