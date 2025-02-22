@echo off
echo Setting up Auto Battle script...

set "SCRIPT_DIR=%~dp0"
set "SCRIPT_PATH=%SCRIPT_DIR%main.exe"
set "GAME_NAME=StarRail.exe"
set "TASK_NAME=HSRAutoContinueBattle"

schtasks /delete /tn "%TASK_NAME%" /f >nul 2>&1
schtasks /delete /tn "%TASK_NAME%_Stop" /f >nul 2>&1

schtasks /create /tn "%TASK_NAME%" /tr "\"%SCRIPT_PATH%\"" /sc onlogon /ru "SYSTEM" /rl HIGHEST /f

schtasks /create /tn "%TASK_NAME%_Stop" /tr "cmd.exe /c taskkill /IM autobattle.exe /F" /sc onidle /i 5 /f

echo Setup complete! Auto battle will now start with %GAME_NAME% and stop when it's closed.
pause
