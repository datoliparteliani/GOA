const boxes = document.querySelectorAll(".box");

for (let i = 0; i < boxes.length; i++) {
    console.log(boxes[i]);
}

function changeBg() {
    boxes[0].style.background = "aqua"
    boxes[1].style.background = "aqua"
    boxes[2].style.background = "aqua"
    boxes[3].style.background = "aqua"
    boxes[4].style.background = "aqua"
    boxes[5].style.background = "aqua"
}