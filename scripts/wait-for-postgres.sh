#!/bin/bash
# Wait for PostgreSQL to be ready

HOST=$1
PORT=${2:-5432}
TIMEOUT=${3:-30}

echo "Waiting for PostgreSQL at $HOST:$PORT (timeout: ${TIMEOUT}s)..."

START_TIME=$(date +%s)

while [ $(( $(date +%s) - START_TIME )) -lt $TIMEOUT ]; do
    if pg_isready -h "$HOST" -p "$PORT" > /dev/null 2>&1; then
        echo "PostgreSQL is ready!"
        exit 0
    fi
    echo "PostgreSQL is unavailable - sleeping..."
    sleep 1
done

echo "PostgreSQL is still unavailable after ${TIMEOUT}s timeout!"
exit 1
