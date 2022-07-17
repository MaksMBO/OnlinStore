// function myFunction() {
//     document.getElementById("myDropdown").classList.toggle("show");
// }

// window.onclick = function(event) {
//   if (!event.target.matches('.dropbtn') & !event.target.matches('.dropbtn__img') & !event.target.matches('.dropbtn__span')) {

//   var dropdowns = document.getElementsByClassName("dropdown-content");
//   var i;
//   for (i = 0; i < dropdowns.length; i++) {
//     var openDropdown = dropdowns[i];
//     if (openDropdown.classList.contains('show')) {
//       openDropdown.classList.remove('show');
//     }
//   }
// }
// }


let buttonCatalog = document.querySelector("button.dropbtn");
let menu = document.querySelector("div.myDropdown")

buttonCatalog.addEventListener("mouseenter", function () {
  document.getElementById("myDropdown").classList.toggle("show");
});

