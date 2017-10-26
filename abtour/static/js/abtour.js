$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
      lazyLoad:true,
      loop:true,
      autoplay:true,
      autoplayHoverPause:false,
      animateOut: 'fadeOut',
      nav:false,
      dots:false,
      mouseDrag: false,
      touchDrag: false,
      items:1
  });
  AOS.init();
  datepicker();
  href_target_blank();
  href_section_scroll();
});

$(function ($) {
    $('#id_phone').mask("+7(999)999-99-99");
    $('#id_budget').mask("?999999999",{placeholder:" "});
});

$(window).scroll(ScrollChange);

function href_target_blank(){
$('a[href^="http://"]').attr('target', '_blank');
$('a[href^="https://"]').attr('target', '_blank');
}

function href_section_scroll() {
	$('a[href^="#"]').on('click',function (e) {
	    e.preventDefault();

	    var target = this.hash;
	    var $target = $(target);

	    $('html, body').stop().animate({
        'scrollTop': $target.offset().top
        }, 900, 'swing');
	});
}

function datepicker() {
    var startdate = $('#id_startdate');
    var enddate = $('#id_enddate');
    startdate.datetimepicker({
        format: "DD.MM.YYYY",
        locale: 'ru',
        minDate: moment()
    });
    enddate.datetimepicker({
        format: "DD.MM.YYYY",
        useCurrent: false, //Important! See issue #1075
        locale: 'ru',
        minDate: moment()
    });
    startdate.on("dp.change", function (e) {
        enddate.data("DateTimePicker").minDate(e.date);
    });
    enddate.on("dp.change", function (e) {
        startdate.data("DateTimePicker").maxDate(e.date);
    });
}

$('#datetimepicker1').datetimepicker({
    format: "E"
});

function ScrollChange() {
    if ($(document).scrollTop() > 50) {
        $('nav').addClass('shrink');
        $('#enquire-btn').addClass('btn-shrink');
        $('#logo').css("max-height", "70px");
        $('#logo-link').css("padding-top", "7px")
    } else {
        $('nav').removeClass('shrink');
        $('#enquire-btn').removeClass('btn-shrink');
        $('#logo').css("max-height", "100px");
        $('#logo-link').css("padding-top", "15px")
    }
}

$('.no-right-click').contextmenu(function () {
   return false
});




//-------------------------------------------------------
//------------TESTING--------AREA-------BELOW------------
//-------------------------------------------------------

