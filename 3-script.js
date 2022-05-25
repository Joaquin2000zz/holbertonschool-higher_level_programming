const header = document.querySelector('#red_header');

header.addEventListener('click', changeColor);
function changeColor() {
  $('header').addClass('red')  
}