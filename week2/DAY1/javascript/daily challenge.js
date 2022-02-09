  //Exercice 1

 let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

 fruits.shift();
 console.log("Retirez Banana:",fruits)//Question1


 fruits.sort();
 console.log("Classer par ordre aphabetique",fruits)//Question2

 fruits.push(`Kiwi`);
 console.log("Kiwi ajouter",fruits)//Question3

 fruits.splice(0,1);
 console.log("Apples supprimer",fruits)//Question4

 fruits.reverse();
 console.log("array au sens inverse",fruits)//Question5


 //Exercice2

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(moreFruits[1][1])
