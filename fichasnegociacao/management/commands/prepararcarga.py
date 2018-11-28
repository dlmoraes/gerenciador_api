import subprocess
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
#from django.db import connection
from django.db import connections
from ...models import Ficha


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Preparando tabela de fichas...')
        # Ficha.objects.all().delete()
        self.reiniciarSequenciaPK()
        self.efetuarCarga()


    def reiniciarSequenciaPK(self):
        with connections['fichas'].cursor() as cursor:
            self.stdout.write('Inciando => {:%d/%b/%Y %H:%M:%S}'.format(datetime.now()))
            self.stdout.write('Limpando tabela de fichas...')
            cursor.execute('DELETE FROM fichasnegociacao_ficha')
            self.stdout.write('Limpeza concluídas em => {:%d/%b/%Y %H:%M:%S}'.format(datetime.now()))
            self.stdout.write('Limpando os espações tabela de fichas...')
            cursor.execute("VACUUM")
            self.stdout.write('Reiniciando a sequencia da tabela de fichas...')
            cursor.execute("update sqlite_sequence set seq=0 where name='fichasnegociacao_ficha'")
            self.stdout.write(self.style.SUCCESS('Tabela de fichas pronta para carga!'))

    def efetuarCarga(self):
        self.stdout.write('Iniciando carga de fichas.sqlite3')
        try:
            subprocess.run('sqlite3 fichas.sqlite3 < atualizar_fichas.txt', shell=True, check=False)
            self.stdout.write(self.style.SUCCESS('Carga Completa!'))
        except subprocess.SubprocessError:
            self.stdout.write(self.style.ERROR('Erro ao efetuar carga de fichas.sqlite3'))
