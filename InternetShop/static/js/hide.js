$(document).ready(function(){   
    setTimeout(hideError, 10000, "error");
    setTimeout(hideError, 10000, "success");
});

function hideError(elem_id) {
    elem = document.getElementById(elem_id);
    elem.style.display = "none";
}