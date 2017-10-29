$(document).ready(function(){
  AOS.init();
  datepicker();
  href_target_blank();
  // href_section_scroll();
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

// function href_section_scroll() {
//
// }

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
    if ($('body').is('.no-navbar-change')) {}
    else {
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
}

$('.no-right-click').contextmenu(function () {
   return false
});

function offerModal(id) {
    $("#offerModal_"+id).modal();
}

function formModal(data) {
    data = typeof data !== 'undefined' ? data : '';
    $("#formModal").modal();
    $("#id_comment")[0].value = data
}


//-------------------------------------------------------
//------------TESTING--------AREA-------BELOW------------
//-------------------------------------------------------

