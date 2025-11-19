from fastapi import FastAPI
# from app.routers import auth, exams

app = FastAPI(title="FAS ExamVault Backend")

# Include routers
# app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# app.include_router(exams.router, prefix="/exams", tags=["Exams"])

@app.get("/")
def root():
    return {"msg": "FAS ExamVault Backend is running"}
