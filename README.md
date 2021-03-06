# Udacity Full Stack NanoDegree Capstone

## About this API
### Motivation
This API has been set up to help The Casting Agency, a company that is responsible for
creating movies and managing and assigning actors to those movies.
This system helps to simplify and streamline the process of managing and assigning actors.

### Where to find it
The API can be accessed at the following web address: https://udacity-fsnd.herokuapp.com/

The github repository link is: https://github.com/aj-cloete/udacity-fsnd-capstone

### API endpoints
The full documentation for the API can be found [here](./API.md)

## Authentication
### Roles

- Casting Assistant
  - Can view actors and movies
- Casting Director
  - All permissions a Casting Assistant has and...
  - Add or delete an actor from the database
  - Modify actors or movies
- Executive Producer
  - All permissions a Casting Director has and...
  - Add or delete a movie from the database

### login
To log in, go to https://udacity-fsnd.herokuapp.com/auth/login and use the pre-shared login/password credentials.


## Development
### Setup
This project uses `pipenv` to set up the development environment and docker images.
You can easily install `pipenv` by simply running `pip install pipenv`
and then use `pipenv install --dev` to set up the development environment.

You can use `docker` to stand up both the webserver and a postgres container by using `docker-compose` directly
or by making use of the `Makefile` commands:

#### Makefile
This project has a Makefile, providing easy access to the `docker-compose` commands.  Simply use one of the following:
- `make` to build the docker images required
- `make up` to stand up the web server and postgres database in docker
- `make db` to stand up just the database
- `make db-d` to stand up just the database and detach from the container (running in the background)
- `make down` to bring down the deployment you created when running `make up`
- `make test` to stand up the test environment (web server and postgres database)
- `make tests` to run the tests in the test environment and bring down the test environment afterwards
- `make test-db` to stand up just the test database
- `make down-test` to bring the test environment down again
- `make prune` to prune containers, networks, etc.  This helps if the other `make` commands stop working
- `make flask` to run a local flask but making sure postgres is running in the background
- `make upgrade` to upgrade the database
- `make migrate m="migrate message"` to run a migration with message passed in `m` as shown

#### Environment file
This project expects a `.env` file to work.  The file can be empty but may also be used to store things such as:

```
# ./.env
FLASK_ENV=DEVELOPMENT
DATABASE_URL=<your-database-url-here>
```

### Run the web server
To run the web server, simply use one of the tools provided:
- `flask run` if you're running your own database, and you've configured DATABASE_URL in the `.env` file
- `make flask` to bring up postgres in docker and run the flask app locally
- `make up` to bring up the deployment fully within docker using docker-compose.
