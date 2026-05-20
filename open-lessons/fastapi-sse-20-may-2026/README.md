# FastAPI SSE + HTMX Demo

Small demo app: orders advance through statuses (`pending` → `processing` → `shipped` → `delivered`) and the UI updates live via **Server-Sent Events** and **HTMX** (`hx-ext="sse"`).

## Stack

- [FastAPI](https://fastapi.tiangolo.com/) with native SSE (`EventSourceResponse`)
- [HTMX](https://htmx.org/) + SSE extension
- Jinja2 templates, in-memory order storage

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended)

## Run

```bash
uv sync
uv run uvicorn app:app --reload
```

Open [http://127.0.0.1:8000/orders](http://127.0.0.1:8000/orders), create an order, and open its detail page to watch status updates stream in.

API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### HTTPS + HTTP/2 (recommended for SSE)

On **HTTP/1.1**, browsers cap concurrent connections per host (often six). A long-lived SSE stream uses one slot; with the list page, detail page, assets, and API calls, extra requests (including new SSE connections) can queue and look “stuck.” **HTTPS with HTTP/2** multiplexes many streams on one connection, so SSE stays responsive during local dev.

Install [mkcert](https://github.com/FiloSottile/mkcert) once (`brew install mkcert` on macOS), then trust its local CA:

```bash
mkcert -install
```

Generate certs (creates `certs/`; keep these local, do not commit):

```bash
mkdir -p certs
mkcert \
  -cert-file certs/localhost.pem \
  -key-file certs/localhost-key.pem \
  localhost 127.0.0.1 ::1
```

Run with [Hypercorn](https://hypercorn.readthedocs.io/) (TLS enables HTTP/2):

```bash
uv run hypercorn app:app \
  --bind 127.0.0.1:8443 \
  --certfile certs/localhost.pem \
  --keyfile certs/localhost-key.pem
```

Open [https://127.0.0.1:8443/orders](https://127.0.0.1:8443/orders) (accept the mkcert-issued certificate if prompted). API docs: [https://127.0.0.1:8443/docs](https://127.0.0.1:8443/docs)

## Endpoints

| Path | Description |
|------|-------------|
| `GET /orders` | Order list (HTML or JSON) |
| `POST /orders` | Create order |
| `GET /orders/{id}` | Order detail with SSE-driven status block |
| `GET /orders/{id}/events` | SSE stream for that order |

Send `Accept: application/json` for JSON responses; omit it or use `text/html` for HTML pages.

## Notes

- Status progression runs in the background after create; SSE pushes rendered HTML fragments to connected clients.
- Graceful shutdown closes SSE connections on `SIGINT` / `SIGTERM` (see `misc/shutdown.py`, `static/js/sse-graceful-close.js`).
