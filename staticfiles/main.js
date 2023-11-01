const $counter = document.querySelector('.counter')
let i = 0;

function counter() {
  i++
  $counter.textContent = i;
}

document.querySelector('.button').addEventListener("click", counter)