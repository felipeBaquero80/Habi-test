from connect_db import connect_db
import json


def json_parser(tuple_search):
    """
    Convert a tuple of database search results into JSON format.

    Args:
        tuple_search (tuple): A tuple containing database search results.

    Returns:
        str: JSON representation of the search results.
    """
    result_dict = [
        {"Direccion": row[0], 'Ciudad': row[1], 'Estado': row[2], 'Precio': row[3], 'Descripcion': row[4]} for row
        in tuple_search]
    result_json = json.dumps(result_dict)
    return result_json


class Filter_manage:
    """
    A class for managing property filters and database queries.
    """

    def consult_db(self, filter_city, filter_address, filter_year):

        """
        Execute a database query based on provided filters.

        Args:
            filter_city (str): The city filter.
            filter_address (str): The address filter.
            filter_year (str): The year filter.

        Returns:
            str: JSON representation of the query results.
        """

        string_consulta = """SELECT p.address, p.city,
                                s.name, p.price, p.description FROM status As s
                                INNER JOIN status_history AS sh ON s.id = sh.property_id
                                INNER JOIN property AS p  ON s.id = p.id
                                where (s.name IN ('pre_venta', 'en_venta', 'vendido')) AND sh.update_date = (
                                SELECT MAX(update_date)
                                FROM status_history
                                WHERE property_id = p.id)"""

        conditions = []

        if filter_city:
            conditions.append(f"""p.city ='{filter_city.lower()}'""")
        if filter_address:
            conditions.append(f"""p.address ='{filter_address.lower()}'""")
        if filter_year:
            conditions.append(f"""p.year ='{filter_year.lower()}'""")

        if conditions:
            where_clause = "AND " + "AND ".join(conditions)
            string_consulta += where_clause

        string_consulta += "ORDER BY p.id, sh.update_date DESC;"

        # get conn and cursor from connect_db
        conn, cursor = connect_db()

        if conn and cursor:
            cursor.execute(string_consulta)
            result = cursor.fetchall()

            print('Cerrando conexiones...')
            cursor.close()
            conn.close()
            print('Conexion cerrada')

            return json_parser(result)
