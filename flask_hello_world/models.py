import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, DECIMAL
#from sqlalchemy.type import Decimal
from flask.ext.login import UserMixin

from .database import Base, engine

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Mytime(Base):
    __tablename__ = "times"

    id = Column(Integer, primary_key=True)
    name = Column(Text)

Base.metadata.create_all(engine)