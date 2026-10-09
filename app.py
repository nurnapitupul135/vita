from fastapi import FastAPI
import subprocess
import threading

app = FastAPI()
status = {"running": False, "logs": "idle"}

def run_task():
    global status
    status["running"] = True
    try:
        result = subprocess.run(["python", "task.py"], capture_output=True, text=True)
        status["logs"] = result.stdout + "\n" + result.stderr
        print(status["logs"]) # biar keliatan di log Novita
    except Exception as e:
        status["logs"] = str(e)
    finally:
        status["running"] = False

@app.get("/")
def home():
    return {"status": "ok", "running": status["running"], "logs": status["logs"]}

@app.post("/run")
def trigger():
    if not status["running"]:
        threading.Thread(target=run_task).start()
        return {"message": "task.py started - check / for logs"}
    return {"message": "already running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
