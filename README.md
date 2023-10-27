### Deployment:
1) ``clone this repo via https``
2) ``docker-compose up -d``

### API Spec:
1) GET `/api/v1/` will return all existing key-value pairs in the db
2) POST `/api/v1/` {"key": \<your key here\>, "value": \<your value here\>} will add new key-value pair into db
3) GET `/api/v1/<your key here>` will return info about the existing key
4) PUT `/api/v1/<your key here>` will modify the existing key