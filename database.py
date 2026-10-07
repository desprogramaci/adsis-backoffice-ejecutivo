import os
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://adsis_admin:secure_adsis_password@db:5432/adsis_central_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ActividadAdsis(Base):
    __tablename__ = "actividad_adsis"
    id = Column(Integer, primary_key=True, index=True)
    provincia_sede = Column(String, index=True)
    programa_social = Column(String, index=True)
    personas_acompanadas = Column(Integer)
    fondos_publicos_eur = Column(Float)
    estado_expediente = Column(String)
    fecha = Column(Date)

class LogGobernanza(Base):
    __tablename__ = "logs_gobernanza"
    id = Column(Integer, primary_key=True, index=True)
    mensaje = Column(String)
    timestamp = Column(DateTime, default=datetime.now)

def init_db():
    Base.metadata.create_all(bind=engine)