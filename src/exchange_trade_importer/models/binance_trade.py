import datetime
from exchange_trade_importer.models.trade import Trade
from exchange_trade_importer.models.coin import COINS

class BinanceTrade(Trade):
    MANDATORY_FIELDS = [
        'Date(UTC)', 'Market', 'Type', 'Price', 'Amount', 'Total', 'Fee', 'Fee Coin'
    ]

    def __init__(self, *args):
        self.valid_trade = True
        self.normalized_data = {}
        Trade.__init__(self, *args)
        self.normalize()

    def normalize(self):
        for current_name, target_name in zip(self.MANDATORY_FIELDS, self.BASE_FIELDS):
            self.normalized_data[target_name] = self.atr_data[current_name]

        traded_pair = self.get_traded_pair(self.atr_data['Market'])
        self.normalized_data['primary_coin'] = traded_pair['left']
        self.normalized_data['secondary_coin'] = traded_pair['right']
        self.normalized_data['source'] = 'Binance'

        try:
            descriptive = {
                'type': self.normalized_data['type'].capitalize(),
                'amount': self.normalized_data['amount'],
                'price': self.normalized_data['price'],
                'strdate': self.normalized_data['strdate'],
                'primary': self.normalized_data['primary_coin']['long_name'],
                'secondary': self.normalized_data['secondary_coin']['long_name']
            }
            if self.normalized_data['type'] in ['BUY', 'SELL']:
                self.normalized_data['description'] = '{type} {amount} {primary} using {secondary} at {price} [{strdate}]'.format(**descriptive)

            self.normalized_data['record_key'] = '{strdate}-{type}-{amount}-{primary}-{secondary}-{price}'.format(**descriptive)
            self.normalized_data['isodate'] = datetime.datetime.strptime(self.normalized_data['strdate'], '%Y-%m-%d %H:%M:%S')
            self.normalized_data['meta_doc_created_at'] = datetime.datetime.utcnow()
        except:
            print('Ommiting: %s' % self.normalized_data)
            self.valid_trade = False

    def get_traded_pair(self, market):
        result = {'left': None, 'right': None}
        possible_lefts = (market[0:3], market[0:4], market[0:5])
        for possible_left in possible_lefts:
            if possible_left in COINS:
                long, short = COINS.get(possible_left)
                result['left'] = {'short_name': short, 'long_name': long}
                break

        if result['left']:
            right = market[len(result['left']['short_name']):]
            if right in COINS:
                long, short = COINS.get(right)
                result['right'] = {'short_name': short, 'long_name': long}

        return result

    def insert(self, mongo):
        result = mongo.find_trade(self.normalized_data['record_key'])
        if result:
            return 0
        else:
            trade_id = mongo.insert_trade(self.normalized_data)
            return 1
