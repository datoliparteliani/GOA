const html = document.querySelector("html")
const button = document.getElementById("dark-mode")

let darkMode = true
button.addEventListener("click", function () {
    if (darkMode) {
        document.body.classList.add("dark")
        darkMode = false
    } else {
        document.body.classList.remove("dark")
        darkMode = true
    }
})