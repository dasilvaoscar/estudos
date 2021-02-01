const headerUpDown = () => {
  window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
    if (document.getElementsByClassName('warning')[0].style.display != 'none') {
      if (currentScrollPos <= 40) {
        document.getElementById("header").style.top = "40px";
      } else {
        document.getElementById("header").style.top = "0px";
      }
      prevScrollpos = currentScrollPos;
    }
  }
}

const closeWarning = () => {
  document.getElementsByClassName('warning')[0].style.display = "none";
  document.getElementById("header").style.top = "0px";
  coc
}

headerUpDown()

document.getElementsByClassName("close-link")[0].addEventListener("click", closeWarning);

