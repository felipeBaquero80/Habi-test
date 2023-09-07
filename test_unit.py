from connect_db import connect_db
from filters import Filter_manage
import json



def test_conexion_db():
    conn, cursor = connect_db()
    assert conn is not None, "Connection should be successful"
    assert cursor is not None, "The cursor should be valid"
    print("Successful database connection test")

class TestFilterManage:

    def test_json_parser(self):

        tuple_search = [('123 Main St', 'New York', 'NY', 100000, 'Lorem ipsum')]
        expected_result = '[{"Direccion": "123 Main St", "Ciudad": "New York", "Estado": "NY", "Precio": 100000, "Descripcion": "Lorem ipsum"}]'


        filter_manager = Filter_manage()


        result = filter_manager.json_parser(tuple_search)

        assert result == expected_result

    def test_consult_db(self):

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
"""





if __name__ == '__main__':
    test_conexion_db()