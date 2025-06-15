const ul = document.createElement("ul")

for (let i = 0; i < 20; i++) {
    const li = document.createElement("li")
    li.textContent = `Item ${i}`
    ul.appendChild(li)
}

document.body.append(ul)