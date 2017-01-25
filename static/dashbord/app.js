function startCountdown(liftoffTime) {
    $('#timer').countdown({until: liftoffTime, 
            compact: true,
            layout: '{hnn}{sep}{mnn}{sep}{snn}',
            onExpiry: expirSignal
    });
}

function expirSignal(){
    var html = "<div class='alert alert-danger'>"+
            "<button type='button' class='close' data-dismiss='alert' aria-hidden='true'></button>"+
            '<h3><i class="fa fa-bullhorn fa-dcustom"></i> Awaiting Signal...</h3>'+ 
            '</div>'
    $('#active-signal').html(html)
}
