from fastapi import FastAPI
from routers.estudiantes import router as estudiantes_router

app = FastAPI(title="Examen - FastAPI + MongoDB (Estudiantes)")

app.include_router(estudiantes_router)

@app.get("/")
def root():
    return {"message": "API estudiantes OK. Ve a /docs"}
