$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

// The following code was adapted from an answer found on stackoverflow. The solution was
// giving by Bakudan and later edited by LWC. Here is the original source:
// https://stackoverflow.com/questions/5517597/plain-count-up-timer-in-javascript

var sec = 0;
    function pad ( val ) { return val > 9 ? val : "0" + val; }
    setInterval( function(){
        $("#seconds").html(pad(++sec%60));
        $("#minutes").html(pad(parseInt(sec/60,10)));
    }, 1000);