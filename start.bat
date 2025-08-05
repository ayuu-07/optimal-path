@echo off
echo Starting Arch-AI Project...
echo.

echo Starting Backend Server...
cd backend
start "Backend" cmd /k "python -c \"from fastapi import FastAPI; from pydantic import BaseModel; from fastapi.middleware.cors import CORSMiddleware; import uvicorn; app = FastAPI(); app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*']); exec(open('main.py').read()); uvicorn.run(app, host='127.0.0.1', port=8000)\""

cd ..
echo.
echo Backend started on http://127.0.0.1:8000
echo.

echo Starting Frontend Server...
cd frontend
start "Frontend" cmd /k "npm run dev"

cd ..
echo.
echo Frontend will start on http://localhost:5173
echo.
echo Demo available at: demo.html
echo.
pause
