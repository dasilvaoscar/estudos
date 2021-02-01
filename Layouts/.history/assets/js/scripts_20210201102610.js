const headerUpDown = () => {
  window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
    if (document.getElementsByClassName('warning')[0].style.display !=) {

    }
    
  }
}

headerUpDown()

const closeWarning = () => {
  document.getElementsByClassName('warning')[0].style.display = "none";
}

document.getElementsByClassName("close-link")[0].addEventListener("click", closeWarning);

