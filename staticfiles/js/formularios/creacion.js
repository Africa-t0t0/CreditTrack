

$(document).ready(function () {

    const tipoTarjetaSelect = $("#id_tipo_tarjeta");


    tipoTarjetaSelect.on("change", function () {
        const tipoPago = tipoTarjetaSelect.val();

        if (tipoPago === "debito") {
            $("#id_monto_maximo").hide();
            $("label[for='id_monto_maximo']").hide();
            $("id_monto_utilizado").hide();
            $("label[for='id_monto_utilizado']").hide();
            $("#id_fecha_pago").hide();
            $("label[for='id_fecha_pago']").hide();

            $("#id_saldo").show();
            $("label[for='id_saldo']").show();
        } else if (tipoPago === "credito") {
            $("#id_saldo").hide();
            $("label[for='id_saldo']").hide();

            $("#id_monto_maximo").show();
            $("label[for='id_monto_maximo']").show();
            $("#id_monto_utilizado").show();
            $("label[for='id_monto_utilizado']").show();
            $("#id_fecha_pago").show();
            $("label[for='id_fecha_pago']").show();
        }
    });
});