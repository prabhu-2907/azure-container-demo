from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/hit")
def hit():
    count = r.incr("hits")
    return jsonify(message="Hello from API", hits=count)

@app.get("/")
def root():
    return jsonify(
        service="api",
        endpoints=["/health", "/hit"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
