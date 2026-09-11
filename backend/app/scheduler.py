from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging
from app.config import settings
from app.ingestion.corpus_updater import CorpusUpdater

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()
corpus_updater = CorpusUpdater()

def start_scheduler():
    """Start background scheduler"""
    if not scheduler.running:
        # Schedule corpus update
        scheduler.add_job(
            corpus_updater.update_corpus,
            trigger=CronTrigger(
                hour=settings.corpus_update_hour,
                minute=settings.corpus_update_minute
            ),
            id="corpus_update",
            name="Daily corpus update",
            replace_existing=True
        )
        
        scheduler.start()
        logger.info("Scheduler started")

def stop_scheduler():
    """Stop background scheduler"""
    if scheduler.running:
        scheduler.shutdown()
        logger.info("Scheduler stopped")
