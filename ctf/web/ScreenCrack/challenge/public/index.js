const screenshotBtn = document.getElementById('screenshot-btn');
const sourceBtn = document.getElementById('source-btn');
const screenshotDiv = document.getElementById('screenshot');
const sourceIframe = document.getElementById('filesource');
const sourceDiv = document.getElementById('source');
const urlInput = document.getElementById('url-input');

screenshotBtn.addEventListener('click', () => {
    sourceIframe.classList.add('hidden');

    const url = urlInput.value;
    if (url === "") {
        alert("Please Enter a Url");
        return;
    }
    const img = document.createElement('img');
    try {
        sourceDiv.innerHTML = '';
    }catch (e) {
        console.log(e);
    }

    const data = {
      site: url
    };

    fetch('/api/getss', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then((e) => {
            if (!e.image) {
                alert(e.message);
                return;
            }
            img.src = e.image;
            screenshotDiv.innerHTML = '';
            screenshotDiv.appendChild(img);
            screenshotDiv.classList.remove('hidden');
        }
    )
    .catch(error => console.error(error));
});

sourceBtn.addEventListener('click', () => {
    screenshotDiv.classList.add('hidden');

    var url = urlInput.value;
    if (url === "") {
        alert("Please Enter a Url");
        return;
    }

    if (!url.includes("://")) {
        url = "http://" + url
    }

    const data = {
      site: url
    };

    fetch('/api/get-html', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => {response.json(), alert("OK1!")})
    .then((e) => {
            if (!e.filename){
                alert("There was an error.");
                return;
            }
	    else
	    {
	    	alert("OK2!");
	    	alert(e.filename);
	    }
            sourceIframe.src = e.filename;
            sourceIframe.classList.remove('hidden');
        }
    )
    .catch(error => console.error(error));
});
