function SpittleWidget(config, transform, callback){
   var defaults ={
        timeout : 5000,
        container : 'spittle-container',
        transform: function(spittle){
            return '<h5>'+ spittle.title + '</h5>' +
                   '<p>' + spittle.message + '</p>';
        },
        callback : function(widget){
        }
    }

    if(config){
        for(var property in config){
            defaults[property] = config[property];
        }
    }

    if(transform && typeof transform == 'function'){
        defaults['transform'] = transform;
    }

    if(callback && typeof callback == 'function'){
        defaults['callback'] = callback;
    }

    SpittleWidget.prototype.launch = function(){
        $.getJSON('http://127.0.0.1:8000/rest/spittle?callback=?', null, function(spittles) {
            $('#' + defaults.container).html(defaults.transform(spittles));
        });
        defaults.callback(this);
        setTimeout(SpittleWidget.prototype.launch, defaults.timeout);
    }
}