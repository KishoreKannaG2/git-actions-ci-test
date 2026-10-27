import logging
import os
import sys
from fastapi import FastAPI, HTTPException

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger("reliability-lab")

app = FastAPI(title="Cloud Deployment & Reliability Lab", version="1.0.0")


@app.get("/")
def root():
    logger.info("Root endpoint requested")
    return {"service": "cloud-reliability-lab", "status": "running"}


@app.get("/health")
def health():
    """Liveness check: is the API process responding?"""
    return {"status": "alive"}


@app.get("/ready")
def ready():
    """Readiness check: can this app accept requests? Extend with dependency checks later."""
    return {"status": "ready"}


@app.get("/demo/failure")
def demo_failure():
    """Intentional failure for local learning; do not expose this route in production."""
    logger.error("Intentional demo failure triggered")
    raise HTTPException(status_code=500, detail="Intentional demo failure for reliability testing")
