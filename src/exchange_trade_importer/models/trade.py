from exchange_trade_importer.utils import checker

class Trade:
    BASE_FIELDS = MANDATORY_FIELDS = [
        'date', 'market', 'type', 'price', 'amount', 'total', 'fee', 'fee_coin'
    ]

    def __init__(self, data):
        if not isinstance(data, dict):
            raise Exception('Trade init error. Received data is not dict')
        if not checker.is_dict_valid(data, self.MANDATORY_FIELDS):
            raise Exception('Trade init error. Missing fields')

        self.atr_data = {**data}

    def insert(self):
        """Insert the trade in the db. Child classes must implement this"""
        raise NotImplementedError
