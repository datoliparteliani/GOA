let arrayToDo = []

const boxCon = document.getElementsByClassName("box-con")[0]
const input = document.getElementById("coms")
const btn = document.getElementById("button")
const resetBtn = document.getElementById("reset-button")

btn.onclick = () => {
    const value = input.value.trim()
    if (!value) return

    arrayToDo.push({ text: value, completed: false })
    input.value = ""
    renderList()
};

resetBtn.onclick = () => {
    arrayToDo = []
    renderList()
};

function renderList() {
    boxCon.innerHTML = ""

    arrayToDo.forEach((item, index) => {
        const taskDiv = document.createElement("div")
        taskDiv.className = "flex items-center justify-between bg-gray-50 p-2 rounded-xl shadow-sm"

        const span = document.createElement("span")
        span.textContent = item.text
        span.className = "flex-grow cursor-pointer" + (item.completed ? " line-through text-gray-400" : "")
        span.onclick = () => {
            arrayToDo[index].completed = !arrayToDo[index].completed
            renderList()
        }

        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Remove"
        deleteBtn.className = "text-red-500 hover:text-red-700 ml-4"
        deleteBtn.onclick = () => {
            arrayToDo.splice(index, 1)
            renderList()
        }

        taskDiv.appendChild(span)
        taskDiv.appendChild(deleteBtn)
        boxCon.appendChild(taskDiv)
    })
}
