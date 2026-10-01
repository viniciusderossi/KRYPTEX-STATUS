# ⛏️ Kryptex Auto-Restart Monitor

Um sistema inteligente e 100% local (Open-Source) criado para monitorar o status das suas máquinas de mineração no **Kryptex** e reiniciar automaticamente o aplicativo no Windows caso a máquina trave, o minerador pare ou a placa de vídeo desarme.

## ⚙️ Como funciona?

O sistema é composto por duas partes que conversam entre si:

1. **Extensão do Google Chrome:** Injetada invisivelmente na página de hardware do seu painel do Kryptex. Ela faz a leitura automática dos seus computadores a cada minuto procurando por ícones de erro (triângulo vermelho) ou ausência de rentabilidade.
2. **Servidor Local Python:** Roda em uma tela do CMD no Windows. Ao receber o alerta de falha da extensão, ele usa o sistema `WMI` do Windows com poderes de Administrador para aniquilar qualquer processo travado do Kryptex (`Kryptex.exe`, `KryptexService.exe`, `SRBMiner`, etc.) e reiniciar o programa com a memória limpa.

## 🔒 Privacidade e Segurança

* **100% Local:** A extensão NÃO se comunica com a internet. Os alertas são enviados apenas para `http://127.0.0.1:15000` (seu próprio computador).
* **Nenhum Dado Sensível:** O sistema lê apenas os nomes dos computadores e os status na tela. Ele NÃO possui acesso a senhas, carteiras ou cookies do usuário.
* **Sistema de Cooldown:** Possui um temporizador de segurança de 10 minutos após cada reinício para evitar loops infinitos enquanto o Kryptex faz benchmarking.

## 🚀 Instalação Totalmente Automática (Plug & Play)

A maior vantagem deste projeto é que você não precisa ter conhecimentos técnicos. **O script faz tudo sozinho!**

### Requisitos
* Google Chrome (ou Brave/Edge)
* Sistema Windows
* *(Não precisa se preocupar em instalar o Python, o nosso sistema identifica se você não tem e faz o download e a instalação silenciosa para você no primeiro clique!)*

### Passo 1: Configurar a Extensão no Chrome
1. Faça o download deste repositório e extraia a pasta no seu PC.
2. Abra o Chrome e digite na barra de endereços: `chrome://extensions/`
3. Ative o **Modo do desenvolvedor** (no canto superior direito).
4. Clique em **Carregar sem compactação** e selecione a pasta `extensao_kryptex`.
5. Fixe a extensão na sua barra, clique nela e defina o computador que deseja monitorar. Você pode digitar o nome manualmente ou **clicar no botão azul (🔄) para a extensão buscar e listar automaticamente todas as suas máquinas disponíveis na página!** Selecione a máquina e clique em Salvar.

### Passo 2: Iniciar o Servidor
1. Na pasta principal, dê um duplo clique no arquivo **`iniciar_servidor.bat`**.
2. Ele vai pedir permissão de Administrador (necessário para conseguir matar os processos travados do Kryptex). Clique em **Sim**.
3. **Se você não tiver o Python instalado:** O próprio script vai baixar e instalar o Python silenciosamente para você! Ele fará isso apenas na primeira vez que você abrir, de forma 100% automática.
4. Uma tela preta ficará aberta aguardando informações. Deixe-a aberta!

### Passo 3: Monitoramento
1. Acesse o painel de hardware do Kryptex no Chrome: `https://www.kryptex.com/pt/hardware/computers`
2. Mantenha essa aba aberta (ela pode ficar em segundo plano).
3. A extensão cuidará do resto e se comunicará com o servidor local sempre que o PC travar!

---

**⚠️ Dica para Automação Total:** Se quiser que o script inicie automaticamente junto com o Windows (para casos de tela azul onde o PC reinicia sozinho), aperte `Win + R`, digite `shell:startup` e crie um Atalho do `iniciar_servidor.bat` lá dentro.

**Apoie o Projeto:** Se este projeto te salvou algumas noites de mineração perdidas, considere apoiar usando o botão na própria extensão! ☕
