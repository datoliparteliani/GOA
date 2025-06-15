for (let i = 0; i < 101; i++) {
    const h2 = document.createElement("h2")
    h2.textContent = `child ${i < 10 ? `00${i}` :    `0${i}`}`
    document.body.append(h2)
}