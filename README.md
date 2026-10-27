# Cloud Deployment & Reliability Lab

A small portfolio project demonstrating a Python API, Docker packaging, automated tests, a GitHub Actions CI pipeline, health checks, logs, failure simulation, and a basic operational runbook.

## Requirements
- Python 3.12+
- Docker Desktop or Docker Engine
- Git
- A GitHub account for CI

## Run locally without Docker
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
uvicorn app:app --reload
```

Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/ready
- http://127.0.0.1:8000/docs

Run tests in another terminal:
```bash
pytest -q
```

## Run with Docker
```bash
docker build -t cloud-reliability-lab .
docker run --name reliability-lab -p 8000:8000 cloud-reliability-lab
```

Then visit `http://localhost:8000/health`.

Check logs:
```bash
docker logs -f reliability-lab
```

Simulate an intentional HTTP 500:
```bash
curl -i http://localhost:8000/demo/failure
```
This endpoint is for local learning only; remove or protect it before any public deployment.

## CI pipeline
The workflow in `.github/workflows/ci.yml` runs on pushes and pull requests. It installs dependencies, runs pytest, and builds the Docker image. It does not deploy to production.

## Reliability exercise
1. Confirm `/health` and `/ready` return HTTP 200.
2. Trigger `/demo/failure` and observe the HTTP 500.
3. Inspect container logs and identify the intentional error message.
4. Verify `/health` still returns HTTP 200.
5. Complete the incident note in `RUNBOOK.md`.

## Next improvements
- Add dependency-aware readiness checks.
- Add a test that fails when an invalid configuration is supplied.
- Add a monitoring dashboard or uptime check.
- Add a staging deployment after selecting a hosting provider.
- Add image scanning and dependency vulnerability checks.

## Important scope note
This is a learning project, not a production-ready service. It intentionally includes a failure-demo endpoint and has no authentication, rate limiting, or real external dependency checks.
# git-actions-ci-test
