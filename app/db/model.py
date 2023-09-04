from sqlalchemy import Column, Integer, String, text, BigInteger
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .session import Base

class URLMap(Base):
    __tablename__ = "url_map"

    id = Column(Integer, primary_key=True, nullable=False)
    short_url = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class URLMapGenerated(Base):
    __tablename__ = "url_map_generated"
    id = Column(Integer, primary_key=True, nullable=False)
    total = Column(BigInteger, nullable=False, default=0)
    