/* Variables */
var updateBtns = document.getElementsByClassName('update-cart')

/* Toggle navbar-toggler icon between "bars" and "X" icons 
    according to whether the mobile navbar is open */
$(function () {
    $('#navbarSupportedContent')
        /* When mobile navbar is open, hide the "bars" icon and display the "X" icon */
        .on('shown.bs.collapse', function () {
            $('#navbar-open-icon').addClass('hidden');
            $('#navbar-close-icon').removeClass('hidden');
        })
        /* When mobile navbar is closed, hide the "X" icon and display the "bars" icon */
        .on('hidden.bs.collapse', function () {
            $('#navbar-open-icon').removeClass('hidden');
            $('#navbar-close-icon').addClass('hidden');
        });

});

/* "< Back" button functionality */
function goBack() {
    window.history.back();
}