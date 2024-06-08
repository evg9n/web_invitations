let spacePressCount = 0;
let snowInterval;

document.addEventListener('keydown', function(e) {
    if (e.code === 'Enter') {
        spacePressCount++;
        if (spacePressCount === 10) {
            startSnowing();
        }
    } else {
        spacePressCount = 0;
    }
});

function startSnowing() {
    spacePressCount = 0; // Сброс счётчика нажатий Enter
    if (snowInterval) {
        return; // Если снег уже идёт, не начинать заново
    }

    snowInterval = setInterval(createSnowflake, 100);

    setTimeout(function() {
        clearInterval(snowInterval); // Останавливаем создание новых снежинок
        snowInterval = null; // Сбрасываем переменную интервала
    }, 10000); // Задаём таймер на 10 секунд
}

function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.classList.add('eea-snowflake');
    snowflake.textContent = 'EEA';
    document.body.appendChild(snowflake);

    snowflake.style.left = `${Math.random() * window.innerWidth}px`;
    snowflake.style.top = `0px`;

    animateSnowflake(snowflake);
}

function animateSnowflake(flake) {
    let posY = 0;
    const fallSpeed = Math.random() * 5 + 2; // Скорость падения снежинки

    function fall() {
        posY += fallSpeed;
        flake.style.top = `${posY}px`;

        if (posY < window.innerHeight) {
            requestAnimationFrame(fall);
        } else {
            flake.remove(); // Удаляем снежинку после того, как она вышла за пределы экрана
        }
    }

    fall();
}