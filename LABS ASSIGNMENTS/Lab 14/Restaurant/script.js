const slides = document.querySelector('.slides');
const images = document.querySelectorAll('.slides img');
const prev = document.getElementById('prev');
const next = document.getElementById('next');

let index = 0;

function showSlide(i) {
  index = (i + images.length) % images.length;
  slides.style.transform = `translateX(-${index * 100}%)`;
}

next.addEventListener('click', () => showSlide(index + 1));
prev.addEventListener('click', () => showSlide(index - 1));

// Auto-slide every 4 seconds
setInterval(() => showSlide(index + 1), 4000);
