let main = document.querySelector("body > div > main.px-3.startmessage");
let intro = document.getElementById('intro');
let start = document.getElementById('Start');
let go = document.getElementById('sendform');
// let restart = document.getElementById('restart');
let body = document.querySelector("body");
let form = document.getElementsByClassName('nameform')[0];
// let popup = document.getElementsByClassName('popup')[0];

var showform = function () {
    body.style.transition = "2s ease-out";
    main.style.opacity = 0;
    // intro.style.opacity = 0; 
    main.style.visibility = "hidden"; 
    setTimeout(function(){ 
        body.style.backgroundImage = "url('./static/images/ghana\ kids\ 1.jpg')";
    }, 1500);



    // setTimeout(function(){ 

        
    // }, 500);
    
    setTimeout(function(){ 
        intro.style.display = "none";
        main.style.visibility = "visible"
        main.style.opacity = 1;
        form.style.opacity = 1;
        form.style.visibility = "visible";
        form.style.display = "block"; 
        intro.style.display = "none";
    }, 3000)

};

// var showresults = function() {
//     setTimeout(function(){
//         popup.style.visibility = "visible"

//     }, 2000)

//     setTimeout(function(){ 
//         body.style.backgroundImage = "url('./static/images/ghana\ kids\ 2.jpg')";
//     }, 1500);
// };

start.addEventListener('click', showform);
