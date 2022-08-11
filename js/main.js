function showLeftMenu() {
  document.getElementById("myDropdown__mobile").style.display = "block";
  document.body.style.overflow = 'hidden';
}

function showlogin() {
  document.getElementById("login").style.display = "flex";
  document.getElementById("login__menu").style.display = "flex";
  document.body.style.overflow = 'hidden';
  setTimeout(animation, 0.1, "login__menu", "login__menu-active");
}

window.onclick = function (event) {
  if (event.target.matches('.login')) {
    document.getElementById("login").style.display = "none";
    document.getElementById("register__menu").style.display = "none";
    document.getElementById("login__menu").style.display = "none";
    document.body.style.overflow = 'auto';
    document.getElementById("register__menu").classList.remove("register__menu-active");
    document.getElementById("login__menu").classList.remove("login__menu-active");

  }

  if (event.target.matches('.left__menu')) {
    document.getElementById("myDropdown__mobile").style.display = "none";
    document.body.style.overflow = 'auto';
  }

  if (event.target.matches('.catalog__mobile') || event.target.matches('.catalog__mobile img[alt="exit"]')) {
    document.getElementById("catalog__mobile").style.display = "none";
    document.getElementById("catalog__mobile__all").classList.remove("catalog__mobile__all-active");
  }

  if (document.getElementById("sorting__list").style.display === "block" && !event.target.matches('.sorting__list')
    && !event.target.matches('.sorting__list ul') && !event.target.matches('.sorting__list ul a') &&
    !event.target.matches('.sorting__list ul a li')) {
    document.getElementById("sorting__list").style.display = "none";
    document.getElementById('sorting__svg').style.transform = "rotate(0)";
  }

  else if (event.target.matches('.sorting__filter p') || event.target.matches('.sorting__menu .sorting__svg')) {
    document.getElementById("sorting__list").style.display = "block";
    document.getElementById('sorting__svg').style.transform = "rotate(180deg)";
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
  setTimeout(animation, 0.1, "register__menu", "register__menu-active");
}

function closeRegister() {
  document.getElementById("register__menu").style.display = "none";
  document.getElementById("login__menu").style.display = "flex";
  setTimeout(animation, 0.1, "login__menu", "login__menu-active");
}

function showMobileCatalog() {
  document.getElementById("catalog__mobile").style.display = "flex";
  setTimeout(animation, 0.1, "catalog__mobile__all", "catalog__mobile__all-active");
}

function animation(id, toggleAtr) {
  document.getElementById(id).classList.add(toggleAtr);
}
