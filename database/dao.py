from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO

    @staticmethod
    def read_rifugi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM rifugio"""
        cursor.execute(query)
        for row in cursor:
            result[row['id']] = Rifugio(**row)

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def read_connessioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM connessione"""
        cursor.execute(query)
        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result

    """
    @staticmethod
    def get_sentieri():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = 
        cursor.execute(query)
        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
    """






