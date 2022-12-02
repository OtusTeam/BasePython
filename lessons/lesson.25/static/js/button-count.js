const button = document.getElementById("click-button");
const countSpan = document.getElementById('clicked-times')
// console.log(button)

// button.onclick = function () {
//   console.log('here clicked too')
// }

let count = 0

function processButtonClick() {
  // console.log('here clicked too')
  count += 1
  updateValueOnPage()
}

function updateValueOnPage() {
  countSpan.innerText = count.toString()
}

button.addEventListener('click', processButtonClick)
