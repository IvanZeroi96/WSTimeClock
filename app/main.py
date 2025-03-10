# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from business_logic import calculate_work_hours, save_work_hours, get_all_work_hours
from datetime import datetime

app = FastAPI()

class CheckInRequest(BaseModel):
    emplid: int
    fecha_checada: str 
    hora_checada: str 
    tipo_checada: int
    estatus_checada: int

@app.post("/calculate_hours")
async def calculate_hours(request: CheckInRequest):
    try:

        fecha_checada = datetime.strptime(request.fecha_checada, '%d/%m/%Y %H:%M:%S')
        hora_checada = datetime.strptime(request.hora_checada, '%d/%m/%Y %H:%M:%S')

        worked_hours = calculate_work_hours(hora_checada, fecha_checada)

        save_work_hours(request.emplid, fecha_checada, worked_hours)

        return {"message": "Horas trabajadas calculadas y guardadas correctamente", "worked_hours": worked_hours}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la solicitud: {str(e)}")

@app.get("/get_work_hours")
async def get_work_hours():
    try:
        records = get_all_work_hours()
        return {"records": [record.__repr__() for record in records]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los registros: {str(e)}")
