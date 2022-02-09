const word="Developer".toUpperCase()
const wordLetters = word.split("")
const emptyLetters = new Array(word.length)
console.log( emptyLetters)
let turn =10
const lettersAlreadyUsed = []
function guestWordRender(){
	const display= []
	for (let index=0; index < emptyLetters.length; index++) {
		
			display.push('_')
		
	}
	console.log(display)
	let x =document.getElementById('emptyLetters')
	let tirets = display.join(' ')

	x.textContent = tirets
	console.log(x)
}
guestWordRender()

function render(){
	document.getElementById('turn').textContent=("Tour :" + turn)
	document.getElementById('lettersAlreadyUsed').textContent= "Lettres jouees : " + lettersAlreadyUsed
	guestWordRender()
	document.getElementById('selectedLetter').value = ""
}

function getAllIndex(myWord, mySelectedLetter){
	const indexes =[]
	for(let index=0; index< myWord.length; index++){
		
		if (myWord[index]=== mySelectedLetter) {
			element=myWord[index]
			indexes.push(element)
			wordLetters[index] = element
			console.log('youpii you found letter '+element )
			console.log(wordLetters)
		}
	}

	return indexes
}

function selectedLetter(){
	let letter = document.getElementById('selectedLetter').value
	console.log(letter)
	letter = letter.trim()
	let mySelectedLetter = letter[0].toUpperCase()
	lettersAlreadyUsed.push(mySelectedLetter)
	const temp = getAllIndex(wordLetters, mySelectedLetter)
	if (temp.length === 0) {
		turn--
	}else{
		console.log(temp)
		for(let index=0; index<temp.length;index++){
			emptyLetters[temp[index]]-wordLetters[temp[index]]
			wordLetters[temp[index]]=""
			console.log(wordLetters)
		}
	}
	render()
	if (turn === 0) {
		alert('LOSE')
	}
	if (wordLetters.every((el)=> el === "")) {
		alert('WIN')
	}
}
onload = function(){
	
}
render()
