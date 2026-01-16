from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime


class EstudianteBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    apellido: str = Field(..., min_length=1)
    aprobado: bool
    nota: float


class EstudianteCreate(EstudianteBase):
    
    fecha: Optional[date] = None


class EstudianteUpdate(BaseModel):
 
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    aprobado: Optional[bool] = None
    nota: Optional[float] = None
    fecha: Optional[date] = None


class EstudianteOut(EstudianteBase):
    id: str
    fecha: datetime
