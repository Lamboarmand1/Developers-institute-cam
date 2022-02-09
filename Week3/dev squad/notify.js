let nofication =[ ];


let s = document.getElementById("notify")
 	s.addEventListener("click", show())

function show(){

 	
 	document.write("The items below were requested")
 	document.write(nofication)

 }

 	
let p = document.getElementById("phone")
	p.addEventListener("click", iphone13)
 

 function iphone13(){
 
 	let i =document.getElementById("ph").innerHTML
 	nofication.push(i)
 	alert("this item is added to the list of commads")
    document.getElementById("checkout_items").innerHTML = nofication.length
   alert( "the new number of notification is  " +nofication.length)
 }

   
let c = document.getElementById('cas')
  c.addEventListener("click", casq)  

function casq(){
let t = document.getElementById("ca").innerHTML;  	
nofication.push(t)
  	alert('this item has been added')
document.getElementById("checkout_items").innerHTML = nofication.length
	alert( "the new number of notification is  " +nofication.length)
  }

 
 