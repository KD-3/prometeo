(function ($) {

    
    /*------------------
        CountDown
    --------------------*/
    $("#countdown .row").countdown("2020/01/23", function(event) {
        $(this).html(event.strftime(' \
            <div class="col-lg-3 col-md-3 col-sm-3 col-3 col-timer"> \
                <div class="card card-pricing bg-rose"><div class="card-body "> \
                    <h2 class="card-title">%D</h2> \
                    <p class="card-description"> \
                        Days \
                    </p> \
                    </div> \
                </div> \
            </div> \
            <div class="col-lg-3 col-md-3 col-sm-3 col-3 col-timer"> \
                <div class="card card-pricing bg-rose"><div class="card-body "> \
                    <h2 class="card-title">%H</h2> \
                    <p class="card-description"> \
                        Hours \
                    </p> \
                    </div> \
                </div> \
            </div> \
            <div class="col-lg-3 col-md-3 col-sm-3 col-3 col-timer"> \
                <div class="card card-pricing bg-rose"><div class="card-body "> \
                    <h2 class="card-title">%M</h2> \
                    <p class="card-description"> \
                        Minutes \
                    </p> \
                    </div> \
                </div> \
            </div> \
            <div class="col-lg-3 col-md-3 col-sm-3 col-3 col-timer"> \
                <div class="card card-pricing bg-rose"><div class="card-body "> \
                    <h2 class="card-title">%S</h2> \
                    <p class="card-description"> \
                        Seconds \
                    </p> \
                    </div> \
                </div> \
            </div> \
        '));
    });

    $("#countdown-2").countdown("2020/01/23 10:00:00", function(event) {
        $(this).html(event.strftime("<div class='cd-time'><span>%D</span> <p>Days</p> </div>" + "<div class='cd-time'><span>%H</span> <p>Hours</p> </div>" + "<div class='cd-time'><span>%M</span> <p>Minutes</p> </div>" + "<div class='cd-time'><span>%S</span> <p>Seconds</p> </div>"));
    });

    $("#countdown-3").countdown("2020/01/23 20:00:00", function(event) {
        $(this).html(event.strftime("<div class='cd-time'><span>%D</span> <p>Days</p> </div>" + "<div class='cd-time'><span>%H</span> <p>Hours</p> </div>" + "<div class='cd-time'><span>%M</span> <p>Minutes</p> </div>" + "<div class='cd-time'><span>%S</span> <p>Seconds</p> </div>"));
    });


})(jQuery);