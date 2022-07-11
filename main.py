from datetime import datetime
from multiprocessing.sharedctypes import Value
class DateException(Exception):

    __module__ = 'builtins'

    def __init__(self, date, consult_date, message=""):
        self.date = date
        self.consult_date = consult_date
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Date {self.consult_date} is less than birth_date ({self.date})'

class DateFormatException(ValueError):

    __module__ = 'builtins'

    def __init__(self, date, message=""):
        self.date = date
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Date wrong format: {self.date}'


def mayoria_de_edad(fecha_nacimiento,fecha_consulta):
    try:
        dt1 = datetime.strptime(fecha_nacimiento,'%d/%m/%Y')
    except:
        raise DateFormatException(fecha_nacimiento)
    

    try:
        dt2 = datetime.strptime(fecha_consulta,'%d/%m/%Y')
    except:
        raise DateFormatException(fecha_consulta)

    if dt2 < dt1:
        raise DateException(dt1,dt2)

    return int((dt2 - dt1).days / 365) >= 18



