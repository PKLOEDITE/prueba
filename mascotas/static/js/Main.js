document.addEventListener('DOMContentLoaded', () => {
    const elementosCarousel = document.querySelectorAll('.carousel');
    M.Carousel.init(elementosCarousel, {
        duration: 200,
        padding: 5,
        dist: -80,
        shift: 5,
        numVisible: 3,
        indicators: true,
        noWrap: true

    });

});

$(document).ready(main);

var contador = 0;




document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('select');
    var options = {
        duration: 350,
        i18n: {
            cancel: 'cancelar',
            undefined: 'ok'
        }
    }
    var instances = M.FormSelect.init(elems, options);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.timepicker');
    var options = {
        duration: 350,
        i18n: {
            cancel: 'cancelar',
            undefined: 'ok'
        }
    }
    var instances = M.Timepicker.init(elems, options);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.datepicker');
    var options = {
        format: 'DD/MM/YYYY',
        i18n: {
            cancel: 'cancelar',

        }
    }
    var instances = M.Datepicker.init(elems, options);
});
function form() {
    alert("holiii");
}  