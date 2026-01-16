from fastapi import APIRouter, HTTPException, Query
from bson import ObjectId
from datetime import datetime
import re

from database import estudiantes_collection
from schemas.estudiante import EstudianteCreate, EstudianteUpdate

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])




def validate_object_id(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido (ObjectId)")
    return ObjectId(id)


def serialize_estudiante(doc):
    return {
        "id": str(doc["_id"]),
        "nombre": doc["nombre"],
        "apellido": doc["apellido"],
        "aprobado": doc["aprobado"],
        "nota": doc["nota"],
        "fecha": doc["fecha"]
    }



@router.get("/", status_code=200)
def listar_estudiantes():
    docs = list(estudiantes_collection.find())
    return [serialize_estudiante(d) for d in docs]



@router.post("/", status_code=201)
def crear_estudiante(payload: EstudianteCreate):
    data = payload.dict()
    data["fecha"] = datetime.utcnow()
    result = estudiantes_collection.insert_one(data)
    doc = estudiantes_collection.find_one({"_id": result.inserted_id})
    return serialize_estudiante(doc)



@router.get("/buscar", status_code=200)
def buscar_por_nombre_apellido(
    nombre: str = Query(..., min_length=1),
    apellido: str = Query(..., min_length=1),
):
    nombre_re = re.compile(re.escape(nombre), re.IGNORECASE)
    apellido_re = re.compile(re.escape(apellido), re.IGNORECASE)

    docs = list(
        estudiantes_collection.find({
            "nombre": {"$regex": nombre_re},
            "apellido": {"$regex": apellido_re}
        })
    )

    return [serialize_estudiante(d) for d in docs]



@router.get("/aprobados", status_code=200)
def filtrar_aprobados():
    docs = list(estudiantes_collection.find({"aprobado": True}))
    return [serialize_estudiante(d) for d in docs]



@router.get("/{id}", status_code=200)
def obtener_estudiante(id: str):
    oid = validate_object_id(id)
    doc = estudiantes_collection.find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return serialize_estudiante(doc)



@router.put("/{id}", status_code=200)
def actualizar_estudiante(id: str, payload: EstudianteUpdate):
    oid = validate_object_id(id)

    result = estudiantes_collection.update_one(
        {"_id": oid},
        {"$set": payload.dict(exclude_unset=True)}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    doc = estudiantes_collection.find_one({"_id": oid})
    return serialize_estudiante(doc)



@router.delete("/{id}", status_code=200)
def eliminar_estudiante(id: str):
    oid = validate_object_id(id)
    result = estudiantes_collection.delete_one({"_id": oid})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    return {"message": "Estudiante eliminado correctamente"}
