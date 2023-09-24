from datetime import datetime
from dateutil.relativedelta import relativedelta


def funcion_meses():
        meses = []
        fecha_actual = datetime.now()
        anio = fecha_actual.year
        nueva_fecha = fecha_actual - relativedelta(months=5)
        while True:
            if nueva_fecha.month == fecha_actual.month:
                meses.append(nueva_fecha.month)
                break
            meses.append(nueva_fecha.month)
            nueva_fecha = nueva_fecha + relativedelta(months=1)
        return meses, anio

def nombre_meses(meses):
    array_nombres = []
    meses_dict = {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre',
     }
    for mes in meses:
        array_nombres.append(meses_dict[mes])
    return array_nombres