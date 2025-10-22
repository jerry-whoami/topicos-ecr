# FastAPI + Docker

Minimal guide to build and test the FastAPI service in this repo.

## Project layout

```
.
├── Dockerfile
├── main.py            # FastAPI app (GET /hello-app)
├── requirements.txt   # Python deps (fastapi, uvicorn, etc.)
└── README.md
```

`main.py` (for reference) exposes:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-app")
def hello_app():
    return {"message": "Hello, world!"}
```

---

## Prerequisites

* Docker 20+ installed and running
* Optional: Python 3.10+ if you want to run it locally without Docker

---

## 1) Build the Docker image

From the project root:

```bash
docker build -t fastapi-hello:latest .
```

---

## 2) Run the container

```bash
# Map container port 8000 to host port 8000
docker run --rm -p 8000:8000 --name fastapi-hellofastapi-hello:latest
```

* Service base URL: `http://localhost:8000`
* Interactive docs: `http://localhost:8000/docs` (Swagger UI)
* Alternative docs: `http://localhost:8000/redoc`

---

## 3) Test the API

### Curl

```bash
curl -s http://localhost:8000/hello-app | jq .
# Expected: { "message": "Hello, world!" }
```

Without `jq`:

```bash
curl http://localhost:8000/hello-app
```

### Python (requests)

```python
import requests
print(requests.get("http://localhost:8000/hello-app").json())
```

---

## 4) Stop and clean up

```bash
docker stop fastapi-hello  # if running detached
docker rmi fastapi-hello:latest  # remove image (optional)
```

---

## Local run (no Docker, optional)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Open `http://localhost:8000/docs`.

---

## Troubleshooting

* **Port already in use**
  Change the host port: `-p 8080:8000` then hit `http://localhost:8080`.

* **Cannot reach /docs**
  Ensure the container is running and logs show `Uvicorn running on http://0.0.0.0:8000`.

* **Changes not reflected**
  Rebuild the image: `docker build -t fastapi-hello:latest .` then re-run the container.

That’s it. Build, run, hit `/hello-app`, done.
