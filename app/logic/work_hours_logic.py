from datetime import datetime

def calculate_work_hours(hora_checada: datetime, fecha_checada: datetime) -> float:
    try:
        worked_hours = (fecha_checada - hora_checada).total_seconds() / 3600 
        return round(worked_hours, 2)
    except Exception as e:
        raise ValueError(f"Error al calcular las horas trabajadas: {str(e)}")

def save_work_hours(emplid: int, fecha_checada: datetime, worked_hours: float):
    from database import get_db_session
    from models import WorkHoursRecord

    session = get_db_session()

    new_record = WorkHoursRecord(
        emplid=emplid,
        fecha_checada=fecha_checada,
        worked_hours=worked_hours
    )

    session.add(new_record)
    session.commit()

def get_all_work_hours():
    from database import get_db_session
    from models import WorkHoursRecord

    session = get_db_session()
    return session.query(WorkHoursRecord).all()
