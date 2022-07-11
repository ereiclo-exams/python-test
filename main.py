from datetime import datetime
class DateException(ValueError):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """
    __module__ = 'builtins'

    def __init__(self, date, message="Salary is not in (5000, 15000) range"):
        self.date = date
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'





def mayoria_de_edad(fecha_nacimiento,fecha_consulta):
    # dt1 = datetime.strptime(fecha_nacimiento,'%d/%m/%Y')

    # dt2 = datetime.strptime(fecha_nacimiento,'%d/%m/%Y')
    pass
