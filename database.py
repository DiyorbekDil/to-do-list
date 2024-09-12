import sqlalchemy

DATABASE_URL = "postgresql://postgres:diyorbekdev123@localhost:5432/to_do"

engine = sqlalchemy.create_engine(DATABASE_URL)

metadata = sqlalchemy.MetaData()
metadata.create_all(engine)


class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.transaction = None

    def __enter__(self):
        try:
            self.conn = engine.connect()
            self.transaction = self.conn.begin()
            return self
        except Exception as e:
            print(f"Error while connecting to database: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn is not None and exc_type is None:
            self.conn.commit()
        elif self.conn is not None and exc_type is not None:
            self.conn.rollback()
        elif self.conn is not None:
            self.conn.close()

    def execute(self, query):
        return self.conn.execute(query)


def execute_query(query):
    with DatabaseManager() as db:
        result = db.execute(query)
        return result

