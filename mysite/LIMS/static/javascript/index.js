$(document).ready(function () {
    function delay(callback, ms) {
        var timer = 0;
        return function () {
            var context = this, args = arguments;
            clearTimeout(timer);
            timer = setTimeout(function () {
                callback.apply(context, args);
            }, ms || 0);
        };
    }

    $(document).on('keyup', '#id_taxon_id', delay(function (e) {
        var t_id = $('#id_taxon_id').val()

        $.ajax({
            'url': 'auto_complete',
            'method': 'GET',
            data: {
                't_id': t_id
            }
        }).done(function (data) {
            $("#id_scientific_name").val(data)
            $("#id_common_name").val(data)
        })
    }, 1000))

})
