setInterval(setClock, 1000);

const secondHand = document.querySelector('[data-second-hand]');
const minuteHand = document.querySelector('[data-minute-hand]');
const hourHand = document.querySelector('[data-hour-hand]');

function setClock() {
    const time = new Date();
    const second = time.getSeconds() / 60;
    const minute = (second / 60) + time.getMinutes()/ 60;
    const hour = (minute + time.getHours())/12;
    console.log(second);
    console.log(minute);
    console.log(hour);
    

    setRotation(secondHand, second);
    setRotation(minuteHand, minute);
    setRotation(hourHand, hour);
}

function setRotation (element, rotationRation) {
    element.style.setProperty('--rotation', rotationRation*360);
}