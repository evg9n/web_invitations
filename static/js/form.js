document.querySelectorAll('input[name="attendance"]').forEach(radio => {
    radio.addEventListener('change', function() {
        if (this.value === 'yes') {
            document.getElementById('additional-fields').classList.remove('hidden');
            document.getElementById('sad-response').classList.add('hidden');

            document.getElementById('toTransferYes').setAttribute('required', '')
            document.getElementById('toTransferNo').setAttribute('required', '')

            document.getElementById('fromTransferYes').setAttribute('required', '')
            document.getElementById('fromTransferNo').setAttribute('required', '')
            
            var elements = document.getElementsByClassName('sad-text');

            
            if (elements.length > 0) {
                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.display = 'none';
                }                
            }

            document.getElementById('particles-js').style.display = 'block';
            
            setTimeout(function() {
                document.getElementById('particles-js').style.display = 'none';
            }, 5000);
            showCelebration();
        } else {
            document.getElementById('additional-fields').classList.add('hidden');
            document.getElementById('sad-response').classList.remove('hidden');

            document.getElementById('toTransferYes').removeAttribute('required')
            document.getElementById('toTransferNo').removeAttribute('required')

            document.getElementById('fromTransferYes').removeAttribute('required')
            document.getElementById('fromTransferNo').removeAttribute('required')

            document.getElementById('particles-js').style.display = 'none';
            showSadText()
        }
    });
});

document.querySelectorAll('input[name="to_transfer"]').forEach(radio => {
    radio.addEventListener('change', function() {
        var inputs = document.querySelectorAll('#formFromCity input');
        if (this.value === 'yes') {
            document.getElementById('formFromCity').classList.remove('hidden');
            
            inputs.forEach(function(input) {
                input.setAttribute('required', '');
            });
        } else {
            document.getElementById('formFromCity').classList.add('hidden');

            inputs.forEach(function(input) {
                input.removeAttribute('required');
            });
        }
    });
});

document.querySelectorAll('input[name="from_transfer"]').forEach(radio => {
    radio.addEventListener('change', function() {
        var inputs = document.querySelectorAll('#formToCity input');
        if (this.value === 'yes') {
            document.getElementById('formToCity').classList.remove('hidden');

            inputs.forEach(function(input) {
                input.setAttribute('required', '');
            });
        } else {
            document.getElementById('formToCity').classList.add('hidden');

            inputs.forEach(function(input) {
                input.removeAttribute('required');
            });
        }
    });
});


function showCelebration() {
    particlesJS('particles-js', {
        particles: {
            number: {
                value: 150,
                density: {
                    enable: true,
                    value_area: 1000
                }
            },
            color: {
                value: ["#ff0000", "#ffff00", "#00ff00", "#0000ff", "#ff00ff"]
            },
            shape: {
                type: "circle",
                stroke: {
                    width: 0
                }
            },
            opacity: {
                value: 0.8,
                random: false,
                anim: {
                    enable: true,
                    speed: 1,
                    opacity_min: 0
                }
            },
            size: {
                value: 10,
                random: true,
                anim: {
                    enable: true,
                    speed: 10,
                    size_min: 0.1
                }
            },
            line_linked: {
                enable: false
            },
            move: {
                enable: true,
                speed: 20,
                direction: "none",
                random: true,
                straight: false,
                out_mode: "out",
                bounce: false,
                attract: {
                    enable: false,
                    rotateX: 600,
                    rotateY: 1200
                }
            }
        },
        interactivity: {
            detect_on: "canvas",
            events: {
                onhover: {
                    enable: false
                },
                onclick: {
                    enable: false
                }
            }
        },
        retina_detect: true
    });
}

function showSadText() {
    spacePressCount = 0;
    if (snowInterval) {
        return;
    }

    snowInterval = setInterval(createTextflake, 100);

    setTimeout(function() {
        clearInterval(snowInterval);
        snowInterval = null;
    }, 2000);
}

function createTextflake() {
    const snowflake = document.createElement('div');
    snowflake.classList.add('sad-text');
    snowflake.textContent = '😢';
    document.body.appendChild(snowflake);

    snowflake.style.left = `${Math.random() * window.innerWidth}px`;
    snowflake.style.top = `0px`;

    animateTextflake(snowflake);
}

function animateTextflake(flake) {
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