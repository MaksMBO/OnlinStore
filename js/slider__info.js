$(document).ready(function () {

    $('.slider_nav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        // asNavFor: '.slider-products',
        dots: true,
        centerMode: true,
        focusOnSelect: true,
        vertical: true,
    });
});