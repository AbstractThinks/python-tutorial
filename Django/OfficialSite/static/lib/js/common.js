/**
 * Created by Jesse on 16/9/6.
 */
$(document).ready( function () {
    
    $('.button-collapse').sideNav({
      time_constant: 10,
      menuWidth: 300, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    }
    );
    $('.parallax').parallax();

});
