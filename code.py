// HTML:
// <!DOCTYPE html>
// <html>
// <head>
//     <script src="https://cdn.jsdelivr.net/npm/web3@1.5.2/dist/web3.min.js"></script>
// </head>
// <body>
//     <h1>Цитата дня</h1>
//     <p id="quote"></p>
//     <button onclick="setQuote()">Установить новую цитату</button>
// </body>
// <script src="app.js"></script>
// </html>

// JavaScript (app.js):
document.addEventListener("DOMContentLoaded", function () {
    if (window.ethereum) {
        window.web3 = new Web3(window.ethereum);
        window.ethereum.enable().then(function (accounts) {
            web3.eth.getAccounts((error, accounts) => {
                if (error) {
                    console.error(error);
                } else {
                    const account = accounts[0];
                    initApp(account);
                }
            });
        });
    }
});

function initApp(account) {
    const contractAddress = "YOUR_CONTRACT_ADDRESS"; // Замените на адрес вашего умного контракта
    const contractAbi = [YOUR_CONTRACT_ABI]; // Замените на ABI вашего контракта

    const quoteContract = new web3.eth.Contract(contractAbi, contractAddress);

    // Функция для получения текущей цитаты дня
    async function getQuote() {
        try {
            const currentQuote = await quoteContract.methods.getQuote().call();
            document.getElementById("quote").innerText = currentQuote;
        } catch (error) {
            console.error(error);
        }
    }

    // Функция для установки новой цитаты
    async function setQuote() {
        const newQuote = prompt("Введите новую цитату:");
        if (newQuote) {
            try {
                const gas = await quoteContract.methods.setQuote(newQuote).estimateGas({ from: account });
                const result = await quoteContract.methods.setQuote(newQuote).send({ from: account, gas });
                console.log(result);
                getQuote();
            } catch (error) {
                console.error(error);
            }
        }
    }

    getQuote();
}
