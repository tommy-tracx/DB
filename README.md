# AutoShop Diagnostic Service

This project provides a minimal prototype for an AI-powered vehicle
inspection and diagnostic service. Due to the limited runtime
environment, computer vision and real-time diagnostics are implemented
as simple placeholders.

## Features
- HTTP API with two endpoints:
  - `POST /inspect` – accept image data and return a stub analysis.
  - `POST /diagnostics` – interpret OBD-II fault codes using a small
    local database.
- Modular Python package with configuration utilities.
- Basic unit tests using the standard library `unittest` module.

## Quick Start
Run the development server:

```bash
python -m autoshop.main
```

Send requests using `curl` or any HTTP client. Example diagnostic
request:

```bash
curl -X POST http://localhost:8080/diagnostics \
     -H 'Content-Type: application/json' \
     -d '{"codes": ["P0001", "P0123"]}'
```

Run the test suite:

```bash
python -m unittest discover tests
```