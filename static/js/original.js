$(function() {
    
    $('.spiner_sub').on('click', function(){
        var el = $('.weight-counter');
        console.log(el.attr('data-min'));
        if (el.val() > el.attr('data-min')) {
            el.val(function(i, oldval) {
                return parseInt(oldval) - 1;
            });
        }
    });
    $('.spiner_add').on('click', function(){
        var el = $('.weight-counter');
        if (parseInt(el.val()) < el.attr('data-max')) {
            el.val(function(i, oldval) {
                return parseInt(oldval)+1;
            });
        }else{
            console.log('dame')
            console.log(el.val() )
            console.log(el.attr('data-max'))
        }
    });
    //±5ずつのボタンも作成
});