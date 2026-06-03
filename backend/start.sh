#!/bin/bash
cd /home/z/my-project/backend
while true; do
    echo "Starting ContaEC backend..." >> /tmp/contaec-backend.log
    python3 -m uvicorn main:app --host 0.0.0.0 --port 8001 >> /tmp/contaec-backend.log 2>&1
    EXIT_CODE=$?
    echo "Backend exited with code $EXIT_CODE, restarting in 3s..." >> /tmp/contaec-backend.log
    sleep 3
done
