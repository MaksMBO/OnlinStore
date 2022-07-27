$(document).ready(function () {

    $('.slider_nav').slick({
        focusOnSelect: true,
        vertical: true,
        arrows: false,
        adaptiveHeight: true,
        slidesToShow: 7,
        asNavFor: ".slider_nav_big",
    });

    $('.slider_nav_big').slick({
        arrows: false,
        fade: true,
        asNavFor: ".slider_nav",
        draggable: false,
        waitForAnimate: false,
    })
});