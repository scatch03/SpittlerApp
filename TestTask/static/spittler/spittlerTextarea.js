var $ = $ || django.jQuery;

$(
    function(){
        $(".spittler-textarea").keyup( function(){
            var selected = $(this);
            var count = selected.val().length;
            selected.prev().html('&nbsp;' + count + '&nbsp;symbols');
        });
    }
);