function headerUpDown() {
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

function closeWarning() {
  document.getElementsByClassName('warning')[0].style.display = "none";
  document.getElementById("header").style.top = "0px";
  localStorage.setItem('warning-closed', 'warning-closed')
}

(() => {
  if (localStorage.getItem('warning-closed')) {
    document.getElementsByClassName('warning')[0].style.display = "none";
    document.getElementById("header").style.top = "0px";
  }
})()

// TODO Votar nesse desgraça
// const img = document.getElementsByClassName('img-text-quetinho')[0]

// if ($(window).innerWidth() == 1750) {
//   console.log($(window).innerWidth())
//   img.style.right = ' px'.replace(' ', 300 - 33)
// }
  

headerUpDown()

document.getElementsByClassName("close-link")[0].addEventListener("click", closeWarning);

