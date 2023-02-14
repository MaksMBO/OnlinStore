$(document).ready(function(){   
    BinHide(false);
});

function BinShow(){
    var inp = document.getElementById("bin");
    inp.style.opacity = '1';
    document.getElementById("bin").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    document.getElementById("bin").style.visibility = "inherit";
    document.getElementById("bin").style.zIndex = 200;
    $("body").css("overflow","hidden"); 
}

function BinHide(second=true){
    console.log("suka");
    var inp = document.getElementById("bin");
    inp.style.opacity = '0';
    if (second) {
       document.getElementById("bin").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s"; 
    }
    document.getElementById("bin").style.visibility = "hidden";
    document.getElementById("bin").style.zIndex = 0;
    $("body").css("overflow","auto");
}

function BinDell(){
    var inp = document.getElementById("bin");
    console.log("dell");
    inp.style.opacity = '1';
    document.getElementById("bin").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    document.getElementById("bin").style.visibility = "inherit";
    document.getElementById("bin").style.zIndex = 200;
}