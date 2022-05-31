function deleteItem() {
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState === 4 && this.status === 200) {
      // Typical action to be performed when the document is ready:
      const data = JSON.parse(xhttp.responseText);
      console.log('received data', data)
      window.location.href = data.url || '/';
    }
  };
  xhttp.open("DELETE", window.location, true);
  xhttp.send();
}

window.onload = function () {
  const buttonDelete = document.getElementById('delete-product');
  buttonDelete.addEventListener('click', function () {
    console.log('button clicked!')
    if (confirm('Delete item?')) {
      console.log('delete.')
      deleteItem();
    } else {
      console.log('dont.ok')
    }
  })
}