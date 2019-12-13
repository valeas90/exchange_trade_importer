import pymongo


class Mongo:

    @classmethod
    def connect(cls):
        uri = 'mongodb://localhost:27017/cryp'
        client = pymongo.MongoClient(uri)
        return client

    def __init__(self, client=None):
        if not client:
            self.client = self.connect()

    def handle_errors(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                raise

        return wrapper

    @handle_errors
    def find_trade(self, record_key):
        result = self.client.cryp.trades.find_one({'record_key': record_key})
        return result

    @handle_errors
    def insert_trade(self, data):
        result = self.client.cryp.trades.insert_one(data)
        return result.inserted_id
