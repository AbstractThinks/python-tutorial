/**
 * Created by Jesse on 16/9/6.
 */

$(document).ready(function (){
    // var options = [
    //     {selector: '.class', offset: 200, callback: customCallbackFunc }},
    //     {selector: '.other-class', offset: 200, callback: function() {
    //         customCallbackFunc();
    //     }},
    // ];
    // Materialize.scrollFire(options);
    $('select').material_select();
    Materialize.showStaggeredList('#tag-list');
});
