/*! light-blue - v3.3.0 - 2016-03-08 */
function keyColor(a, b) {
    return window.colors || (window.colors = function() {
        return d3.scale.ordinal().range(COLOR_VALUES)
    }()), window.colors(a.key)
}

function closeNavigation() {
    var a = $("#side-nav").find(".panel-collapse.in");
    a.collapse("hide"), a.siblings(".accordion-toggle").addClass("collapsed"), resetContentMargin();
    var b = $("#sidebar");
    $(window).width() < 768 && b.is(".in") && b.collapse("hide")
}

function resetContentMargin() {
    $(window).width() > 767 && $(".content").css("margin-top", "")
}