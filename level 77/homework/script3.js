const array = ['a', 'b', 'c', 'd', 'e']
const splicedAr = array.splice(1, 2)
const slicedSAr = splicedAr.slice(1, 2)
const addedSAr = splicedAr.splice(1, 2, "o", "x")
console.log(splicedAr)