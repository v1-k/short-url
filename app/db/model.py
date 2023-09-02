from sqlalchemy import Column, Integer, String, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .session import Base

class Alias(Base):
    __tablename__ = "alias"

    id = Column(Integer, primary_key=True, nullable=False)
    short_url = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
