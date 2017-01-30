
$(document).on("click",'#authorize-binary', function(e){
    console.log(window['binary-live-api']);
    const { oauthUrl, parseOAuthResponse } = window['binary-live-api'].OAuth;
    const url = oauthUrl('2569');
    window.location = url;

})



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

function updateBalance(balance,currency,url){
    $.ajax({
        url: url,
        'data':{'balance':balance,'currency':currency},
        'type':'POST',
        success: function(result){
            console.log(result)
        }
});
}

 function activeTrade(){
    $("#active-trade tbody tr").remove()
    api.getPortfolio().then(response =>{
            $.each(response.portfolio.contracts, function(i, item){
                if(item.contract_type == 'PUT'){
                    type = '<td><i class="fa fa-caret-down color-red"></i></td>'
                }else{
                    type = '<td><i class="fa fa-caret-up color-blue"></i></td>'
                }
                purchase_time = new Date (item.purchase_time*1000)

            html =  '<tr id="'+item.contract_id+'">'+
                    '<td><span class="label label-important "'+item.symbol+'>'+item.symbol+'</span></td>'+
                    '<td>'+ item.buy_price+'</td>'+type+
                    '<td class="open-tick">'+ 1.31352 +'</td>'+
                    '<td class="current-tick '+item.symbol+'">'+ 1.13120 +'</td>'+
                    '<td>'+ purchase_time +'</td>'+
                    '<td><strong class="color-green">'+item.payout +'</strong></td>'+
                    '</tr>'
                    //console.log(item)
                    $("#active-trade tbody").append(html)
                    openContract(item.contract_id)
                    if ($.inArray(item.symbol, currency_pair) == -1){
                          tickStream(item.symbol)
                          currency_pair.push(item.symbol)
                        }
                    
            });
            
    });
 }




function openContract(contract_id){
    api.getContractInfo(contract_id).then(response =>{
        $("#"+contract_id+" .open-tick").text(response.proposal_open_contract.entry_tick)
        $("#"+contract_id+" .current-tick").text(response.proposal_open_contract.current_spot)

    })
}

function tickStream(currency) {
    api.events.on('tick', function(response) {
        $("."+response.tick.symbol).text(response.tick.quote)
    });
    api.subscribeToTick(currency);
}


 function onPageLoad(){
    activeTrade()
    openContract()
 }

/* getProfitTable(){
    option = {
      "profit_table": 2,
      "description":1,
      "limit":10
    }
 }*/