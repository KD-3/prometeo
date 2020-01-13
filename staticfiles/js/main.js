(function ($) {

    
    /*------------------
        CountDown
    --------------------*/
    $("#countdown").countdown("2020/01/25", function(event) {
        $(this).html(event.strftime("<div class='cd-item'><span>%D</span> <p>Days</p> </div>" + "<div class='cd-item'><span>%H</span> <p>Hours</p> </div>" + "<div class='cd-item'><span>%M</span> <p>Minutes</p> </div>" + "<div class='cd-item'><span>%S</span> <p>Seconds</p> </div>"));
    });

    $("#countdown-2").countdown("2020/01/25 10:00:00", function(event) {
        $(this).html(event.strftime("<div class='cd-time'><span>%D</span> <p>Days</p> </div>" + "<div class='cd-time'><span>%H</span> <p>Hours</p> </div>" + "<div class='cd-time'><span>%M</span> <p>Minutes</p> </div>" + "<div class='cd-time'><span>%S</span> <p>Seconds</p> </div>"));
    });

    $("#countdown-3").countdown("2020/01/25 20:00:00", function(event) {
        $(this).html(event.strftime("<div class='cd-time'><span>%D</span> <p>Days</p> </div>" + "<div class='cd-time'><span>%H</span> <p>Hours</p> </div>" + "<div class='cd-time'><span>%M</span> <p>Minutes</p> </div>" + "<div class='cd-time'><span>%S</span> <p>Seconds</p> </div>"));
    });


})(jQuery);