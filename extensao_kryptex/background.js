chrome.runtime.onInstalled.addListener(() => {
    chrome.alarms.create("kryptex_watchdog", { periodInMinutes: 1.5 });
});

chrome.alarms.onAlarm.addListener((alarm) => {
    if (alarm.name === "kryptex_watchdog") {
        chrome.tabs.query({ url: "*://*.kryptex.com/*" }, (tabs) => {
            tabs.forEach(tab => {
                chrome.tabs.reload(tab.id);
            });
        });
    }
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "SEND_STATUS") {
        fetch(`http://127.0.0.1:15000/${request.status}`, { mode: "no-cors", cache: "no-store" })
            .then(res => console.log('Servidor respondeu com sucesso'))
            .catch(err => console.log('Erro no background:', err));
    }
});
