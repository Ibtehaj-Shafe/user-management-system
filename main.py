from routes import user_routes
from fastapi import FastAPI
from db.database import Engine, Base

app= FastAPI(title="FASTAPI practice",description="IMPLEMENT CRUD using SQLALCHEMY, POSTGRESQL and FASTAPI")

try:
    Base.metadata.create_all(bind=Engine)
except Exception as e:
    print(f"Warning: Could not create tables on startup: {e}")


app.include_router(user_routes.router)
