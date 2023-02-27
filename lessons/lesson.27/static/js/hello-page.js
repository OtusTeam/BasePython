console.log('Hello page', window.location.href)

const clickButton = document.getElementById('click-button')

let clickCount = 0
const countSpan = document.getElementById("count-span")
console.log(countSpan)

function handleClick() {
  clickCount += 1
  countSpan.innerText = clickCount.toString()
}

clickButton.addEventListener('click', function () {
  console.log('handle click')
  handleClick()
})

const productIdSpan = document.getElementById('product-id')
const productInfo = document.getElementById('product-info')

function fetchAndShowProduct(productId) {
  fetch(`/items/${productId}/`
  ).then(response => response.json()
  ).then(data => {
    productIdSpan.innerText = productId.toString()
    productInfo.innerText = JSON.stringify(data, null, 2)
  })
}

let productLastId = 0
// setTimeout(function () {
//   productLastId += 1
//   fetchAndShowProduct(productLastId)
// }, 1000)

// setInterval(function () {
//   productLastId += 1
//   fetchAndShowProduct(productLastId)
// }, 1000)

