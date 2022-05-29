const defensiveButton = document.querySelector(".defensive-button"); 
const defensiveContainer = document.querySelector("#delete-defensive-container");


defensiveButton.onclick = function () {
    defensiveContainer.classList.toggle("active")
}; 

// window.onclick = function () {
//     defensiveContainer.classList.toggle("remove")
// }