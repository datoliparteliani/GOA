let arrayToDo = []
const boxCon = document.getElementsByClassName("box-con")[0]
const input = document.getElementById("coms")
const btn = document.querySelector("button")
const resetBtn = document.getElementById("reset-button")

btn.onclick = () => {
    const value = input.value

    arrayToDo.push(value)

    boxCon.innerHTML = ""

    arrayToDo.forEach((item, index) => {
        const div = document.createElement("div")
        div.textContent = item
        boxCon.append(div)
    })
}

resetBtn.onclick = () => {
    arrayToDo = []
    boxCon.innerHTML = ""
}