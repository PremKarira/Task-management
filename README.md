# FastAPI and MongoDB based TASK-Management

## Features

+ Python FastAPI backend.
+ MongoDB database.

## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ python3 -m venv venv
```

2. You also need to start your mongodb instance either locally or on Docker as well as create a `.env` file. See the sample below for configurations.

```console
MONGO_URL=<url>
```

3. Start the application:

```console
$ python -m uvicorn main:app --reload
```

4. Build the Docker image and run the Docker container

```console
$ docker build -t task-docker .
$ docker run -p 8000:80 task-docker
```

![FastAPI](https://github.com/PremKarira/Task-management/blob/master/1.png?raw=true)



## License

This project is licensed under the terms of MIT license.