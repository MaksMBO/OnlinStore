
function zoom(receivedIMG, placeIMG) {
    let allLinks = document.querySelector(receivedIMG);
    let linkIMG = allLinks.getAttribute('src');

    $(placeIMG).html(`<div class='test position-absolute'><img src='${linkIMG}'class= 'full-image'></div >`);
}
