+++
title = "Documents service (Django)"
api_url = "marketplace/documents-service"
+++

# Documents service (Django)

## Overview

The documents service provides the backend with an API for storing static files
in an Amazon S3 Bucket and retrieving them. 

It exposes the Document data model, which holds all data about a file 
and endpoints for retrieving the file or thumbnail directly.  


## REST Data models

### Document

A _Document_ is representation of a stored file. It includes the following properties::

- **id**: ID of the document.
- **uuid**: UUID of the document.
- **file**: The actual file which was uploaded.
- **thumbnail**: A thumbnail created from the file, if it was in PNG-, GIF- or JPEG-format.
- **file_description**: Textual description about the file.
- **file_name**: Name of the file.
- **upload_date**: Date when the document was first created (automatically set).
- **create_date**: Date, which is not automatically set.
- **organization_uuid**: Organization of the document.
- **user_uuid**: User of the document.
- **contact_uuid**: Contact of the document.
- **workflowlevel1_uuids**: Workflowlevel1s related to the document.
- **workflowlevel2_uuids**: Workflowlevel2s related to the document.

#### Endpoints

-  `GET /documents/`: Retrieves a list of documents.
-  `POST /documents/`: Creates a new document.
-  `GET /documents/{id}/`: Retrieves a documents by its ID.
-  `PUT /documents/{id}/`: Updates the document with the given ID (all fields).
-  `PATCH /documents/{id}/`: Updates the document with the given ID (only specified fields).
-  `DELETE /documents/{id}/`: Deletes the document with the given ID.

## Non-model endpoints

-  `GET /documents/file/{id}`: Retrieves the file attached to the document with the given ID.
-  `GET /documents/thumbnail/{id}`: Retrieves the thumbnail attached to the document with the given ID.

## Local development

### Prerequisites

You must have [Docker](https://www.docker.com/) installed.

### Deploy locally via Docker

Build first the images:

```bash
docker-compose build # --no-cache to force deps installation
```

To run the webserver:

```bash
docker-compose up # -d for detached
```

Open your browser with URL `http://localhost:8004`. For the admin panel
`http://localhost:8004/admin` (user: `admin`, password: `admin`).

The documentation can be consulted in `http://localhost:8004/docs`.


### Development utils

To run the tests only once:

```bash
docker-compose run --entrypoint 'bash scripts/run-tests.sh' --rm documents_service
```

To run the tests and open the bash when they are finished - useful to allow
you work faster if you want to run them more than once:

```bash
docker-compose run --entrypoint 'bash scripts/run-tests.sh --bash-on-finish' --rm documents_service
```

To run bash:

```bash
docker-compose run --entrypoint 'bash' --rm documents_service
```

## Deploy to server

### Environment Variables

The following environment variables need to be configured in order to make 
the service work correctly:

-  `ALLOWED_HOSTS`
-  `CORS_ORIGIN_WHITELIST`
-  `DATABASE_ENGINE` 
-  `DATABASE_NAME` 
-  `DATABASE_USER` 
-  `DATABASE_PASSWORD` 
-  `DATABASE_PORT` and `DATABASE_HOST` are optional
 
 If AWS S3 Buckets should be used for storing documents the following 
 settings are required as well:
 
 -  `AWS_ACCESS_KEY_ID`
 -  `AWS_ACCESS_KEY_SECRET`
 -  `AWS_S3_BUCKET`

## API documentation (Swagger)

[Click here for the full API documentation.](https://docs.walhall.io/api/marketplace/documents-service/)

## License

Copyright &#169;2019 Humanitec GmbH.

This code is released under the Humanitec Affero GPL. See the **LICENSE** file for more information.
