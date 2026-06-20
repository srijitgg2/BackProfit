@echo off
setlocal
set "ROOT=%~dp0"
set "PORT=8020"
echo Starting BackProfit on http://127.0.0.1:%PORT% ...
cd /d "%ROOT%"
python -m uvicorn main:app --host 127.0.0.1 --port %PORT% --reload
endlocal
