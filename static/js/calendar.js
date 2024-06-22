const calendarDate = document.getElementById('date').innerHTML.trim();

function generateCalendar(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = date.getMonth();
    const day = date.getDate();
    
    const monthYearElement = document.getElementById('monthYear');
    const calendarElement = document.getElementById('calendar');
    
    const monthNames = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
    monthYearElement.textContent = `${monthNames[month]} ${year}`;
    
    const firstDay = (new Date(year, month, 1).getDay() + 6) % 7; // Смещаем первый день недели на понедельник
    const lastDate = new Date(year, month + 1, 0).getDate();
    
    calendarElement.innerHTML = '';
    
    const daysOfWeek = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'];
    daysOfWeek.forEach(day => {
        const dayElement = document.createElement('div');
        dayElement.textContent = day;
        dayElement.classList.add('day');
        calendarElement.appendChild(dayElement);
    });
    
    for (let i = 0; i < firstDay; i++) {
        const emptyCell = document.createElement('div');
        emptyCell.classList.add('date');
        calendarElement.appendChild(emptyCell);
    }
    
    for (let i = 1; i <= lastDate; i++) {
        const dateElement = document.createElement('div');
        dateElement.textContent = i;
        dateElement.classList.add('date');
        if (i === day) {
            dateElement.classList.add('highlighted');
        }
        calendarElement.appendChild(dateElement);
    }
}

generateCalendar(calendarDate);