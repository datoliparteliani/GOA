const btn1 = document.getElementById("btn1");
const btn2 = document.getElementById("btn2");
const body = document.querySelector("body");

function toggleBlue() {
    body.classList.toggle("lightblue");
}

btn1.addEventListener("click", toggleBlue);

btn2.addEventListener("click", () => {
    btn1.removeEventListener("click", toggleBlue);
})