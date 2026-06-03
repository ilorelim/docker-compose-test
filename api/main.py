import os

import redis
from fastapi import FastAPI


REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

app = FastAPI()


def get_redis_client():
    return redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        decode_responses=True,
    )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def index():
    client = get_redis_client()
    visits = client.incr("visits")

    return {
        "message": "Hello from FastAPI behind Nginx",
        "visits": visits,
    }
