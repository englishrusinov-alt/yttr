import fastapi
from contextlib import contextmanager, asynccontextmanager


@asynccontextmanager
async def lifespan(app:fastapi.FastAPI):
    print("Application startup")
    yield
    print("Application shutdown")

app = fastapi.FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return {"status":"ok"}