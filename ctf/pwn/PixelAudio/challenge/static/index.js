const submitFile = document.getElementById("submitFile");
const playButton = document.getElementById("play-button");
const modalText = document.getElementById("modal-text");
const dialog = document.getElementById("dialog");
const dialogText = document.getElementById("dialog-text");

let hasFile = false;
playButton.style.opacity = 0.25;

const onClickSubmit = () => {
    submitFile.click();
}

const handleFileChange = async () => {
    const files = submitFile.files;

    if (files.length !== 1) {
        hasFile = false;
        playButton.style.opacity = 0.25;
        return;
    }

    const file = files[0];
    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        if (res.status !== 200) {
            hasFile = false;
            playButton.style.opacity = 0.25;
            alert(await res.text());
            return;
        }

        hasFile = true;
        playButton.style.opacity = 1;
        alert("File uploaded successfully")
    } catch (err) {
        console.log(err);
    }
}

const onClickPlay = async () => {
    if (!hasFile) {
        alert("Please upload a file first");
        return;
    }

    try {
        const res = await fetch("/play");
        const data = await res.text();
        console.log(data);
        dialog.showModal();
        dialogText.innerText = data;
    } catch (err) {
        console.log(err);
    }
}
