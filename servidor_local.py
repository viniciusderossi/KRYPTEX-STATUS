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
    # Fallback caso ele mude o diret??rio (pode ser editado pelo usu??rio)
    return r"C:\Program Files\Kryptex\Kryptex.exe"

KRYPTEX_EXE_PATH = find_kryptex()

# Vari??vel de controle (Cooldown)
ultimo_restart = 0
TEMPO_DE_ESPERA = 600  # 10 minutos de car??ncia

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
                # Usa \r para nao poluir a tela com inumeros avisos enquanto espera os 10 minutos
                print(f"[{time.strftime('%H:%M:%S')}] \033[93mALERTA IGNORADO: Aguardando o Kryptex (re)iniciar nos bastidores... ({tempo_restante}s restantes)\033[0m   ", end='\r', flush=True)
                return

            print(f"\n[{time.strftime('%H:%M:%S')}] \033[91mSTATUS ATUAL: OFFLINE! Triangulo de erro detectado.\033[0m", flush=True)
            print(f"[{time.strftime('%H:%M:%S')}] Fechando TODO O ECOSSISTEMA Kryptex silenciosamente...", flush=True)
            
            ultimo_restart = agora
            
            # Limpeza extrema silenciosa
            ps_cmd = "Get-WmiObject Win32_Process | Where-Object { $_.Name -match 'kryptex' -or $_.ExecutablePath -match 'kryptex' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
            subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True)

            mineradores = ["trexminer.exe", "xmrig.exe", "phoenixminer.exe", "gminer.exe", "nbminer.exe", "srbminer-multi.exe", "srbminer.exe"]
            for miner in mineradores:
                subprocess.run(["taskkill", "/F", "/T", "/IM", miner], capture_output=True)
                
            print(f"[{time.strftime('%H:%M:%S')}] Processos limpos! Aguardando 5 segundos...", flush=True)
            time.sleep(5)
            
            if os.path.exists(KRYPTEX_EXE_PATH):
                DETACHED_PROCESS = 0x00000008
                CREATE_NEW_PROCESS_GROUP = 0x00000200
                subprocess.Popen(
                    [KRYPTEX_EXE_PATH],
                    creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    stdin=subprocess.DEVNULL
                )
                print(f"[{time.strftime('%H:%M:%S')}] \033[92mKryptex reaberto com sucesso!\033[0m\n", flush=True)
            else:
                print(f"[{time.strftime('%H:%M:%S')}] \033[91mERRO: Nao achou o Kryptex no caminho {KRYPTEX_EXE_PATH}\033[0m\n", flush=True)

        elif self.path == '/online':
            print(f"[{time.strftime('%H:%M:%S')}] \033[92m[✓] Vigiando: PC ONLINE e minerando corretamente...\033[0m   ", end='\r', flush=True)

        elif self.path == '/notfound':
            print(f"[{time.strftime('%H:%M:%S')}] \033[93mSite do Kryptex Offline ou Fora do Ar. Aguardando recarregar a pagina em 2 min...\033[0m", flush=True)

    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        if self.path == '/debug':
            content_len = int(self.headers.get('Content-Length', 0))
            post_body = self.rfile.read(content_len).decode('utf-8')
            with open('debug_html.txt', 'w', encoding='utf-8') as dbg: dbg.write(post_body)
            pass
    def log_message(self, format, *args):
        pass

def run_server():
    server_address = ('127.0.0.1', 15000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("===============================================================")
    print("       MOTOR LOCAL DO KRYPTEX (RODANDO NA PORTA 15000)       ")
    print("===============================================================\n")
    print(f"[{time.strftime('%H:%M:%S')}] \033[92mServidor ATIVO e vigiando a extensao! (Modo Silencioso)\n\033[0m", flush=True)
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        run_server()
    except KeyboardInterrupt:
        # Tratamento para quando voc?? acidentalmente apertar Ctrl+C na tela
        print("\n\n[AVISO] Voce pressionou as teclas Ctrl+C e cancelou o servidor local!")
        print("Feche esta tela e abra o iniciar_servidor.bat de novo.")
        time.sleep(5)
