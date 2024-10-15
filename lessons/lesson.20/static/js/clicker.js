document.addEventListener("DOMContentLoaded", function () {
    const clickButton = document.getElementById("click-button");
    const counterDisplay = document.getElementById("counter");
    let counter = 0;

    clickButton.addEventListener("click", function () {
        counter++;
        counterDisplay.textContent = counter;
    });
});
