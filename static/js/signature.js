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
    spacePressCount = 0;
    if (snowInterval) {
        return;
    }

    snowInterval = setInterval(createSnowflake, 100);

    setTimeout(function() {
        clearInterval(snowInterval);
        snowInterval = null;
    }, 10000);
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
    const fallSpeed = Math.random() * 5 + 2;

    function fall() {
        posY += fallSpeed;
        flake.style.top = `${posY}px`;

        if (posY < window.innerHeight) {
            requestAnimationFrame(fall);
        } else {
            flake.remove();
        }
    }

    fall();
}