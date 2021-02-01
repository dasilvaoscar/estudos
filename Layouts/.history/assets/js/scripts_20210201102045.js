var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (currentScrollPos <= 40) {
    document.getElementById("header").style.top = "40px";
  } else {
    document.getElementById("header").style.top = "0px";
  }
  prevScrollpos = currentScrollPos;
}

const sc