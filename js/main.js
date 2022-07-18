function showLeftMenu() {
  document.getElementById("myDropdown__mobile").style.display = "block";
  document.body.style.overflow = 'hidden';
}

window.onclick = function (event) {
  if (!event.target.matches('.dropdown-content__mobile') & !event.target.matches('.dropbtn__mobile') & !event.target.matches('.dropbtn__img')) {
    document.getElementById("myDropdown__mobile").style.display = "none";
    document.body.style.overflow = 'auto';
  }
}

let buttonCatalog = document.querySelector("button.dropbtn");
let menu = document.querySelector("div.myDropdown")

buttonCatalog.addEventListener("mouseenter", function () {
  document.getElementById("myDropdown").classList.toggle("show");
});

