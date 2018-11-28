# coding = utf-8

import datetime

def formatoDeHoras(interval):
    segundos  = interval.total_seconds()

    # formata minutos e segundos
    duracao  = datetime.datetime.utcfromtimestamp(segundos)
    formatado = duracao.strftime('%M:%S')

    # formata horas e concatena com os minutos e segundos formatados
    return '%02d:%s' % (segundos / (60 * 60), formatado)