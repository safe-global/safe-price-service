![Build Status](https://github.com/safe-global/safe-price-service/workflows/Python%20CI/badge.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/safe-global/safe-price-service/badge.svg?branch=master)](https://coveralls.io/github/safe-global/safe-price-service?branch=master)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)
![Django 4](https://img.shields.io/badge/Django-4-blue.svg)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/safeglobal/safe-price-service?label=Docker&sort=semver)](https://hub.docker.com/r/safeglobal/safe-price-service)

# Safe Price Service
Returns fiat prices for base currencies and ERC20 tokens.

## Configuration

```bash
cp .env.sample .env
```

Configure environment variables on `.env`:
- `DJANGO_SECRET_KEY`: **IMPORTANT: Update it with a secure generated string**.
- `ETHEREUM_NODES_URLS`: Comma separated list of the node RPCS for the chains supported for fetching prices.
- `PRICES_CACHE_TTL_MINUTES`: Minutes to keep a price in cache.

## Execution

```bash
docker compose build
docker compose up
```

Then go to http://localhost:8000


## Contributors
[See contributors](https://github.com/safe-global/safe-price-service/graphs/contributors)
