let fruits = ["Banana", "Apples", "Oranges", "Blueberries"]
undefined
fruits.splice(0,1)
Array [ "Banana" ]
fruits.sort()
Array(3) [ "Apples", "Blueberries", "Oranges" ]
fruits.push("kiwi")
4
fruits
Array(4) [ "Apples", "Blueberries", "Oranges", "kiwi" ]
fruits.shift()
"Apples"
fruits.reverse()
Array(3) [ "kiwi", "Oranges", "Blueberries" ]
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
moreFruits[1][1][0]

let user1 = { username : 'Clarice', password : "Dev123" }
undefined
user1
Object { username: "Clarice", password: "Dev123" }
let database = [user1]
undefined
database
Array [ {…} ]
let newsfeed = [ {username:"Jane", timeline:123}, {username:"Rhoda", timeline:56},{username: "Lami", timeline:8796} ]
undefined
newsfeed
Array(3) [ {…}, {…}, {…} ]
0: Object { username: "Jane", timeline: 123 }
1: Object { username: "Rhoda", timeline: 56 }
2: Object { username: "Lami", timeline: 8796 }
length: 3
<prototype>: Array []
database.push({username:'Bryan',password:"Dev007"})
2
database
Array [ {…}, {…} ]
database.push(newsfeed[2])
3
database
Array(3) [ {…}, {…}, {…} ]
0: Object { username: "Clarice", password: "Dev123" }
1: Object { username: "Bryan", password: "Dev007" }
2: Object { username: "Lami", timeline: 8796 }
