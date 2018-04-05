CREATE DATABASE innodream_finance;

CREATE TABLE tickers (
  ticker TEXT NOT NULL,
  name   TEXT NOT NULL,
  PRIMARY KEY (ticker)
);

INSERT INTO tickers(ticker, name)
    VALUES('ABB.ST', 'ABB');