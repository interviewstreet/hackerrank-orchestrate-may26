@echo off
REM ============================================================
REM  HackerRank Orchestrate — Support Triage Agent (Windows)
REM ============================================================

REM Load .env if it exists
if exist ".env" (
    for /f "delims== tokens=1,2" %%i in (.env) do (
        if not "%%i"=="" if not "%%i:~0,1%"=="#" (
            set "%%i=%%j"
        )
    )
) else (
    echo [WARNING] .env not found. Copy from .env.example and add your API keys.
    echo Continuing with environment variables...
)

REM Install dependencies
echo [Setup] Installing dependencies...
pip install -q -r requirements.txt

echo.
echo [Run] Processing support_tickets.csv...
echo.
cd code
python main.py --file ../support_tickets/support_tickets.csv --output ../support_tickets/output.csv
cd ..

echo.
echo [Done] Results written to support_tickets/output.csv
echo.
