[![Python CI](https://github.com/safe-global/safe-price-service/actions/workflows/python.yml/badge.svg?branch=main)](https://github.com/safe-global/safe-price-service/actions/workflows/python.yml)
[![Coverage Status](https://coveralls.io/repos/github/safe-global/safe-price-service/badge.svg?branch=main)](https://coveralls.io/github/safe-global/safe-price-service?branch=main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)
![Django 5](https://img.shields.io/badge/Django-5-blue.svg)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/safeglobal/safe-price-service?label=Docker&sort=semver)](https://hub.docker.com/r/safeglobal/safe-price-service)

# Safe Price Service

Returns fiat prices for base currencies and ERC20 tokens.

This logic was previously on the [Safe Transaction Service](https://github.com/safe-global/safe-transaction-service). As it was not needed anymore but a lot of work was done,
a decision was made to create a new service and give it to the Ethereum community.

It's expected that the project will be community driven, Safe team will only take care of updating dependencies and reviewing community PRs, so please don't open issues
about your favorite token not returning a price or price being wrong.

## Configuration

One instance of the service can support multiple EVM compatible chains.

```bash
cp .env.sample .env
```

Configure environment variables on `.env`:

- `DJANGO_SECRET_KEY`: **IMPORTANT: Update it with a secure generated string**.
- `ETHEREUM_NODES_URLS`: Comma separated list of the node RPCs for the chains supported for fetching prices.
- `PRICES_CACHE_TTL_MINUTES`: Minutes to keep a price in cache.

## Execution

```bash
docker compose build
docker compose up
```

Then go to http://localhost:8000 to see the service documentation.

Example request to get USD for Gnosis token on mainnet:
http://localhost:8000/api/v1/1/tokens/0x6810e776880C02933D47DB1b9fc05908e5386b96/prices/usd/

## Endpoints

- /v1/{chainId}/tokens/{address}/prices/usd/

## Contributors

[See contributors](https://github.com/safe-global/safe-price-service/graphs/contributors)
