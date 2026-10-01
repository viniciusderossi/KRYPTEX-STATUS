@echo off
:: Pede permissão de Administrador automaticamente (necessário para matar os serviços teimosos do Kryptex)
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :run
) else (
    echo Solicitando privilegios de Administrador...
    powershell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    exit /B
)

:run
cd /d "%~dp0"
echo Iniciando o Servidor Local do Kryptex com Privilegios Maximos...
python servidor_local.py
pause
