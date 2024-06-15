document.querySelectorAll('input[name="attendance"]').forEach(radio => {
    radio.addEventListener('change', function() {
        if (this.value === 'yes') {
            document.getElementById('additional-fields').classList.remove('hidden');
            document.getElementById('sad-response').classList.add('hidden');
        } else {
            document.getElementById('additional-fields').classList.add('hidden');
            document.getElementById('sad-response').classList.remove('hidden');
        }
    });
});