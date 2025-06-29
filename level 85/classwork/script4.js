const date = new Date
const year = date.getFullYear()
const day = date.getDay()
const number = date.getDate()
const time = date.getTime()
const h2 = document.createElement("h2")
const body = document.body
h2.textContent = `${year}. ${day}. ${number}. ${time}`
body.append(h2)