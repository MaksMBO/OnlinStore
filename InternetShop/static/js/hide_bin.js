$(document).ready(function(){   
    BinHide(false);
});

function BinShow(){
    var inp = document.getElementById("bin");
    inp.style.opacity = '1';
    document.getElementById("bin").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    document.getElementById("bin").style.visibility = "inherit";
    $("body").css("overflow","hidden"); 
}

function BinHide(second=true){
    var inp = document.getElementById("bin");
    inp.style.opacity = '0';
    if (second) {
       document.getElementById("bin").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s"; 
    }
    document.getElementById("bin").style.visibility = "hidden";
    $("body").css("overflow","auto");
}