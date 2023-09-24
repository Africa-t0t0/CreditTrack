$(document).ready(function () {

    $("#id_fecha").datepicker();

    function crearTransaccionFormListener() {
        $("#crearTransaccionButton").on("click", function () {
            const data = $(this).serialize();
            const url = $(this).attr("action");
            const method = $(this).attr("method");
            $.ajax({
                url: url,
                method: method,
                data: data,
                success: function (data) {
                    location.reload();
                },
                error: function (error) {
                    console.log(error);
                }
            });
        });
    }

    // crearTransaccionFormListener();

});