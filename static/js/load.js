window.addEventListener('load', function() {
    document.getElementById('loading-screen').style.display = 'none';
    document.getElementById('content').classList.remove('hidden');
});

// window.addEventListener('load', function() {
//     setTimeout(function() {
//         document.getElementById('loading-screen').style.display = 'none';
//         document.getElementById('content').classList.remove('hidden');
//     }, 5000); // Задержка в 5000 миллисекунд, что равно 5 секундам
// });
