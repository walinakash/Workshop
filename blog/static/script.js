/**
 * Created by User on 7/23/2017.
 */
function adjustStyle() {
    var width = 0;
    if(window.innerHeight){
        width = window.innerWidth;

    }else if(document.documentElement && document.documentElement.cleintHeight){
        width = document.documentElement.clientWidth;
    }else if(document.body){
        width = document.body.clientWidth;
    }
    if (width < 1000){
        document.getElementById("image").setAttribute("src", "static/img/subNav_accent.png");
        document.getElementById("style").setAttribute("href","static/css/simple.css");

    }else{
        document.getElementById("image").setAttribute("src", "static/img/django.jpg");
        document.getElementById("style").setAttribute("href", "static/css/style.css");
    }
}

//now call it when the windo is resizrd
window.onresize = function () {
    adjustStyle();

};
window.onload = function () {
    adjustStyle();
}