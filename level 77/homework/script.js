let elements = ["el1", "el2", "el3", "el4", 'el5']
const slicedEl = elements.slice(2, 3)
const splicedEl = elements.splice(1, 3)
const addedEl = elements.splice(2, 2, slicedEl)