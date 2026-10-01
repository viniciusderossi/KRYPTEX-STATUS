@echo off
:: Pede permissao de Administrador automaticamente (necessario para matar os servicos teimosos do Kryptex)
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

:: Verifica se o Python esta instalado
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo =======================================================
    echo [AVISO] Python nao foi encontrado neste computador!
    echo O Servidor Kryptex precisa dele para funcionar.
    echo Nao se preocupe, faremos a instalacao APENAS ESTA VEZ.
    echo Tudo sera feito sozinho de forma automatica!
    echo =======================================================
    echo.
    echo Baixando o instalador oficial do Python... aguarde.
    curl -o python_installer.exe https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe
    
    echo.
    echo Instalando o Python no seu sistema (isso pode demorar cerca de 1 a 2 minutos)...
    :: Instala de forma totalmente invisivel, marcando a opcao crucial de adicionar ao "Path" do Windows
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    
    echo Instalacao concluida! Limpando os arquivos...
    del python_installer.exe
    
    echo.
    echo O Windows precisa atualizar os caminhos. O script vai reiniciar em 5 segundos...
    timeout /t 5 >nul
    start "" "%~dpnx0"
    exit /B
)

echo Iniciando o Servidor Local do Kryptex com Privilegios Maximos...
python servidor_local.py
pause
