const originalP = document.createElement('p');
originalP.textContent = "ეს არის ორიგინალური პერაგრაფი";

const clonedP = originalP.cloneNode(true);
clonedP.style.color = 'red';

document.body.appendChild(originalP);
document.body.appendChild(clonedP);