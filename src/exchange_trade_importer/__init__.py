from argparse import ArgumentParser
from pathlib import Path
import os
import sys
from exchange_trade_importer import models
from exchange_trade_importer import utils

__version__ = '0.1.0'

BASE_PATH = os.path.abspath(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__))))

def get_args():
    parser = ArgumentParser(description="exchange_trade_importer")
    parser.add_argument(
        '-u', '--user_id', required=True, help='User ID')
    parser.add_argument(
        '-d', '--debug', action='store_true', help='Enable debug mode')

    return parser.parse_args(sys.argv[1:])


def main():
    """Entry point for the application script"""
    args = get_args()
    file_path = os.path.join(BASE_PATH, 'storage', 'trade_history')
    fp = utils.file_processer.FileProcesser()
    mongo = utils.mongo.Mongo()
    stats = {'new_inserts': 0}
    # Pending: Check if user id exists
    for file in os.listdir(file_path):
        full_path = os.path.join(file_path, file)
        for element in fp.parse_file(full_path):
            element['user_id'] = args.user_id
            trade = models.binance_trade.BinanceTrade(element)
            if trade.valid_trade:
                result = trade.insert(mongo)
                stats['new_inserts'] += result

    print(stats)
