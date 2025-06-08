const btn1 = document.getElementById("btn1")
const btn2 = document.getElementById("btn2")
const btn3 = document.getElementById("btn3")
const body = document.querySelector("body")

btn1.addEventListener("click", () => {
    body.classList.toggle("lightblue")
})

btn2.addEventListener("click", () => {
    body.classList.toggle("lightgreen")
})

btn3.addEventListener("click", () => {
    body.classList.toggle("lightcoral")
})
