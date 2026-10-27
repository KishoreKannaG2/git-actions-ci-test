# Runbook: Cloud Deployment & Reliability Lab

## Purpose
This runbook describes how to check the API, inspect logs, investigate a failed health check, and recover the local container.

## Start the service
```bash
docker build -t cloud-reliability-lab .
docker run --name reliability-lab -p 8000:8000 cloud-reliability-lab
```

## Verify service health
```bash
curl -i http://localhost:8000/health
curl -i http://localhost:8000/ready
```
Expected: HTTP 200 and a JSON response.

## Inspect logs
```bash
docker logs --tail 100 reliability-lab
docker logs -f reliability-lab
```

## Simulate an application error
In a second terminal:
```bash
curl -i http://localhost:8000/demo/failure
```
Expected: HTTP 500. This endpoint is intentionally included for local learning only. Do not expose it in a public production deployment.

Then inspect logs:
```bash
docker logs --tail 100 reliability-lab
```
Look for the `Intentional demo failure triggered` message. Note that an HTTP 500 response from this route does not mean the whole process is unhealthy; `/health` should still return HTTP 200.

## Check container status and health
```bash
docker ps
docker inspect --format='{{json .State.Health}}' reliability-lab
```

## Recovery
For this demo, stop and remove the container, then start it again:
```bash
docker stop reliability-lab
docker rm reliability-lab
docker run --name reliability-lab -p 8000:8000 cloud-reliability-lab
```
In a real incident, first assess impact, preserve relevant logs, follow the approved incident/rollback procedure, and escalate when required. Do not restart production services without authorization.

## Stop the lab
```bash
docker stop reliability-lab
docker rm reliability-lab
```

## Incident note template
- Date/time:
- Observed symptom:
- Impact:
- Evidence checked (health endpoint, logs, container status):
- Root cause (confirmed or still unknown):
- Action taken:
- Verification after recovery:
- Follow-up prevention:
