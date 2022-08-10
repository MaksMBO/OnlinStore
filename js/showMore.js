var more = document.querySelectorAll('.more');
var show__more = document.getElementById('show__more');
var closer = document.getElementById('close');
var svgElement = document.getElementById('more__SVG');

for (var i = 0; i < more.length; i++) {
    more[i].addEventListener('click', function () {
        var hidden = this.parentNode.querySelectorAll('div.hidden');
        var unhidden = this.parentNode.querySelectorAll('div.box');

        var showPerClick = hidden.length;
        var hideClich = unhidden.length;

        if (hideClich) {
            show__more.style.display = "block";
            closer.style.display = "none";
            svgElement.style.transform = "rotate(0)";
            for (var i = 0; i < hideClich; i++) {
                unhidden[i].classList.add('hidden');
                unhidden[i].classList.remove('box');
            }
        }
        else {
            show__more.style.display = "none";
            closer.style.display = "block";
            svgElement.style.transform = "rotate(180deg)";
            for (var i = 0; i < showPerClick; i++) {
                if (!hidden[i]) return this.outerHTML = "";
                hidden[i].classList.add('box');
                hidden[i].classList.remove('hidden');
            }
        }
    });
}