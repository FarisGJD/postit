const hamburger = document.getElementById('hamburger');
const navUl = document.getElementById('navbar');
const ctaButton = document.getElementById('cta-button'); 


hamburger.addEventListener('click', () => {
    navUl.classList.toggle('show'); 
    ctaButton.classList.toggle('show');
})