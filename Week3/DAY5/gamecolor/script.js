
for(let i=0; i<1440; i++){

	let divs= document.createElement('div');
	document.getElementById('box').appendChild(divs)

}
let mousedown = false;
let couleur = null;
let body = document.getElementsByTagName("body")[0];
let bloc_couleur = document.querySelectorAll('#sidebar> *');
let bloc_remplissages = document.querySelectorAll('#box> *');
let clear_button = document.getElementsByTagName("button")[0];

clear_button.addEventListener("click", function(){
    for (bloc_remplissage of bloc_remplissages){
        bloc_remplissage.style.backgroundColor = "white";
    }
});

body.addEventListener("mousedown", function(){
    mousedown = true;
})

body.addEventListener("mouseup", function(){
    mousedown = false;
})

for (bloc_couleurs of bloc_couleur){
    bloc_couleurs.addEventListener("click", function(event){
        couleur = event.target.style.backgroundColor;
        console.log(couleur)
    });
}

for (bloc_remplissage of bloc_remplissages){
    bloc_remplissage.addEventListener("mousedown", function(event){
        if (couleur != null) event.target.style.backgroundColor = couleur;
    });
    bloc_remplissage.addEventListener("mouseover", function(event){
        if ( mousedown && couleur != null) event.target.style.backgroundColor = couleur;
    });
}

	