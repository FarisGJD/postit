const defensiveButton = document.querySelector(".defensive-button"); 
const defensiveContainer = document.querySelector("#delete-defensive-container");
window.onclick = closeWindow;

defensiveButton.onclick = function () {
    defensiveContainer.classList.toggle("active")
}; 

function closeWindow() {
    document.getElementById("#delete-defensive-container").style.display = "none"
}