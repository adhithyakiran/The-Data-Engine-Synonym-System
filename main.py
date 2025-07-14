from fastapi import FastAPI, Depends, Header, HTTPException
from sqlmodel import select, Session
from db import get_session
from models import Synonym, SynonymOut
from cache import cache
from fastapi.responses import JSONResponse
from config import USE_REDIS_CACHE
from dotenv import load_dotenv
import os
import logging

#  Load environment variables and define API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

#  Enable logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Data Engine Synonym System")

#  Auth dependency
def verify_api_key(x_api_key: str = Header(..., alias="X-API-KEY")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

#  Synonyms endpoint
@app.get("/synonyms", response_model=list[SynonymOut], dependencies=[Depends(verify_api_key)])
def get_synonyms(session: Session = Depends(get_session)):
    try:
        cached_data = cache.get()
        if cached_data:
            logging.info("Returned synonyms from cache")
            return cached_data

        logging.info("Cache miss — querying database")
        records = session.exec(select(Synonym)).all()
        output = [
            SynonymOut(
                word=rec.word,
                synonyms=[s.strip() for s in rec.synonyms.split(",")],
                source="database"
            )
            for rec in records
        ]
        for o in output:
            o.source = "cache"
        cache.set(output)
        return output
    except Exception as e:
        logging.exception("Failed to get synonyms")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Cache strategy status
@app.get("/cache-status", dependencies=[Depends(verify_api_key)])
def get_cache_strategy():
    return JSONResponse(content={
        "cache_backend": "redis" if USE_REDIS_CACHE else "in_memory"
    })
