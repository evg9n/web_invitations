const countdownElement = document.getElementById('countdown');
const daysElement = document.getElementById('days');
const minutesElement = document.getElementById('minutes');
const hoursElement = document.getElementById('hours');
const secondsElement = document.getElementById('seconds');
const date = document.getElementById('date').innerHTML
const targetDate = new Date(date).getTime();

function updateCountdown() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    daysElement.innerHTML = `<span class="text-xl">${days}</span><span class="font-light">Дней</span>`
    hoursElement.innerHTML = `<span class="text-xl">${hours}</span><span class="font-light">Часа</span>`
    minutesElement.innerHTML = `<span class="text-xl">${minutes}</span><span class="font-light">Минут</span>`
    secondsElement.innerHTML = `<span class="text-xl">${seconds}</span><span class="font-light">Секунд</span>`

    if (distance < 0) {
        clearInterval(updateInterval);
        countdownElement.innerHTML = "Время истекло!";
    }
}

const updateInterval = setInterval(updateCountdown, 1000);