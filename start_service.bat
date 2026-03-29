@echo off

set BASE_DIR=%~dp0

start "" "%BASE_DIR%frontend\index.html"

call ".venv\Scripts\activate.bat"

uvicorn main:app --reload

call deactivate