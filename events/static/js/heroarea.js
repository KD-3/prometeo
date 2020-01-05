window.setInterval(function(){
    var heroarea = document.querySelector(".hero-area.set-bg .container"); 
    var msgCount = document.getElementsByClassName('alert').length;
    var heading = document.querySelector(".hero-text h2");
    var title = document.querySelector(".logo h2");
    if (document.documentElement.clientWidth < 748) {
        heroarea.style.paddingTop = "0px";
    }
    else if (document.documentElement.clientWidth < 788) {
        heroarea.style.paddingTop = msgCount*45 + 75 + "px";
    } 
    else if (document.documentElement.clientWidth <= 1046) {
        heroarea.style.paddingTop = msgCount*45 + 30 + "px";
    } 
    else {
        heroarea.style.paddingTop = msgCount*45 + "px";
    }
    if(document.documentElement.clientWidth < 490) {
        heading.style.fontSize = "15vw";
    } else {
        heading.style.fontSize = "80px";
    }
    if(document.documentElement.clientWidth < 410) {
        title.style.fontSize = "7vw";
    } else {
        title.style.fontSize = "40px";
    }
  }, 1);


