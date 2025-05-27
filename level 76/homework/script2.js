const points = [10, 30, 5, 2, 99]
const points2 = [11, 31, 6, 3, 100]
points.pop()
points.push(140)
points.shift()
points.unshift(140)
let all = points.join(" ")
let str = points.toString()
let con = points.concat(points2)
console.log(points)
console.log(all)
console.log(str)
console.log(con)