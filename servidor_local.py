import time
import subprocess
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

os.system('color')

def find_kryptex():
    paths = [
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "kryptex", "Kryptex.exe"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "kryptex", "Kryptex.exe"),
        r"C:\Program Files\Kryptex\Kryptex.exe",
        r"C:\Program Files (x86)\Kryptex\Kryptex.exe"
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    # Fallback caso ele mude o diretório (pode ser editado pelo usuário)
    return r"C:\Program Files\Kryptex\Kryptex.exe"

KRYPTEX_EXE_PATH = find_kryptex()

# Variável de controle (Cooldown)
ultimo_restart = 0
TEMPO_DE_ESPERA = 600  # 10 minutos de carência

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global ultimo_restart
        
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(b"OK")
        
        if self.path == '/restart':
            agora = time.time()
            if (agora - ultimo_restart) < TEMPO_DE_ESPERA:
                tempo_restante = int(TEMPO_DE_ESPERA - (agora - ultimo_restart))
                print(f"[{time.strftime('%H:%M:%S')}] \033[93mALERTA IGNORADO: O Kryptex foi reiniciado ha pouco tempo. Dando tempo para ele iniciar... ({tempo_restante}s restantes)\033[0m")
                return

            print(f"\n[{time.strftime('%H:%M:%S')}] \033[91mSTATUS ATUAL: OFFLINE! Triangulo de erro detectado.\033[0m")
            print(f"[{time.strftime('%H:%M:%S')}] Fechando TODO O ECOSSISTEMA Kryptex silenciosamente...")
            
            ultimo_restart = agora
            
            # Limpeza extrema silenciosa
            ps_cmd = "Get-WmiObject Win32_Process | Where-Object { $_.Name -match 'kryptex' -or $_.ExecutablePath -match 'kryptex' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
            subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True)

            mineradores = ["trexminer.exe", "xmrig.exe", "phoenixminer.exe", "gminer.exe", "nbminer.exe", "srbminer-multi.exe", "srbminer.exe"]
            for miner in mineradores:
                subprocess.run(["taskkill", "/F", "/T", "/IM", miner], capture_output=True)
                
            print(f"[{time.strftime('%H:%M:%S')}] Processos limpos! Aguardando 5 segundos...")
            time.sleep(5)
            
            if os.path.exists(KRYPTEX_EXE_PATH):
                # BLINDAGEM TOTAL contra as mensagens feias de log do Kryptex:
                # Agora redirecionamos o lixo (stderr e stdout) para o "buraco negro" (DEVNULL)
                DETACHED_PROCESS = 0x00000008
                subprocess.Popen(
                    [KRYPTEX_EXE_PATH], 
                    creationflags=DETACHED_PROCESS,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    stdin=subprocess.DEVNULL
                )
                print(f"[{time.strftime('%H:%M:%S')}] \033[92mKryptex reaberto com sucesso e totalmente blindado!\033[0m\n")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] ERRO: Nao achou o Kryptex no caminho {KRYPTEX_EXE_PATH}\n")

        elif self.path == '/online':
            print(f"[{time.strftime('%H:%M:%S')}] \033[92mSTATUS ATUAL: ONLINE. Tudo funcionando perfeitamente.\033[0m")

    def log_message(self, format, *args):
        pass

def run_server():
    server_address = ('127.0.0.1', 15000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("===============================================================")
    print("       MOTOR LOCAL DO KRYPTEX (RODANDO NA PORTA 15000)       ")
    print("===============================================================\n")
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        run_server()
    except KeyboardInterrupt:
        # Tratamento para quando você acidentalmente apertar Ctrl+C na tela
        print("\n\n[AVISO] Voce pressionou as teclas Ctrl+C e cancelou o servidor local!")
        print("Feche esta tela e abra o iniciar_servidor.bat de novo.")
        time.sleep(5)
