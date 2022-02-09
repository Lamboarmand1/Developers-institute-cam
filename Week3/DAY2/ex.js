//EXO1
//1-En cliquant sur le bouton, la police, la taille de la police et la couleur du texte du paragraphe seront modifiées

// function js_style(){
// 	text.style.fontSize="14px";
// 	text.style.fontFamily="arial";
// 	text.style.color="skyblue";
// 	text.style.backgroundColor="black";
// 	jsstyle.style.fontSize="14px";
// 	jsstyle.style.fontFamily="arial";
// 	jsstyle.style.color="skyblue";
// 	jsstyle.style.backgroundColor="black";
// }

//EXO2
// 1-Écrivez une fonction JavaScript pour obtenir les valeurs du prénom et du nom de la forme suivante.
// function getFormvalue(){
// 	let x=document.getElementById("form1");
// 	for (let i=0;i<x.length;i++) {
// 		if (x.elements[i].value!='Submit') {
// 			console.log(x.elements[i].value);
// 		}
// 	}
// }

//EXO3

// 1-Ecrivez un programme JavaScript pour définir la couleur d'arrière-plan d'un paragraphe.

// function set_background() {
//  docBody = document.getElementsByTagName("body")[0];
//   //Get all the p elements that are descendants of the body
//   myBodyElements = docBody.getElementsByTagName("p");
// // get the first p elements
//   myp1 = myBodyElements[0];
//   myp1.style.background = "red";
// // get the second p elements
//   myp2 = myBodyElements[1];
//   myp2.style.background = "rgb(255,255,0)";
// }

//EXO4

// 1-Écrivez une fonction JavaScript pour obtenir la valeur des attributs href, hreflang, rel, target et type du lien spécifié

// function getAttributes()
// {
//  let u = document.getElementById("w3r").href;
//  alert('The value of the href attribute of the link is : '+u);
//  let v = document.getElementById("w3r").hreflang;   
//  alert('The value of the hreflang attribute of the link is : '+v);
//  let w = document.getElementById("w3r").rel; 
//   alert('The value of the rel attribute of the link is : '+w);
//  let x = document.getElementById("w3r").target; 
//   alert('The value of the taget attribute of the link is : '+x);
//  let y = document.getElementById("w3r").type; 
//   alert('The value of the type attribute of the link is : '+y);  
// }

//EXO5

// 1-Écrivez une fonction JavaScript pour ajouter des lignes à une table

// function insert_Row()
// {
// var x=document.getElementById('sampleTable').insertRow(0);
// var y = x.insertCell(0);
// var z = x.insertCell(1);
// y.innerHTML="New Cell1";
// z.innerHTML="New Cell2";
// }

//EXO6

//1-Écrivez une fonction JavaScript qui accepte la ligne, la colonne (pour identifier une cellule particulière) et une chaîne pour mettre à jour le contenu de cette cellule.

// function changeContent()
// {
// rn = window.prompt("Input the Row number(0,1,2)", "0");
// cn = window.prompt("Input the Column number(0,1)","0");
// content = window.prompt("Input the Cell content");  
// var x=document.getElementById('myTable').rows[parseInt(rn,10)].cells;
// x[parseInt(cn,10)].innerHTML=content;
// }

//EXO7

// 1-Écrivez une fonction JavaScript qui crée un tableau, accepte les numéros de ligne et de colonne de l'utilisateur et saisit le numéro de ligne-colonne comme contenu (par exemple, ligne-0 colonne-0) d'une cellule.
// function createTable()
// {
// rn = window.prompt("Input number of rows", 1);
// cn = window.prompt("Input number of columns",1);
  
//  for(var r=0;r<parseInt(rn,10);r++)
//   {
//    var x=document.getElementById('myTable').insertRow(r);
//    for(var c=0;c<parseInt(cn,10);c++)  
//     {
//      var y=  x.insertCell(c);
//      y.innerHTML="Row-"+r+" Column-"+c; 
//     }
//    }
// }

//EXO8

// 1-Écrivez un programme JavaScript pour supprimer des éléments d une liste déroulante.
// function removecolor()
// {
// var x=document.getElementById("colorSelect");
// x.remove(x.selectedIndex);
// }

