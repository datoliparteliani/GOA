const ul = document.createElement("ul");

for (let i = 0; i < 5; i++) {
    const li = document.createElement("li");
    li.textContent = `I am list item ${i + 1}`;
    li.classList.add((i + 1) % 2 == 0 ? 'even' : 'odd');
    ul.appendChild(li);
}

document.body.appendChild(ul);