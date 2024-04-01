# memoires-bff
The backend-for-frontend (BFF) API for the memoires project.

## Application relationships

The resources required in this API require the database and endpoints served
by:

- [memoires-api](https://github.com/evanjt/memoires-api)

and supports the following applications:

- [memoires-ui](https://github.com/evanjt/memoires-ui)

## Getting started

To start the app run:

```
    poetry run uvicorn app.main:app --reload
```
