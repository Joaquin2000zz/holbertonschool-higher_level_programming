const header = document.querySelector('#add_item');

header.addEventListener('click', changeColor);
function changeColor() {
  $('.my_list').append('<li>Item')
}