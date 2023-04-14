let currentLetter = parseInt(new URL(location.href).searchParams.get('id') ?? '1');
let letterCount = 1;

const letter = document.getElementById('letter');
const letterText = document.getElementById('letter-content');
const errorMessage = document.getElementById('error-message');
const idLabel = document.getElementById('letter-id');
const nextLink = document.getElementById('next');
const previousLink = document.getElementById('previous');
const stampContainer = document.getElementById('stamp-container');

const loadLetter = () => {
  stampContainer.classList.remove('stamped');
  idLabel.innerText = currentLetter;

  fetch(`/message/${currentLetter}`)
    .then(response => response.json())
    .then(data => {
      stampContainer.classList.add('stamped');

      nextLink.style.visibility = currentLetter === data.count ? 'hidden' : '';
      previousLink.style.visibility = currentLetter === 1 ? 'hidden' : '';

      if (data.error) {
        letter.style.visibility = 'hidden';
        errorMessage.style.visibility = '';
        errorMessage.textContent = data.error;
        return;
      }

      letter.style.visibility = '';
      errorMessage.style.visibility = 'hidden';
      letterText.value = data.message;
    });
};

loadLetter();

nextLink.addEventListener('click', (event) => {
  event.preventDefault();
  currentLetter += 1;
  loadLetter();
});

previousLink.addEventListener('click', (event) => {
  event.preventDefault();
  currentLetter -= 1;
  loadLetter();
});
