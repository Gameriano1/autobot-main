// ==UserScript==
// @name         Bing Search Automation
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Automates Bing searches using cookies
// @author       Your Name
// @match        https://www.bing.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Função para obter os cookies do Bing
    function getCookies() {
        var cookies = document.cookie.split("; ");
        var cookieData = {};

        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].split("=");
            var cookieName = cookie[0];
            var cookieValue = cookie[1];
            cookieData[cookieName] = cookieValue;
        }

        return cookieData;
    }

    // Função para fazer uma solicitação de pesquisa
    function performSearch(searchQuery) {
        return new Promise(function(resolve, reject) {
            // Obtenha os cookies do Bing
            var cookies = getCookies();

            // Crie um objeto XMLHttpRequest para enviar a solicitação de pesquisa
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "https://www.bing.com/search?q=" + encodeURIComponent(searchQuery), true);

            // Adicione os cookies à solicitação
            for (var cookieName in cookies) {
                var cookieValue = cookies[cookieName];
                xhr.setRequestHeader("Cookie", cookieName + "=" + cookieValue);
            }

            // Manipule a resposta da solicitação
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        resolve("Solicitação de pesquisa concluída com sucesso!");
                    } else {
                        reject("Falha na solicitação de pesquisa");
                    }
                }
            };

            // Envie a solicitação de pesquisa
            xhr.send();
        });
    }

    // Função para gerar uma palavra aleatória
    function generateRandomWord() {
        var letters = "abcdefghijklmnopqrstuvwxyz";
        var randomWord = "";

        for (var i = 0; i < 15; i++) {
            var randomIndex = Math.floor(Math.random() * letters.length);
            randomWord += letters.charAt(randomIndex);
        }

        return randomWord;
    }

    // Array para armazenar todas as promessas de pesquisa
    var searchPromises = [];

    // Loop para criar todas as promessas de pesquisa
    for (var i = 0; i < 110; i++) {
        var randomWord = generateRandomWord();
        var searchPromise = performSearch(randomWord);
        searchPromises.push(searchPromise);
    }

    // Executa todas as promessas de pesquisa simultaneamente
    Promise.all(searchPromises)
        .then(function(results) {
            console.log(results);
        })
        .catch(function(error) {
            console.error(error);
        });
})();