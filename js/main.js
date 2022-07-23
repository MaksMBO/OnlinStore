function showLeftMenu() {
  document.getElementById("myDropdown__mobile").style.display = "block";
  document.body.style.overflow = 'hidden';
}

function showlogin() {
  document.getElementById("login").style.display = "flex";
  document.body.style.overflow = 'hidden';
}

window.onclick = function (event) {
  if (event.target.matches('.login')) {
    document.getElementById("login").style.display = "none";
    document.body.style.overflow = 'auto';
  }

  if (event.target.matches('.left__menu')) {
    document.getElementById("myDropdown__mobile").style.display = "none";
    document.body.style.overflow = 'auto';
  }
}

let buttonCatalog = document.querySelector("button.dropbtn");
let menu = document.querySelector("div.myDropdown")

buttonCatalog.addEventListener("mouseenter", function () {
  document.getElementById("myDropdown").classList.toggle("show");
});

function loginDisplayNone(email = "none", number = "block") {
  correct = ["block", "flex", "none"];
  if (typeof email === 'string' & typeof number === 'string' & correct.includes(email) & correct.includes(number)) {
    forEmail = Array.from(document.getElementsByClassName("login__email"));
    forNuber = Array.from(document.getElementsByClassName("login__number"));

    forEmail.forEach(element => element.style.display = email);
    forNuber.forEach(element => element.style.display = number);
  }
}

function showRegister() {
  document.getElementById("register__menu").style.display = "flex";
  document.getElementById("login__menu").style.display = "none";
}

function closeRegister() {
  document.getElementById("register__menu").style.display = "none";
  document.getElementById("login__menu").style.display = "flex";
}
