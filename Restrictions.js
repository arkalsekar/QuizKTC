// Disable Hot Keys
document.onkeydown = function (e) {
        return false;
}

// Disable right click 
document.addEventListener('contextmenu', event => event.preventDefault());


// Detect Tab change
document.addEventListener("visibilitychange", (event) => {
  if (document.visibilityState == "visible") {
    console.log("tab is active")
  } else {
    console.log("tab is inactive")
  }
});

// Detect Application Change
document.addEventListener("visibilitychange", function() {
  console.log(document.hidden, document.visibilityState);
}, false);

// or this can also be used for the detect of application change
window.addEventListener('blur', function(){
   console.log('blur');
}, false);

window.addEventListener('focus', function(){
   console.log('focus');
}, false);

// Enforce FUll Screen
function enterFullScreen() {
  let elem = document.documentElement;
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.mozRequestFullScreen) { // Firefox
    elem.mozRequestFullScreen();
  } else if (elem.webkitRequestFullscreen) { // Chrome, Safari and Opera
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { // IE/Edge
    elem.msRequestFullscreen();
  }
}

document.addEventListener("fullscreenchange", function() {
  if (!document.fullscreenElement) {
    console.log("User exited full screen");
    // You can alert the user or terminate the exam session here
  }
});


// Web cam access
navigator.mediaDevices.getUserMedia({ video: true })
  .then(function(stream) {
    // Display video on the page or send it to a server for monitoring
    let videoElement = document.querySelector('video');
    videoElement.srcObject = stream;
  })
  .catch(function(err) {
    console.error("Webcam access denied:", err);
  });

// Prevent copy and paste
navigator.mediaDevices.getUserMedia({ video: true })
  .then(function(stream) {
    // Display video on the page or send it to a server for monitoring
    let videoElement = document.querySelector('video');
    videoElement.srcObject = stream;
    video.addEventListener("loadedmetadata", () => {
      video.play();
  });
  })
  .catch(function(err) {
    console.error("Webcam access denied:", err);
  });

// Timer and auto submit
let examDuration = 3600; // In seconds (1 hour)
setInterval(function() {
  if (examDuration > 0) {
    examDuration--;
    console.log("Time remaining: ", examDuration);
    // Update UI timer display
  } else {
    alert("Time's up! Submitting the exam.");
    document.getElementById('exam-form').submit();
  }
}, 1000);
