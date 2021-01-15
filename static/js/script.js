$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });


// The following code was adapted from an answer found on stackoverflow. The solution was
// giving by Bakudan and later edited by LWC. Here is the original source:
// https://stackoverflow.com/questions/5517597/plain-count-up-timer-in-javascript

// HIDE TIMER, SHOW TIMER AND RESET TO 0

var sec = 0;
    function pad ( val ) { return val > 9 ? val : "0" + val; }
    setInterval( function(){
        if (running){
            sec ++}
        $("#seconds").html(pad(sec%60));
        $("#minutes").html(pad(parseInt(sec/60,10)));
    }, 1000);


var running = false

function turn_on(){
    running = true;
    sec = 0;
}

function currentlyWorking() {
    document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-briefcase"></i>  Working</h1>';
    turn_on();
}

function currentlySleeping() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-bed"></i>  Sleep</h1>';
  running = true;
  sec = 0;
}

function currentlyChildcaring() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-baby"></i>  Childcare</h1>';
      running = true;
    sec = 0;
}

function currentlyStudying() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-graduation-cap"></i>  Study</h1>';
      running = true;
    sec = 0;
}

function currentlyStrengthing() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-dumbbell"></i>  Strength</h1>';
}

function currentlyCardioing() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-running"></i>  Cardio</h1>';
}

function currentlyMusicing() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-guitar"></i>  Play Music</h1>';
}

function currentlyCleaning() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-soap"></i>  Cleaning</h1>';
}

function currentlyTraveling() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-compass"></i>  Travel</h1>';
}

function currentlyWatching() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-film"></i>  Watching</h1>';
}

function currentlyVideogaming() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-gamepad"></i>  Videogames</h1>';
}

function currentlyOthering() {
  document.getElementById("current_activity").innerHTML = '<h1 style="font-weight: 600;"><i class="fas fa-random"></i>  Other</h1>';
}
