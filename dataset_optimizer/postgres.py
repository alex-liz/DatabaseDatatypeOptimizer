import psycopg2


class PostgresConfig:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.db_cur = self.conn.cursor()

    def connection(self):
        self.conn = psycopg2.connect(database=self.database, user=self.user,
                                     password=self.password, host=self.host, port=self.port)

    def execute_code(self, code):
        return self.db_cur.execute(code)

    # Change this for cfg file
    @staticmethod
    def datatype_varchar():
        varchar = None
        char = None
        # Numbers
        smallint = 2
        int = 4
        bigint = 8
        real = 4
        double = 8
        # Serials
        smallserial = 2
        serial = 4
        bigserial = 8

    def sql_check_char(self):
        pass
