# models.py
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WorkHoursRecord(Base):
    __tablename__ = 'worked_hours_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    emplid = Column(Integer, nullable=False)
    fecha_checada = Column(DateTime, nullable=False)
    worked_hours = Column(Float, nullable=False)

    def __repr__(self):
        return f"<WorkHoursRecord(emplid={self.emplid}, fecha_checada={self.fecha_checada}, worked_hours={self.worked_hours})>"
