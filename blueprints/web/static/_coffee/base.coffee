_gaq = [
    ["setAccount", "UA-XXXXX-X"]
    ["_setAllowAnchor", true]
    ["_trackPageview"]
]

prettyPrint?()

$ ->
    $(document).pjax "a[data-pjax]"


    $("a[href^='#']").click ->
        action = location.hostname + location.pathname
        label = location.href + $(this).attr "href"

        _gaq.push ["_trackEvent", "hash", action, label]

        return


    $("a[href*='//']:not([href*='#{location.hostname}'])").click ->
        action = $(this).context.hostname
        label = $(this).attr "href"

        _gaq.push ["_trackEvent", "outbound", action, label, undefined, true]

        return


    $("form").submit ->
        action = $(this).attr "action"

        _gaq.push ["_trackEvent", "submit", action]

        return

    return
