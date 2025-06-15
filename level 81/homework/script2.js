const div = document.createElement("div");

const texts = ["1", "2", "3", "4", "5"];
const colors = ["red", "blue", "green", "orange", "purple"];

for (let i = 0; i < 5; i++) {
  const p = document.createElement("p");
  p.textContent = `text ${texts[i]}`;
  p.style.color = colors[i];
  div.appendChild(p);
}

document.body.appendChild(div);