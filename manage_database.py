from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


# A class that maps to a table, ingerits from Base
Base = declarative_base()

# Our class will be mapped to a table with name website
# Each feald is a Column with the given type and constraints


class Website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    relece_date = Column(Date)
    ssl = Column(Boolean)
    html_version = Column(Integer)


class Page(Base):
    __tablename__ = "page"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    website = Column(Integer, ForeignKey("website.id"))
    student = relationship("Website", backref="grades")

