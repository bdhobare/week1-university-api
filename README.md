# University API

A FastAPI service that serves in-memory university student data. It exposes a root endpoint describing the API, a list of all students, and lookup of a single student by ID (returns `404` if the ID is unknown).

## Requirements

- Python 3.11+
- Packages listed in `requirements.txt` (FastAPI and Uvicorn)

## Installation

```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

The server starts on `http://127.0.0.1:8000`.

## URLs to test

| Method | URL | Description |
|--------|-----|-------------|
| GET | http://127.0.0.1:8000/ | API name, version, and list of endpoints |
| GET | http://127.0.0.1:8000/students | All students |
| GET | http://127.0.0.1:8000/students/s1 | A single student (`s1`, `s2`, `s3` exist) |
| GET | http://127.0.0.1:8000/students/unknown | Returns `404 Student not found` |
| GET | http://127.0.0.1:8000/docs | Interactive Swagger UI |

The `/docs` page is not defined in this project. FastAPI generates it automatically when `FastAPI()` is created in `main.py`, building the page from every registered route (including those in `routers/students.py`). See the FastAPI docs: https://fastapi.tiangolo.com/features/#automatic-docs

Example with `curl`:

```bash
curl http://127.0.0.1:8000/students/s2
```

## Running the tests

The tests in `tests.py` use FastAPI's `TestClient` (which relies on `httpx`) and cover all three endpoints plus the 404 case. `pytest` is not in `requirements.txt`, so install it into the virtualenv first:

```bash
source .venv/bin/activate
pip install pytest
pytest tests.py
```

Note: `uv run pytest` will fail with `No pyproject.toml found` because this project uses a plain virtualenv and `requirements.txt` rather than a `uv` project file. Use the commands above instead.

## Project structure

```
main.py              # FastAPI app and root endpoint
routers/students.py  # /students routes and sample data
tests.py             # pytest tests using FastAPI's TestClient
requirements.txt     # pinned dependencies
```
