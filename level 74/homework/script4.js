for (let c = 0; c <= 100; c++) {
    let f = (c * 9/5) + 32

    if (c < 10) {
        console.log(c, "=", f, "ცივა")
    } else if (c <= 30) {
        console.log(c, "=", f, "თბილა")
    } else {
        console.log(c, "=", f, "ცხელა")
    }
}