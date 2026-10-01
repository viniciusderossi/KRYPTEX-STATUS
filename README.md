# ⛏️ Kryptex Auto-Restart Monitor

Um sistema inteligente e 100% local (Open-Source) criado para monitorar o status das suas máquinas de mineração no **Kryptex** e reiniciar automaticamente o aplicativo no Windows caso a máquina trave, o minerador pare ou a placa de vídeo desarme.

## 🧠 Como funciona?
O sistema é composto por duas partes que conversam entre si:
1. **Extensão do Google Chrome:** Injetada invisivelmente na página de hardware do seu painel do Kryptex. Ela faz a leitura automática dos seus computadores a cada minuto procurando por **ícones de erro (triângulo vermelho) ou ausência de rentabilidade**.
2. **Servidor Local Python:** Roda em uma tela do CMD no Windows. Ao receber o alerta de falha da extensão, ele usa o sistema `WMI` do Windows com poderes de Administrador para aniquilar qualquer processo travado do Kryptex (`Kryptex.exe`, `KryptexService.exe`, `SRBMiner`, etc.) e reiniciar o programa com a memória limpa.

---

## 🔒 Privacidade e Segurança
* **100% Local:** A extensão não se comunica com a internet. Os alertas são enviados apenas para `http://127.0.0.1:15000` (seu próprio computador).
* **Nenhum Dado Sensível:** O sistema lê apenas os nomes dos computadores e os status na tela. Ele não possui acesso a senhas, carteiras ou cookies do usuário.
* **Sistema de Cooldown:** Possui um temporizador de segurança de 10 minutos após cada reinício para evitar loops infinitos enquanto o Kryptex faz benchmarking.

---

## 🛠️ Instalação e Uso

### Requisitos
* Google Chrome (ou Brave/Edge)
* Python 3 instalado no Windows

### Passo 1: Configurar a Extensão no Chrome
1. Faça o download deste repositório e extraia a pasta no seu PC.
2. Abra o Chrome e digite na barra de endereços: `chrome://extensions/`
3. Ative o **Modo do desenvolvedor** (no canto superior direito).
4. Clique em **Carregar sem compactação** e selecione a pasta `extensao_kryptex`.
5. Fixe a extensão na sua barra, clique nela e defina o computador que deseja monitorar. Você pode digitar o nome manualmente ou **clicar no botão azul (🔄) para a extensão buscar e listar automaticamente todas as suas máquinas disponíveis na página!** Selecione a máquina e clique em Salvar.

### Passo 2: Iniciar o Servidor
1. Na pasta principal, dê um duplo clique no arquivo **`iniciar_servidor.bat`**.
2. O Windows vai pedir permissão de Administrador (necessário para conseguir matar os processos travados do Kryptex). Clique em **Sim**.
3. A tela preta ficará aguardando informações.

### Passo 3: Monitoramento
1. Acesse o painel de hardware do Kryptex no Chrome: `https://www.kryptex.com/pt/hardware/computers`
2. Mantenha essa aba aberta (ela pode ficar em segundo plano).
3. A extensão cuidará de atualizar a página a cada 5 minutos e fazer varreduras a cada 60 segundos!

---

## ❓ FAQ (Perguntas Frequentes)

**O servidor reinicia o Kryptex sempre que não há saldo (R$) na tela?**
R: Não. Para evitar falsos positivos durante o início da mineração, a extensão procura a ausência do saldo atrelada à *presença de uma classe HTML de erro (o triângulo vermelho)*. 

**Por que o arquivo .bat pede privilégios de Administrador?**
R: O Kryptex utiliza serviços de segundo plano (como o `KryptexService.exe`) que operam em nível elevado para modificar drivers de GPU. Um script normal não tem permissão para fechá-los, resultando no bloqueio do Kryptex com uma "tela branca".

**O servidor travou, ou fechei a janela sem querer. O que eu faço?**
R: Apenas reabra o `iniciar_servidor.bat` e aperte F5 na aba do Kryptex no Chrome.

**Como faço para ignorar os logs feios do Kryptex na tela do CMD?**
R: O projeto já utiliza `subprocess.DETACHED_PROCESS` e direciona as saídas de erro para `DEVNULL`, blindando completamente o servidor de vazamentos de logs do Electron/NodeJs do aplicativo Kryptex.
