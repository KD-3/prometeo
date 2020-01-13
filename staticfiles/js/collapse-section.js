function showType(type) {
    var i, tabcontent;
    tabcontent = document.getElementsByClassName("category");

    if(document.getElementById(type).style.display != "none") {
        document.getElementById(type).style.display = "none";
    } else {
        for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        }
        
        document.getElementById(type).style.display = "flex";
    }

  }