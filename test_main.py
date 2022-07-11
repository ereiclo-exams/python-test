from main import DateException
import pytest



class TestClass:


    def test_1(self):
        with pytest.raises(DateException) as e_info:
            raise DateException(2134)
        
        # assert e_info.type is DateException 
        # assert e_info.type is ValueError


    def test_2(self):
        with pytest.raises(Exception) as e_info:
            raise DateException(2134)
            
        assert e_info.type is DateException 


