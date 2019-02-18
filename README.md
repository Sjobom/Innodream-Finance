#InnoDream Finance
A stock recommendation service for the Swedish stock market.

[![Build Status](https://travis-ci.org/Sjobom/Innodream-Finance.svg?branch=master)](https://travis-ci.org/Sjobom/Innodream-Finance)



### Configuration
Create `secret.json` in the folder `application/instance` formatted like:
```
{
  "world_trading_data_api_key": "XXXXXXXXXXXXXXXXXXXXXXXXXX"
  "db": {
    "dbname": "local db name",
    "user": "postgres e.g.",
    "password": "password",
    "host": "localhost or IP address of db server"
  }
}