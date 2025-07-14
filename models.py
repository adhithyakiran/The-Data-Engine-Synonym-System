from sqlmodel import SQLModel, Field
from typing import List

class Synonym(SQLModel, table=True):
    id: int = Field(primary_key=True)
    word: str
    synonyms: str  # comma-separated

class SynonymOut(SQLModel):
    word: str
    synonyms: List[str]
    source: str
