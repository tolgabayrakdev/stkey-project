from sqlalchemy import create_engine

class DatabaseHelper:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
    
    def execute_query(self, sql_query):
        with self.engine.connect() as connection:
            result = connection.execute(sql_query)
            rows = result.fetchall()
        return rows
