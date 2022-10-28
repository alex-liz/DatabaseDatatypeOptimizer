import postgres

class Optimizer:
    def __init__(self, schema, table, column):
        self.schema = schema
        self.table = table
        self.column = column

    def column_list_table(self):
        return f"SELECT column_name FROM information_schema.columns " \
               f"WHERE table_schema = '{self.schema}' AND table_name = '{self.table}';"

    def column_datatype(self, column_name):
        return f"SELECT data_type FROM information_schema.columns " \
               f"WHERE table_schema = '{self.schema}' AND table_name = '{self.table}' " \
               f"AND column_name = '{column_name}';"

    def max_xchar(self):
        return f"SELECT length({self.column} FROM {self.schema}.{self.table};"

    def max_xint(self):
        return f"SELECT MAX({self.column} FROM {self.schema}.{self.table};"

    def postgres_optimizer(self):
        postgres_db = postgres.Postgres(database=None, user=None, password=None, host=None, port=None)
        if not self.column:
            column_list = self.column_list_table()
        else:
            column_list = [self.column]
        for column_name in column_list:
            column_datatype = self.column_datatype(column_name=column_name)
            if column_datatype in 'char':
                max_char = self.max_xchar()
            postgres_db.varchar()

            # elif self.column_datatype(column_name=column_name) in 'int':
            #     max_int = self.max_xint()
