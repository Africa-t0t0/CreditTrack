

$(document).ready(function () {

    const tipoTarjetaSelect = $("#id_tipo_tarjeta");

    if (tipoTarjetaSelect.val() === "debito") {
        $("#id_monto_maximo").prop("disabled", true);
        $("#id_monto_utilizado").prop("disabled", true);
        $("#id_fecha_pago").prop("disabled", true);
        $("#id_saldo").prop("disabled", false);
    } else {
        $("#id_monto_maximo").prop("disabled", false);
        $("#id_monto_utilizado").prop("disabled", false);
        $("#id_fecha_pago").prop("disabled", false);
        $("#id_saldo").prop("disabled", true);
    }

    tipoTarjetaSelect.on("change", function () {
        const tipoPago = tipoTarjetaSelect.val();

        if (tipoPago === "debito") {
            $("#id_monto_maximo").prop("disabled", true);
            $("#id_monto_utilizado").prop("disabled", true);
            $("#id_fecha_pago").prop("disabled", true);
            $("#id_saldo").prop("disabled", false);
        } else if (tipoPago === "credito") {
            $("#id_monto_maximo").prop("disabled", false);
            $("#id_monto_utilizado").prop("disabled", false);
            $("#id_fecha_pago").prop("disabled", false);
            $("#id_saldo").prop("disabled", true);

        }
    });
});