const headerUpDown = () => {
  window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
    if (currentScrollPos <= 40) {
      document.getElementById("header").style.top = "40px";
    } else {
      document.getElementById("header").style.top = "0px";
    }
    prevScrollpos = currentScrollPos;
  }
}

headerUpDown()

document.getElementsByClassName("close-link")[0].addEventListener("click", closeWarning);

const closeWarning = () => {
  document.getElementsByClassName('close-link').style.top = "-20px";
}