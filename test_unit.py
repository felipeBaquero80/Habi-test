from connect_db import connect_db
from filters import Filter_manage, json_parser
import json



def test_conexion_db():
    """
    Test the database connection.

    Checks if the database connection and cursor are valid.
    """
    conn, cursor = connect_db()
    assert conn is not None, "Connection should be successful"
    assert cursor is not None, "The cursor should be valid"
    print("Successful database connection test")

class TestFilterManage:
    """
    Test cases for the FilterManage class.
    """
    def test_json_parser(self):
        """
        Test the JSON parsing function.

        Compares the result of json_parser with an expected JSON string.
        """

        tuple_search = [
            ('carrera 100 #15-90', 'medellin', 'vendido', 325000000, 'Amplio apartamento en conjunto cerrado')]
        expected_result = '[{"Direccion": "carrera 100 #15-90", "Ciudad": "medellin", "Estado": "vendido", "Precio": 325000000, "Descripcion": "Amplio apartamento en conjunto cerrado"}]'


        filter_manager = Filter_manage()


        result = json_parser(tuple_search)

        assert result == expected_result, "La consulta es exitosa"

    def test_consult_db(self):
        """
        Test the consult_db function.

        Calls consult_db with filters and checks if the result is a valid JSON.
        """

        filter_manager = Filter_manage()

        # Llamar a consult_db con filtros
        filter_city = 'medellin'
        filter_address = ''
        filter_year = '2011'
        result = filter_manager.consult_db(filter_city, filter_address, filter_year)

        try:
            json.loads(result)
            print(result)
        except json.JSONDecodeError:
            assert False, "El resultado no es un JSON válido"







"""if __name__ == '__main__':
    test_filter_manager = TestFilterManage()
    test_filter_manager.test_json_parser()
    test_filter_manager.test_consult_db()






if __name__ == '__main__':
    test_conexion_db()"""