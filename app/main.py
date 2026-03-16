import uuid
from contextlib import asynccontextmanager

import fastapi
import structlog

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.JSONRenderer,
    ]
)
logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")


app = fastapi.FastAPI(lifespan=lifespan)


# 3. Middleware (Промежуточное ПО). Выполняется для КАЖДОГО запроса.
@app.middleware("http")
async def add_request_id_logging(request: fastapi.Request, call_next):
    # генерируем уникальный id
    req_id = str(uuid.uuid4())

    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(request_id=req_id)

    logger.info("request_started", path=request.url.path, method=request.method)
    # Передаем запрос дальше (в роутер)
    response = await call_next(request)
    # Заставляем FastAPI вернуть этот же ID клиенту в заголовках (хорошая практика)
    response.headers["X-Request-Id"] = req_id
    # Засекаем, что запрос завершен
    logger.info("request_finished", status=response.status_code)
    return response


@app.get("/dashboard")
def dashboard():
    logger.info("Dashboard called")
    return {"status": "ok"}
