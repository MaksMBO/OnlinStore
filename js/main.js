function showLeftMenu() {
  document.getElementById("myDropdown__mobile").style.display = "block";
  document.body.style.overflow = 'hidden';
}

function showlogin() {
  document.getElementById("login").style.display = "flex";
  document.getElementById("login__menu").style.display = "flex";
  document.body.style.overflow = 'hidden';
}

window.onclick = function (event) {
  if (event.target.matches('.login')) {
    document.getElementById("login").style.display = "none";
    document.getElementById("register__menu").style.display = "none";
    document.getElementById("login__menu").style.display = "none";
    document.body.style.overflow = 'auto';
  }

  if (event.target.matches('.left__menu')) {
    document.getElementById("myDropdown__mobile").style.display = "none";
    document.body.style.overflow = 'auto';
  }

  if (event.target.matches('.catalog__mobile') || event.target.matches('.catalog__mobile img[alt="exit"]')) {
    document.getElementById("catalog__mobile").style.display = "none";
    document.getElementById("catalog__mobile__all").classList.toggle("catalog__mobile__all-active");
  }

}

let buttonCatalog = document.querySelector("button.dropbtn");

buttonCatalog.addEventListener("mouseenter", function () {
  document.getElementById("myDropdown").classList.toggle("show");
  document.getElementById("header__background").classList.toggle("show");
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
  document.getElementById("login").style.display = "flex";
  document.getElementById("register__menu").style.display = "flex";
  document.getElementById("login__menu").style.display = "none";
}

function closeRegister() {
  document.getElementById("register__menu").style.display = "none";
  document.getElementById("login__menu").style.display = "flex";
}

function showMobileCatalog() {
  document.getElementById("catalog__mobile").style.display = "flex";
  setTimeout(animationCatalog, 0.1);
}

function animationCatalog() {
  document.getElementById("catalog__mobile__all").classList.toggle("catalog__mobile__all-active");
}