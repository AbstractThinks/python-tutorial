$(document).ready(function (){
    $('select').material_select();
    Materialize.showStaggeredList('.tag-list');


    $('#search').on('click', function () {
        var order = ""
        if ($('.sort-filter li.selected span').text()) {
            if ($('.sort-filter li.selected span').text() == '按时间升序') {
               order = "up" ;
            }else{
               order = "down" ;
            }

        }
        if (location.href.indexOf('?') > -1) {
            var address_url = location.href.split('?')[0];
            location.href = address_url+"?&address="+$('.address-filter li.selected span').text()+"&depart="+$('.depart-filter li.selected span').text()+"&order="+order
        } else {
            location.href = location.href+"?address="+$('.address-filter li.selected span').text()+"&depart="+$('.depart-filter li.selected span').text()+"&order="+order
        }
    });
    /**
     * post请求案例
     */
    // $('#search').on('click', function () {
    //     var data = {'depart':$('.depart-filter li.selected span').text(), 'address':$('.address-filter li.selected span').text()}
    //     // console.log(data);
    //     $.ajax({
    //         url:location.href,
    //         type:'POST',
    //         data:data,
    //         success:function(data){
    //             console.log(data);
    //         },
    //         error:function(data){
    //             console.log(data)
    //         }
    //     });
    // })
});


