/*! light-blue - v3.3.0 - 2016-03-08 */$(function(){function a(){$(".widget").widgster(),$(".sparkline").each(function(){$(this).sparkline("html",$(this).data())}),$(".js-progress-animate").animateProgressBar()}a(),PjaxApp.onPageLoad(a)});