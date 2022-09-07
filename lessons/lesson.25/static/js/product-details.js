function sendDeleteRequest(url, onSuccess) {
  const xhr = new XMLHttpRequest();

  xhr.open("DELETE", url, true);
  xhr.onload = function () {
    const data = JSON.parse(xhr.responseText);
    if (xhr.readyState == 4 && xhr.status == "200") {
      onSuccess(data)
    } else {
      console.error(data);
    }
  }
  xhr.send(null);
}
