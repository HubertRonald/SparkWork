#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if docker compose version >/dev/null 2>&1; then
  COMPOSE=(docker compose)
elif command -v docker-compose >/dev/null 2>&1; then
  COMPOSE=(docker-compose)
else
  echo "ERROR: Docker Compose is required (docker compose or docker-compose)." >&2
  exit 2
fi

"${COMPOSE[@]}" up --build -d spark
"${COMPOSE[@]}" ps

echo
echo "Jupyter authentication uses the server-generated token; no password is stored in the repository."
echo "Use the URL/token printed below."
"${COMPOSE[@]}" logs --tail=80 spark
