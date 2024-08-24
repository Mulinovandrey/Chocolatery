(function() {
    var currentDay = document.querySelectorAll('.list-hours li')[new Date().getDay() -1];

    if (currentDay) {
        currentDay.classList.add('today');
    }
})();
