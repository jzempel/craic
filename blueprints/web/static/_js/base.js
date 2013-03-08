var _gaq;

_gaq = [["setAccount", "UA-XXXXX-X"], ["_setAllowAnchor", true], ["_trackPageview"]];

if (typeof prettyPrint === "function") {
  prettyPrint();
}

$(function() {
  $(document).pjax("a[data-pjax]");
  $("a[href^='#']").click(function() {
    var action, label;
    action = location.hostname + location.pathname;
    label = location.href + $(this).attr("href");
    _gaq.push(["_trackEvent", "hash", action, label]);
  });
  $("a[href*='//']:not([href*='" + location.hostname + "'])").click(function() {
    var action, label;
    action = $(this).context.hostname;
    label = $(this).attr("href");
    _gaq.push(["_trackEvent", "outbound", action, label, void 0, true]);
  });
  $("form").submit(function() {
    var action;
    action = $(this).attr("action");
    _gaq.push(["_trackEvent", "submit", action]);
  });
});
