$(document).ready(function () {
    // $('.slider-products').slick({
    //     slidesToShow: 1,
    //     slidesToScroll: 1,
    //     arrows: false,
    //     fade: true,
    //     asNavFor: '.slider-nav'
    // });
    $('.slider-nav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        // asNavFor: '.slider-products',
        dots: true,
        centerMode: true,
        focusOnSelect: true,
        vertical: true,
    });
});