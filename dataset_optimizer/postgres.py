import psycopg2


class Postgres:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = psycopg2.connect(database=self.database, user=self.user,
                                     password=self.password, host=self.host, port=self.port)
        self.db_cur = self.conn.cursor()

    def execute_code(self, code):
        return self.db_cur.execute(code)

    # Change this for cfg file
    @staticmethod
    def datatype_varchar():
        varchar = 10485760
        char = None
        text = None

    @staticmethod
    def varchar():
        return 10485760

    @staticmethod
    def char():
        return None

    @staticmethod
    def text():
        return None


    @staticmethod
    def datatype_numbers():
        smallint = 2
        int = 4
        bigint = 8
        real = 4
        double = 8

    @staticmethod
    def datatype_serials():
        smallserial = 2
        serial = 4
        bigserial = 8
