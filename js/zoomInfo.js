function zoom(receivedIMG, placeIMG, placeIMGId) {
    let allLinks = document.querySelector(receivedIMG);
    let linkIMG = allLinks.getAttribute('src');
   
    $(placeIMG).html(`<div class='test position-absolute'><img src='${linkIMG}'class= 'full-image'></div >`);
     document.getElementById(`${placeIMGId}`).style.display = "block";
}

function zoomLeave(placeIMG) {
    document.getElementById(`${placeIMG}`).style.display = "none";
}
