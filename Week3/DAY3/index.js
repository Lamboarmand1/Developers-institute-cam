function myMove() {
  let element = document.getElementById("animate");
  let deplacement = 0;
  let id = setInterval(function() {
    if (deplacement == 350) {
      // clearInterval(id);
    }
    else {
      deplacement++;
      element.style.right = deplacement + "px";
      element.style.left = deplacement + "px";
    }
  }, );
}
