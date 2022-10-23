class Optimizer:
    def __init__(self, conn, schema, table, column):
        self.conn = conn
        self.schema = schema
        self.table = table
        self.column = column

    def column_list_table(self):
        return f"SELECT column_name FROM information_schema.columns " \
               f"WHERE table_schema = '{self.schema}' AND table_name = '{self.table}';"

    def column_datatype(self):
        return f"SELECT data_type FROM information_schema.columns " \
               f"WHERE table_schema = '{self.schema}' AND table_name = '{self.table}' " \
               f"AND column_name = '{self.column}';"

    def max_xchar(self):
        return f"SELECT length({self.column} FROM {self.schema}.{self.table};"

    def max_xint(self):
        return f"SELECT MAX({self.column} FROM {self.schema}.{self.table};"