//EXO9
// 1-Ecrivez un programme JavaScript pour compter et afficher les éléments d'une liste déroulante, dans une fenêtre d'alerte. 


// function getOptions()
// {
// var x=document.getElementById("mySelect");
// var txt1 = "No. of items : ";
// var i;
// l=document.getElementById("mySelect").length;  
// txt1 = txt1+l;
// for (i=0;i<x.length;i++)
//   {
//     txt1 = txt1 + "\n" + x.options[i].text;
//   }
// alert(txt1);
// }

//EX10

// function volume_sphere()
//  {
//   var volume;
//   var radius = document.getElementById('radius').value;
//   radius = Math.abs(radius);
//   volume = (4/3) * Math.PI * Math.pow(radius, 3);
//   volume = volume.toFixed(4);
//   document.getElementById('volume').value = volume;
//   return false;
//  } 
// window.onload = document.getElementById('MyForm').onsubmit = volume_sphere;

// EXO11
// 1-Ecrivez un programme JavaScript pour afficher une image aléatoire (en cliquant sur un bouton) de la liste suivante.

// function display_random_image() 
// {
//      var theImages = [{
//         src: "http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg",
//         width: "240",
//         height: "160"
//     }, {
//         src: "http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg",
//         width: "320",
//         height: "195"
//     }, {
//         src: "http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg",
//         width: "500",
//         height: "343"
//     }];
    
//     var preBuffer = [];
//     for (var i = 0, j = theImages.length; i < j; i++) {
//         preBuffer[i] = new Image();
//         preBuffer[i].src = theImages[i].src;
//         preBuffer[i].width = theImages[i].width;
//         preBuffer[i].height = theImages[i].height;
//     }
   
// // create random image number
//   function getRandomInt(min,max) 
//     {
//       //  return Math.floor(Math.random() * (max - min + 1)) + min;
    
// imn = Math.floor(Math.random() * (max - min + 1)) + min;
//     return preBuffer[imn];
//     }  

// // 0 is first image,   preBuffer.length - 1) is  last image
  
// var newImage = getRandomInt(0, preBuffer.length - 1);
 
// // remove the previous images
// var images = document.getElementsByTagName('img');
// var l = images.length;
// for (var p = 0; p < l; p++) {
//     images[0].parentNode.removeChild(images[0]);
// }
// // display the image  
// document.body.appendChild(newImage);
// }

//EXO12

// 1-Ecrivez un programme JavaScript pour mettre en évidence les mots en gras du paragraphe suivant, en passant la souris sur un certain lien. 
//First create a list of all bold items 
// var bold_Items;
// window.onload = getBold_items();
 
// // Collect all <strong> tags
// function getBold_items() 
// {
//   bold_Items = document.getElementsByTagName('strong'); 
// }
// // iterate all bold tags and change color  
// function highlight() 
// {
//    for (var i=0; i<bold_Items.length; i++)
//    {                                                    
//     bold_Items[i].style.color = "green";
//     }
// }

// // On mouse out highlighted words become black
// function return_normal()
// {
//   for (var i=0; i<bold_Items.length; i++) 
//   {
//        bold_Items[i].style.color = "black";
//   }
// }

//EXO13

// 1-Ecrivez un programme JavaScript pour obtenir la largeur et la hauteur de la fenêtre (à chaque fois que la fenêtre est redimensionnée).

// function getSize()
// {
// var w = document.documentElement.clientWidth;
// var h = document.documentElement.clientHeight;
        
// // put the result into a h1 tag
//  document.getElementById('wh').innerHTML = "<h1>Width: " + w + " â€¢ Height: " + h + "</h1>";
// }





//exo15

 function madLibs() {
      let storyDiv = document.getElementById("story");
      let name = document.getElementById("name").value;
      let adjective = document.getElementById("adjective").value;
      let noun = document.getElementById("noun").value;
      let verb = document.getElementById("verb");
      let place = document.getElementById("place");
      storyDiv.innerHTML = name + " est une personne " + adjective + " et " + noun + "suis" + verb + "à" + place;
    }

    let libButton = document.getElementById('lib-button');
    libButton.addEventListener('click', madLibs);