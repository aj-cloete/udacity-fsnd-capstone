# API
The API is accessible here: https://udacity-fsnd.herokuapp.com

More info on this project in the [README.md](./README.md)

## Endpoints
The API has the following two models:

- Movies: https://udacity-fsnd.herokuapp.com/movies
- Actors: https://udacity-fsnd.herokuapp.com/actors

with corresponding endpoints:

### Movies

`GET` https://udacity-fsnd.herokuapp.com/movies

- **request:** get all movies in the database
- **response:** an array containing `movie` objects

    ```
    [
        {
            "release_date":"2000-06-05",
            "title":"Gone in Sixty Seconds",
            "actors":[
                ...
            ],
            "uuid":"e57d1be3-8617-4e05-bdc2-6172a27acf1a"
        },
        {
            ...
        }
    ]
    ```

`POST` https://udacity-fsnd.herokuapp.com/movies

- **request:** create a new movie object in the database

  **request body:**

    ```
    {
        "title": a string field containing the name of the movie,
        "release_date": the release date of the movie (can be in the future)
        "actor_uuid": (optional) [list of] string of the uuid(s) of the actor(s) associated with this movie
    }
    ```

- **response:** the created movie object, for example:

    ```
    {
        "release_date": "2000-06-05",
        "title": "Gone in Sixty Seconds",
        "actors": [],
        "uuid": "e57d1be3-8617-4e05-bdc2-6172a27acf1a"
    }
    ```

`GET` https://udacity-fsnd.herokuapp.com/movies/<movie_url>
- **request:** get the specific movie with uuid = <movie_url>
- **response:**

    ```
    {
        "release_date": "2000-06-05",
        "title": "Gone in Sixty Seconds",
        "actors": [],
        "uuid": "e57d1be3-8617-4e05-bdc2-6172a27acf1a"
    }
    ```

`PATCH` https://udacity-fsnd.herokuapp.com/movies/<movie_url>
- **request:** UPDATE the specific movie with uuid = <movie_url>
- **request_body:**

```
    {
        "title": (optional) a string field containing the name of the movie,
        "release_date": (optional) the release date of the movie (can be in the future)
        "actor_uuid": (optional) [list of] string of the uuid(s) of the actor(s) associated with this movie
    }
```

- **response:** the updated movie from the database

    ```
    {
        "release_date": "2030-06-05",
        "title": "Gone in Seventy Seconds",
        "actors": [],
        "uuid": "e57d1be3-8617-4e05-bdc2-6172a27acf1a"
    }
    ```

`DELETE` https://udacity-fsnd.herokuapp.com/movies/<movie_url>
- **request:** DELETE the specific movie with uuid = <movie_url>
- **response:** the uuid of the movie that was deleted from the database

    ```
    "e57d1be3-8617-4e05-bdc2-6172a27acf1a"
    ```

### Actors

`GET` https://udacity-fsnd.herokuapp.com/actors

- **request:** get all actors in the database
- **response:** an array containing `actor` objects

    ```
    [
        {
            "surname":"Jones",
            "name":"James",
            "uuid":"fe91d866-d895-422d-bc09-fd2075a0c844",
            "movies":[
                {
                    "title":"The Lion King",
                    "uuid":"c9546ff0-c305-447e-8008-d6574b22cd1d",
                    "release_date":"1994-05-06"
                }
            ],
            "age":90,
            "gender":"M"
        },
        {
          ...
        }
    ]
    ```

`POST` https://udacity-fsnd.herokuapp.com/actors

- **request:** create a new actor object in the database

  **request body:**

    ```
    {
        "name": (string) name of the actor ,
        "surname": (string) surname of the actor,
        "age":90 (int) the age of the actor,
        "gender":"M" (string(1)) the gender of the actor,
        "movie_uuid": (optional: string, array of strings) the uuid of the associated movie(s)
    }
    ```

- **response:** the created actor object, for example:

    ```
    {
        "surname": "Jones",
        "name": "James",
        "uuid": "fe91d866-d895-422d-bc09-fd2075a0c844",
        "movies": [
            {
                "title": "The Lion King",
                "uuid": "c9546ff0-c305-447e-8008-d6574b22cd1d",
                "release_date": "1994-05-06"
            }
        ],
        "age": 90,
        "gender": "M"
    }
    ```

`GET` https://udacity-fsnd.herokuapp.com/actors/<actor_url>
- **request:** get the specific actor with uuid = <actor_url>
- **response:**

    ```
    {
        "surname": "Jones",
        "name": "James",
        "uuid": "fe91d866-d895-422d-bc09-fd2075a0c844",
        "movies": [
            {
                "title": "The Lion King",
                "uuid": "c9546ff0-c305-447e-8008-d6574b22cd1d",
                "release_date": "1994-05-06"
            }
        ],
        "age": 90,
        "gender": "M"
    }
    ```

`PATCH` https://udacity-fsnd.herokuapp.com/actors/<actor_url>
- **request:** UPDATE the specific actor with uuid = <actor_url>
- **request_body:**

```
    {
        "name": (string) name of the actor ,
        "surname": (string) surname of the actor,
        "age":90 (int) the age of the actor,
        "gender":"M" (string(1)) the gender of the actor,
        "movie_uuid": (optional: string, array of strings) the uuid of the associated movie(s)
    }
```

- **response:** the updated actor from the database

    ```
    {
        "surname": "Jones",
        "name": "James",
        "uuid": "fe91d866-d895-422d-bc09-fd2075a0c844",
        "movies": [
            {
                "title": "The Lion King",
                "uuid": "c9546ff0-c305-447e-8008-d6574b22cd1d",
                "release_date": "1994-05-06"
            }
        ],
        "age": 90,
        "gender": "M"
    }
    ```

`DELETE` https://udacity-fsnd.herokuapp.com/actors/<actor_url>
- **request:** DELETE the specific actor with uuid = <actor_url>
- **response:** the uuid of the actor that was deleted from the database

    ```
    "fe91d866-d895-422d-bc09-fd2075a0c844"
    ```
