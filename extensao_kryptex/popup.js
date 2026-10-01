// Carrega o nome salvo quando o popup for aberto
document.addEventListener('DOMContentLoaded', () => {
    chrome.storage.sync.get(['pcName'], (result) => {
        if (result.pcName) {
            document.getElementById('pcName').value = result.pcName;
        } else {
            // Valor padrão se for a primeira vez
            document.getElementById('pcName').value = "PCVinicius";
        }
    });
});

// Salva o nome quando o botão for clicado
document.getElementById('saveBtn').addEventListener('click', () => {
    const pcName = document.getElementById('pcName').value.trim();
    
    if (pcName) {
        chrome.storage.sync.set({ pcName: pcName }, () => {
            const status = document.getElementById('status');
            status.style.display = 'block';
            setTimeout(() => {
                status.style.display = 'none';
            }, 2000);
        });
    }
});

// Lógica para mostrar/esconder a área de doação (Corrigido bug do 2 cliques)
document.getElementById('donateBtn').addEventListener('click', () => {
    const donateArea = document.getElementById('donateArea');
    const style = window.getComputedStyle(donateArea);
    if (style.display === 'none') {
        donateArea.style.display = 'block';
    } else {
        donateArea.style.display = 'none';
    }
});

// Lógica para buscar máquinas
document.getElementById('loadMachinesBtn').addEventListener('click', () => {
    const status = document.getElementById('status');
    
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        if (!tabs[0] || !tabs[0].url.includes("kryptex.com")) {
            status.style.color = '#ef4444'; // vermelho
            status.innerText = "Abra a página do Kryptex primeiro!";
            status.style.display = 'block';
            setTimeout(() => status.style.display = 'none', 3000);
            return;
        }
        
        chrome.tabs.sendMessage(tabs[0].id, {action: "GET_MACHINES"}, function(response) {
            if (chrome.runtime.lastError) {
                status.style.color = '#f59e0b'; // laranja
                status.innerText = "Recarregue a página do Kryptex (F5)!";
                status.style.display = 'block';
                setTimeout(() => status.style.display = 'none', 3000);
                return;
            }
            
            if (response && response.machines && response.machines.length > 0) {
                const datalist = document.getElementById('pcList');
                datalist.innerHTML = '';
                response.machines.forEach(name => {
                    let option = document.createElement('option');
                    option.value = name;
                    datalist.appendChild(option);
                });
                
                status.style.color = '#10b981'; // verde
                status.innerText = `${response.machines.length} máquinas listadas!`;
                status.style.display = 'block';
                setTimeout(() => status.style.display = 'none', 3000);
            } else {
                status.style.color = '#ef4444'; // vermelho
                status.innerText = "Nenhuma máquina encontrada na tela.";
                status.style.display = 'block';
                setTimeout(() => status.style.display = 'none', 3000);
            }
        });
    });
});

// Lógica dos botões de copiar (O Chrome bloqueia o "onclick" direto no HTML por segurança)
document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const targetId = this.getAttribute('data-target');
        const inputField = document.getElementById(targetId);
        
        inputField.select();
        document.execCommand('copy');
        
        const originalText = this.innerText;
        this.innerText = 'Copiado!';
        setTimeout(() => {
            this.innerText = originalText;
        }, 2000);
    });
});
