const div = document.createElement("div");

for (let i = 0; i < 3; i++) {
    const p = document.createElement("p");
    p.textContent = "text";
    div.appendChild(p);
}

document.body.append(div);

function remove() {
    const firstChild = div.querySelector("p");
    if (firstChild) {
        div.removeChild(firstChild);
        alert("Child removed!");
    } else {
        alert("No more children to remove.");
    }
}
