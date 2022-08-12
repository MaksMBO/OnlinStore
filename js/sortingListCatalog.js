window.onclick = function (event) {
  
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