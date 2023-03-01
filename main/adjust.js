$(document).ready(function() {
    // Check if sidebar-right is hidden and adjust flex-basis values
    function adjustFlexBasis() {
      if($('.sidebar-right').is(':hidden')) {
        $('.main-content').css('flex-basis', '80%');
        $('.sidebar-left').css('flex-basis', '20%');
      } else {
        $('.main-content').css('flex-basis', '60%');
        $('.sidebar-left').css('flex-basis', '20%');
      }
    }
    
    // Call adjustFlexBasis on page load
    adjustFlexBasis();
    
    // Call adjustFlexBasis on window resize
    $(window).resize(function() {
      adjustFlexBasis();
    });
    
    // Hide sidebar-right if no ads are displayed
    $('.adsbygoogle').each(function() {
      if($(this).height() === 0) {
        $(this).closest('.sidebar-right').hide();
        adjustFlexBasis();
      }
    });
  });
  