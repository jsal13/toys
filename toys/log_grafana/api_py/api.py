from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.on_event("startup")
async def startup():
    """Initialize app."""
    Instrumentator().instrument(app).expose(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
