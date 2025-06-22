const elArray = document.querySelectorAll(".el")

elArray.forEach((item, index) => {
    item.onclick = () => {
        console.log(index)
    }
})