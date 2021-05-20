## Setup/run instructions

Create .env file and add a secret key

```
SECRET_KEY={}

```

Run the following command to get started:
```
docker-compose up -d --build
```

## POST /api/v1/tasks/create/

+ ### Request
```
/api/v1/tasks/create/
```

+ ### Body

```
{
    "url": "www.google.com/"
}
```
+ ### Response 200
```
{
    "identifier": "IuJ5Rhek"
}
```

## GET api/v1/tasks/\<str:identifier>/

Get the result
+ ### URL parameters
    + `<str:identifier>` - the identifier of the task

+ ### Request
```
/api/v1/tasks/IuJ5Rhek/
```

* ### Response 200
```
{
    "html": {
        "count": 1,
        "nested": 7
    },
    "head": {
        "count": 1,
        "nested": 4
    }
}
```