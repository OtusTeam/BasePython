const nextItemIdSpan = document.getElementById('next-item-id');
const itemDataOut = document.getElementById('item-data');

let nextItemId = 1;
const loadTimeout = 3;

function getNextItem(itemsUrl) {
  fetch(`${itemsUrl}${nextItemId}/`).then((result) => {
    result.json().then((data) => {
      itemDataOut.innerText = JSON.stringify(data, null, 2);
      nextItemId += 1;
      nextItemIdSpan.innerText = nextItemId.toString();
      setTimeout(() => {
        getNextItem(itemsUrl)
      }, loadTimeout * 1000)
    })
  })
}
