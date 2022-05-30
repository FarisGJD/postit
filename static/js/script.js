// const defensiveButton = document.querySelector(".defensive-button"); 
// const defensiveContainer = document.querySelector("#delete-defensive-container");


// defensiveButton.onclick = function () {
//     defensiveContainer.classList.toggle("active")
// }; 

const hamburger = document.getElementById('hamburger');
const navUl = document.getElementById('navbar');
const ctaButton = document.getElementById('cta-button')

console.log(navUl, hamburger, ctaButton)

hamburger.addEventListener('click', () => {
    navUl.classList.toggle('show'); 
    ctaButton.classList.toggle('show');
})