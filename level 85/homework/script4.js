const body = document.body

const newYearDiv = document.createElement("div")
const giorgobaDiv = document.createElement("div")
const barbarobaDiv = document.createElement("div")

body.append(newYearDiv, giorgobaDiv, barbarobaDiv)

setInterval(() => {
    const now = new Date()

    const newYear = new Date(now.getFullYear() + 1, 0, 1)
    const giorgoba = new Date(now.getFullYear(), 10, 23)
    const barbaroba = new Date(now.getFullYear(), 11, 17)

    if (giorgoba < now) {
        giorgoba.setFullYear(giorgoba.getFullYear() + 1)
    }
    if (barbaroba < now) {
        barbaroba.setFullYear(barbaroba.getFullYear() + 1)
    }

    function countdown(toDate) {
        const diff = toDate - now
        const d = Math.floor(diff / (1000 * 60 * 60 * 24))
        const h = Math.floor(diff / (1000 * 60 * 60)) % 24
        const m = Math.floor(diff / (1000 * 60)) % 60
        const s = Math.floor(diff / 1000) % 60
        return `${d} day ${h}:${m}:${s}`
    }

    newYearDiv.textContent = `Till new year: ${countdown(newYear)}`
    giorgobaDiv.textContent = `Till giorgoba: ${countdown(giorgoba)}`
    barbarobaDiv.textContent = `TIll barbaroba: ${countdown(barbaroba)}`

}, 1000)