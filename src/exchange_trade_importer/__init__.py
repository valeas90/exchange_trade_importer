from exchange_trade_importer import models
from exchange_trade_importer import utils
import os

__version__ = '0.1.0'

BASE_PATH = os.path.abspath(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__))))


def main():
    """Entry point for the application script"""
    file_path = os.path.join(BASE_PATH, 'storage', 'trade_history')
    fp = utils.file_processer.FileProcesser()
    mongo = utils.mongo.Mongo()
    stats = {'new_inserts': 0}

    for file in os.listdir(file_path):
        full_path = os.path.join(file_path, file)
        for element in fp.parse_file(full_path):
            trade = models.binance_trade.BinanceTrade(element)
            if trade.valid_trade:
                result = trade.insert(mongo)
                stats['new_inserts'] += result

    print(stats)
