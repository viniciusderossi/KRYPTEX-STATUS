# â›ï¸ Kryptex Auto-Restart Monitor

Um sistema inteligente e 100% local (Open-Source) criado para monitorar o status das suas mÃ¡quinas de mineraÃ§Ã£o no **Kryptex** e reiniciar automaticamente o aplicativo no Windows caso a mÃ¡quina trave, o minerador pare ou a placa de vÃ­deo desarme.

## ðŸ§  Como funciona?
O sistema Ã© composto por duas partes que conversam entre si:
1. **ExtensÃ£o do Google Chrome:** Injetada invisivelmente na pÃ¡gina de hardware do seu painel do Kryptex. Ela faz a leitura automÃ¡tica dos seus computadores a cada minuto procurando por **Ã­cones de erro (triÃ¢ngulo vermelho) ou ausÃªncia de rentabilidade**.
2. **Servidor Local Python:** Roda em uma tela do CMD no Windows. Ao receber o alerta de falha da extensÃ£o, ele usa o sistema `WMI` do Windows com poderes de Administrador para aniquilar qualquer processo travado do Kryptex (`Kryptex.exe`, `KryptexService.exe`, `SRBMiner`, etc.) e reiniciar o programa com a memÃ³ria limpa.

---

## ðŸ”’ Privacidade e SeguranÃ§a
* **100% Local:** A extensÃ£o nÃ£o se comunica com a internet. Os alertas sÃ£o enviados apenas para `http://127.0.0.1:15000` (seu prÃ³prio computador).
* **Nenhum Dado SensÃ­vel:** O sistema lÃª apenas os nomes dos computadores e os status na tela. Ele nÃ£o possui acesso a senhas, carteiras ou cookies do usuÃ¡rio.
* **Sistema de Cooldown:** Possui um temporizador de seguranÃ§a de 10 minutos apÃ³s cada reinÃ­cio para evitar loops infinitos enquanto o Kryptex faz benchmarking.

---

## ðŸ› ï¸ InstalaÃ§Ã£o e Uso

### Requisitos
* Google Chrome (ou Brave/Edge)
* Python 3 instalado no Windows

### Passo 1: Configurar a ExtensÃ£o no Chrome
1. FaÃ§a o download deste repositÃ³rio e extraia a pasta no seu PC.
2. Abra o Chrome e digite na barra de endereÃ§os: `chrome://extensions/`
3. Ative o **Modo do desenvolvedor** (no canto superior direito).
4. Clique em **Carregar sem compactaÃ§Ã£o** e selecione a pasta `extensao_kryptex`.
5. Fixe a extensÃ£o na sua barra, clique nela e defina o computador que deseja monitorar. VocÃª pode digitar o nome manualmente ou **clicar no botÃ£o azul (ðŸ”„) para a extensÃ£o buscar e listar automaticamente todas as suas mÃ¡quinas disponÃ­veis na pÃ¡gina!** Selecione a mÃ¡quina e clique em Salvar.

### Passo 2: Iniciar o Servidor
1. Na pasta principal, dÃª um duplo clique no arquivo **`iniciar_servidor.bat`**.
2. O Windows vai pedir permissÃ£o de Administrador (necessÃ¡rio para conseguir matar os processos travados do Kryptex). Clique em **Sim**.
3. A tela preta ficarÃ¡ aguardando informaÃ§Ãµes.

4. Uma tela preta ficara aguardando informacoes. (Deixe-a aberta): Monitoramento
1. Acesse o painel de hardware do Kryptex no Chrome: `https://www.kryptex.com/pt/hardware/computers`
2. Mantenha essa aba aberta (ela pode ficar em segundo plano).
3. A extensÃ£o cuidarÃ¡ de atualizar a pÃ¡gina a cada 5 minutos e fazer varreduras a cada 60 segundos!

---

## â“ FAQ (Perguntas Frequentes)

**O servidor reinicia o Kryptex sempre que nÃ£o hÃ¡ saldo (R$) na tela?**
R: NÃ£o. Para evitar falsos positivos durante o inÃ­cio da mineraÃ§Ã£o, a extensÃ£o procura a ausÃªncia do saldo atrelada Ã  *presenÃ§a de uma classe HTML de erro (o triÃ¢ngulo vermelho)*. 

**Por que o arquivo .bat pede privilÃ©gios de Administrador?**
R: O Kryptex utiliza serviÃ§os de segundo plano (como o `KryptexService.exe`) que operam em nÃ­vel elevado para modificar drivers de GPU. Um script normal nÃ£o tem permissÃ£o para fechÃ¡-los, resultando no bloqueio do Kryptex com uma "tela branca".

**O servidor travou, ou fechei a janela sem querer. O que eu faÃ§o?**
R: Apenas reabra o `iniciar_servidor.bat` e aperte F5 na aba do Kryptex no Chrome.

**Como faÃ§o para ignorar os logs feios do Kryptex na tela do CMD?**
R: O projeto jÃ¡ utiliza `subprocess.DETACHED_PROCESS` e direciona as saÃ­das de erro para `DEVNULL`, blindando completamente o servidor de vazamentos de logs do Electron/NodeJs do aplicativo Kryptex.
