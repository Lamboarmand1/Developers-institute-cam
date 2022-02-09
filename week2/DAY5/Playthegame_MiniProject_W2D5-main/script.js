function playTheGame(){
	let Question1 = confirm("Tu Veux Jouer Mon Amie");
	if (Question1== false) {
		alert("Bye bye mon amie")
	}
	else{
	let userNumber= parseInt(prompt("Entre un numero mon amie"));
	
		if (isNaN(userNumber)) {
			alert("Desoler mon amie tu n'as pas saisir de nombre bye bye")
		}
		else if (userNumber>10 || userNumber<0){
			alert("Hollalla! mon amie C'est pas un bon chiffre bye bye")
		}
		else{
			let computerNumber = Math.round(Math.random()*10);
			test()
		}
		
	}
}
playTheGame()

function test(userNumber,computerNumber){
	if (userNumber == computerNumber) {
		alert("Felicitation mon amie")
	}
	else if (userNumber > computerNumber) {
		alert("Mon amie ton numéro est plus grand que celui de l'ordinateur, devinez à nouveau")
		prompt("Entre un numero mon amie")
	}
	else if (userNumber < computerNumber) {
		alert("Mon amie ton numéro est plus petit que celui de l'ordinateur, devinez à nouveau")
	}
	else{
		alert("hors de chance")
	}

}

 