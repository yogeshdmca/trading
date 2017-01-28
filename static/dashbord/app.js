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


originalJson = [
      {
        "app_id": "0",
        "buy_price": "1.1",
        "contract_id": "12140965868",
        "longcode": "Win payout if EUR/USD is strictly higher than entry spot at 2 minutes after contract start time.",
        "payout": "2",
        "purchase_time": 1485337075,
        "sell_price": "2",
        "sell_time": 1485337196,
        "shortcode": "CALL_FRXEURUSD_2_1485337075_1485337195_S0P_0",
        "transaction_id": "24199172648"
      },
      {
        "app_id": "0",
        "buy_price": "1.05",
        "contract_id": "12140887348",
        "longcode": "Win payout if EUR/USD is strictly higher than entry spot at 2 minutes after contract start time.",
        "payout": "2",
        "purchase_time": 1485336756,
        "sell_price": "2",
        "sell_time": 1485336878,
        "shortcode": "CALL_FRXEURUSD_2_1485336756_1485336876_S0P_0",
        "transaction_id": "24199016328"
      },
      {
        "app_id": "0",
        "buy_price": "2.58",
        "contract_id": "12140739708",
        "longcode": "Win payout if EUR/USD is strictly higher than entry spot at 2 minutes after contract start time.",
        "payout": "5.0",
        "purchase_time": 1485336240,
        "sell_price": "0",
        "sell_time": 1485336360,
        "shortcode": "CALL_FRXEURUSD_5.0_1485336240_1485336360_S0P_0",
        "transaction_id": "24198717868"
      },
      {
        "app_id": "0",
        "buy_price": "2.77",
        "contract_id": "12140713868",
        "longcode": "Win payout if EUR/USD is strictly higher than entry spot at 1 minute after contract start time.",
        "payout": "5.0",
        "purchase_time": 1485336145,
        "sell_price": "5",
        "sell_time": 1485336207,
        "shortcode": "CALL_FRXEURUSD_5.0_1485336145_1485336205_S0P_0",
        "transaction_id": "24198666928"
      },
      {
        "app_id": "1",
        "buy_price": "5.46",
        "contract_id": "12140380208",
        "longcode": "Win payout if EUR/GBP is strictly lower than entry spot at 1 minute after contract start time.",
        "payout": "10",
        "purchase_time": 1485334871,
        "sell_price": "10",
        "sell_time": 1485334932,
        "shortcode": "PUT_FRXEURGBP_10_1485334871_1485334931_S0P_0",
        "transaction_id": "24198005108"
      },
      {
        "app_id": "0",
        "buy_price": "5.18",
        "contract_id": "12051415048",
        "longcode": "Win payout if EUR/USD is strictly higher than entry spot at 1 minute after contract start time.",
        "payout": "10",
        "purchase_time": 1484931331,
        "sell_price": "0",
        "sell_time": 1484931395,
        "shortcode": "CALL_FRXEURUSD_10_1484931331_1484931391_S0P_0",
        "transaction_id": "24019951268"
      },
      {
        "app_id": "1",
        "buy_price": "2.5",
        "contract_id": "12045850648",
        "longcode": "Win payout if AUD/NZD is strictly higher than entry spot at 2 minutes after contract start time.",
        "payout": "5",
        "purchase_time": 1484910638,
        "sell_price": "5",
        "sell_time": 1484910758,
        "shortcode": "CALL_FRXAUDNZD_5_1484910638_1484910758_S0P_0",
        "transaction_id": "24008810208"
      },
      {
        "app_id": "1089",
        "buy_price": "5.21",
        "contract_id": "12044587948",
        "longcode": "Win payout if USD/CAD is strictly higher than entry spot at 1 minute after contract start time.",
        "payout": "10",
        "purchase_time": 1484905985,
        "sell_price": "0",
        "sell_time": 1484906046,
        "shortcode": "CALL_FRXUSDCAD_10_1484905985_1484906045_S0P_0",
        "transaction_id": "24006281168"
      },
      {
        "app_id": "1",
        "buy_price": "5.15",
        "contract_id": "12042668088",
        "longcode": "Win payout if Tata Motors is strictly lower than entry spot at close on 2017-01-25.",
        "payout": "10",
        "purchase_time": 1484898565,
        "sell_price": "0.00",
        "sell_time": 1485488702,
        "shortcode": "PUT_INTATAMOTORS_10_1484898565_1485338400_S0P_0",
        "transaction_id": "24002438988"
      },
      {
        "app_id": "1",
        "buy_price": "5.5",
        "contract_id": "12042567948",
        "longcode": "Win payout if Reliance Industries is strictly higher than entry spot at 5 minutes after 2017-01-20 07:50:00 GMT.",
        "payout": "10",
        "purchase_time": 1484898169,
        "sell_price": "4.5",
        "sell_time": 1484898543,
        "shortcode": "CALL_INRIL_10_1484898600F_1484898900_S0P_0",
        "transaction_id": "24002238068"
      }
    ]
var columns = ["longcode", "buy_price","sell_price", "payout",];

var data  = originalJson.map(function(row) {
          return columns.map(function(col){
              return row[col];
          })
       })

//console.log(data)

//$('#expire-trade').dataTable( dataTableObj );

$(document).ready(function() {
    $('#table-dynamic').DataTable( {
        data: data,
        columns: [
            { title: "Trade Detail" },
            { title: "Buy Price" },
            { title: "Sell Price" },
            { title: "Payout" },
        ]
    } );
} );