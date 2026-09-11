from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from contextlib import asynccontextmanager

from app.config import settings
from app.database import init_db, close_db
from app.routes import analyze, chat, corpus, authorities, news, admin, health
from app.scheduler import start_scheduler, stop_scheduler

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting LexPIL AI Server")
    await init_db()
    start_scheduler()
    yield
    logger.info("Shutting down LexPIL AI Server")
    stop_scheduler()
    await close_db()

app = FastAPI(
    title="LexPIL AI",
    description="Private International Law AI Counsel",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(analyze.router, prefix="/api", tags=["analysis"])
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(corpus.router, prefix="/api", tags=["corpus"])
app.include_router(authorities.router, prefix="/api", tags=["authorities"])
app.include_router(news.router, prefix="/api", tags=["news"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Global exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error_type": type(exc).__name__}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.app_port,
        log_level=settings.log_level.lower()
    )
