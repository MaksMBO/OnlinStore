showMore('.checkbox__brands .hidden', '.checkbox__brands div.box', 'show__more__mobile', 'close__mobile',
    'more__SVG__mobile', '.brands__mobile');

showMore('.checkbox__builtIn__memoryMobile .hidden', '.checkbox__builtIn__memoryMobile div.box', 'show__more__builtIn__memoryMobile',
    'close__builtIn__memoryMobile', 'more__SVG__builtIn__memoryMobile', '.builtIn__memoryMobile');

showMore('.checkbox__RAMmobile .hidden', '.checkbox__RAMmobile div.box', 'show__more__RAMmobile', 'close__RAMmobile',
    'more__SVG__RAMmobile', '.RAMmobile');

showMore('.checkbox__screenType__mobile .hidden', '.checkbox__screenType__mobile div.box', 'show__more__screenType__mobile',
    'close__screenType__mobile', 'more__SVG__screenType__mobile', '.screenType__mobile');

showMore('.checkbox__mobile__processor .hidden', '.checkbox__mobile__processor div.box', 'show__more__mobile__processor',
    'close__mobile__processor', 'more__SVG__mobile__processor', '.mobile__processor');

showMore('.checkbox__screen__resolution .hidden', '.checkbox__screen__resolution div.box', 'show__more__screen__resolution',
    'close__screen__resolution', 'more__SVG__screen__resolution', '.screen__resolution');


function showMore(hidenBlock, unhiddenBlock, open, close, more__SVG, mostObject) {
    var more = document.querySelectorAll(mostObject);
    var show__more = document.getElementById(open);
    var closer = document.getElementById(close);
    var svgElement = document.getElementById(more__SVG);

    for (var i = 0; i < more.length; i++) {
        more[i].addEventListener('click', function () {
            var hidden = this.parentNode.querySelectorAll(hidenBlock);
            var unhidden = this.parentNode.querySelectorAll(unhiddenBlock);

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
}