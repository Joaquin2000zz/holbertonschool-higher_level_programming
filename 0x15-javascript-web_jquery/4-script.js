const header = document.querySelector('#toggle_header');

header.addEventListener('click', changeColor);
function changeColor() {
  $('header').toggleClass('red green')  
}