const header = document.querySelector('#red_header');

header.addEventListener('click', changeColor);

function changeColor() {
  $("#red_header").css("color", "#FF0000")
}