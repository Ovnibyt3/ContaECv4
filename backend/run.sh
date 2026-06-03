#!/bin/bash
cd /home/z/my-project/backend
exec python3 -m uvicorn main:app --host 0.0.0.0 --port 8001
