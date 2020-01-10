# exchange_trade_importer CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- More fields to trade records
- Add user_id to trade schema
- Add trade_uuid to trade schema
- Rename record_key to meta_record_key
- Rename isodate to traded_at
- Now user_id must be entered to import data
- Now record_key can be duplicated if belongs to different users

## [1.0.0] - 2017-06-20

### Added

- Stable functionality from [@valeas90](https://github.com/valeas90).

[Unreleased]: https://github.com/valeas90/exchange_trade_importer/compare/v1.0.0...HEAD
[0.0.1]: https://github.com/valeas90/exchange_trade_importer/releases/tag/v1.0.0
