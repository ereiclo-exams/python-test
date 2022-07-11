from main import DateException,DateFormatException,mayoria_de_edad
import pytest



class TestClass:


    def test_1(self):
        with pytest.raises(Exception):
            raise DateException(2134)
        

    def test_2(self):
        with pytest.raises(DateFormatException):
            raise DateFormatException("")

    def test_3(self):
        assert mayoria_de_edad('18/05/2002','11/07/2022') == True

    def test_4(self):
        assert mayoria_de_edad('18/05/2002','11/07/2004') == False

    def test_5(self):
        with pytest.raises(DateException):
            mayoria_de_edad('18/05/2002','18/02/2002')

    def test_6(self):
        with pytest.raises(DateFormatException):
            mayoria_de_edad('18052002','18/06/2002')

    def test_7(self):
        with pytest.raises(DateFormatException):
            mayoria_de_edad('18/05/2002','18062002')
