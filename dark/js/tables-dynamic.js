/*! light-blue - v3.3.0 - 2016-03-08 */

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
var columns = ["buy_price", "longcode", "payout","sell_price"];

var data  = originalJson.map(function(row) {
          return columns.map(function(col){
              return row[col];
          })
       })

$(function() {
    function a() {
        function a(a) {
            var b = [{
                name: "longcode",
                label: "longcode",
                cell: "string"
            }, {
                name: "buy_price",
                label: "buy_price",
                cell: "string"
            }, {
                name: "payout",
                label: "payout",
                cell: "string"
            }, {
                name: "sell_price",
                label: "sell_price",
                cell: "string"
            }];
            LightBlue.isScreen("xs") && b.splice(3, 1);
            var c = new Backgrid.Grid({
                    columns: b,
                    collection: a,
                    className: "table table-striped table-editable no-margin mb-sm"
                }),
                d = new Backgrid.Extension.Paginator({
                    slideScale: .25,
                    goBackFirstOnSort: !1,
                    collection: a,
                    controls: {
                        rewind: {
                            label: '<i class="fa fa-angle-double-left fa-lg"></i>',
                            title: "First"
                        },
                        back: {
                            label: '<i class="fa fa-angle-left fa-lg"></i>',
                            title: "Previous"
                        },
                        forward: {
                            label: '<i class="fa fa-angle-right fa-lg"></i>',
                            title: "Next"
                        },
                        fastForward: {
                            label: '<i class="fa fa-angle-double-right fa-lg"></i>',
                            title: "Last"
                        }
                    }
                });
            $("#table-dynamic").html("").append(c.render().$el).append(d.render().$el)
        }
        Backgrid.InputCellEditor.prototype.attributes["class"] = "form-control input-sm";
        var b = Backbone.Model.extend({}),
            c = Backbone.PageableCollection.extend({
                model: b,
                data: data,
                state: {
                    pageSize: 9
                },
                mode: "client"
            }),
            d = new c,
            e = d;
/*        PjaxApp.onResize(function() {
            a(d)
        }), a(d), $("#search-countries").keyup(function() {
            var b = $(this),
                d = e.fullCollection.filter(function(a) {
                    return ~a.get("name").toUpperCase().indexOf(b.val().toUpperCase())
                });
            a(new c(d, {
                state: {
                    firstPage: 1,
                    currentPage: 1
                }
            }))
        }), d.fetch()*/
    }

    function b() {
        $.extend(!0, $.fn.dataTable.defaults, {
            sDom: "<'row'<'col-md-6'l><'col-md-6'f>r>t<'row'<'col-md-6'i><'col-md-6'p>>",
            sPaginationType: "bootstrap",
            oLanguage: {
                sLengthMenu: "_MENU_ records per page"
            }
        }), $.extend($.fn.dataTableExt.oStdClasses, {
            sWrapper: "dataTables_wrapper form-inline"
        }), $.fn.dataTableExt.oApi.fnPagingInfo = function(a) {
            return {
                iStart: a._iDisplayStart,
                iEnd: a.fnDisplayEnd(),
                iLength: a._iDisplayLength,
                iTotal: a.fnRecordsTotal(),
                iFilteredTotal: a.fnRecordsDisplay(),
                iPage: -1 === a._iDisplayLength ? 0 : Math.ceil(a._iDisplayStart / a._iDisplayLength),
                iTotalPages: -1 === a._iDisplayLength ? 0 : Math.ceil(a.fnRecordsDisplay() / a._iDisplayLength)
            }
        }, $.extend($.fn.dataTableExt.oPagination, {
            bootstrap: {
                fnInit: function(a, b, c) {
                    var d = a.oLanguage.oPaginate,
                        e = function(b) {
                            b.preventDefault(), a.oApi._fnPageChange(a, b.data.action) && c(a)
                        };
                    $(b).append('<ul class="pagination no-margin"><li class="prev disabled"><a href="#">' + d.sPrevious + '</a></li><li class="next disabled"><a href="#">' + d.sNext + "</a></li></ul>");
                    var f = $("a", b);
                    $(f[0]).bind("click.DT", {
                        action: "previous"
                    }, e), $(f[1]).bind("click.DT", {
                        action: "next"
                    }, e)
                },
                fnUpdate: function(a, b) {
                    var c, d, e, f, g, h, i = 5,
                        j = a.oInstance.fnPagingInfo(),
                        k = a.aanFeatures.p,
                        l = Math.floor(i / 2);
                    for (j.iTotalPages < i ? (g = 1, h = j.iTotalPages) : j.iPage <= l ? (g = 1, h = i) : j.iPage >= j.iTotalPages - l ? (g = j.iTotalPages - i + 1, h = j.iTotalPages) : (g = j.iPage - l + 1, h = g + i - 1), c = 0, d = k.length; d > c; c++) {
                        for ($("li:gt(0)", k[c]).filter(":not(:last)").remove(), e = g; h >= e; e++) f = e == j.iPage + 1 ? 'class="active"' : "", $("<li " + f + '><a href="#">' + e + "</a></li>").insertBefore($("li:last", k[c])[0]).bind("click", function(c) {
                            c.preventDefault(), a._iDisplayStart = (parseInt($("a", this).text(), 10) - 1) * j.iLength, b(a)
                        });
                        0 === j.iPage ? $("li:first", k[c]).addClass("disabled") : $("li:first", k[c]).removeClass("disabled"), j.iPage === j.iTotalPages - 1 || 0 === j.iTotalPages ? $("li:last", k[c]).addClass("disabled") : $("li:last", k[c]).removeClass("disabled")
                    }
                }
            }
        });

    }
});