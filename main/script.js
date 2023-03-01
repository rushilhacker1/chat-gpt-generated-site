$(document).ready(function() {
    $.get('output.txt', function(data) {
        $('.main-content').text(data);
    });
});
