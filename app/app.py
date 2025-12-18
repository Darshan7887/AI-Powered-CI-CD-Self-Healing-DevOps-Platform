from flask import Flask, jsonify
import os
import time
import threading
import logging

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

REQUIRED_CONFIG = os.getenv("REQUIRED_CONFIG")

if not REQUIRED_CONFIG:
    logger.error("REQUIRED_CONFIG is missing. App will be unhealthy.")

@app.route("/")
def index():
    return jsonify({"status": "running"})

@app.route("/health")
def health():
    if not REQUIRED_CONFIG:
        return jsonify({"status": "unhealthy"}), 500
    return jsonify({"status": "healthy"})

@app.route("/crash")
def crash():
    logger.critical("Intentional crash triggered")
    os._exit(1)

def cpu_stress(seconds):
    end = time.time() + seconds
    while time.time() < end:
        pass

@app.route("/load")
def load():
    seconds = int(os.getenv("CPU_LOAD_SECONDS", "20"))
    logger.warning(f"Starting CPU load for {seconds} seconds")
    threading.Thread(target=cpu_stress, args=(seconds,)).start()
    return jsonify({"status": "cpu stress started"})

if __name__ == "__main__":
    mode = os.getenv("APP_MODE", "normal")
    logger.info(f"Starting app in mode: {mode}")

    if mode == "crash":
        logger.critical("Crash mode enabled. Exiting.")
        os._exit(1)

    app.run(host="0.0.0.0", port=5000)

