# exchange_trade_importer: A service to load cryptocurrency exchange trades

## What is this

The purpose of this service is to load and parse estructured files containing cryptocurrency trades performed in exchanges.
The data will be permanently stored in a database.

## Installation Guide: What do you need

The service has few dependencies:
Python
MongoDB
Poetry

## Service architecture: What, where, how and maybe why

All code can be found in src folder, and the files containing the data are in storage folder, both at BASE location: ./exchange_trade_importer
Python dependencies are at BASE/pyproject.toml
Service can be used from command line with the following instruction: poetry run exchange_trade_importer -d
This will trigger the main functionality of the service: Parse each valid file in storage subfolder trade_history and load every trade to MongoDB

Repeated executions will not duplicate any trade that is already present in the database.

## Database definition

MongoDB database has one schema: cryp

The schema has one collection: trades

Each trades record is composed of the following fields and the fields have the following types:

    _id: ObjectId
    isodate: ISODate
    date: String
    market: String 
    type: String [SELL, BUY]
    price: String
    amount: String
    total: String
    fee: String
    fee_coin: String
    primary_coin: Dict Object
        short_name: String
        long_name: String
    secondary_coin: Dict Object
        short_name: String
        long_name: String
    source: String
    description: String
    record_key: String
