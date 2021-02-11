![Python application test with Github Actions](https://github.com/noahgift/Python-Functions-from-Zero/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

# Python-Functions-from-Zero
this is a repo for building Python functions from Zero

## Getting Started

* Create scaffold:  `Makefile`, `requirements.txt`, `hello.py`

* Create a virtualenv: `virtualenv ~/.python-functions-zero`

* Source it:  `source ~/.python-functions-zero/bin/activate`

### Run CLI

` ./cli.py  --color "red"`

### Test project

`make lint && make test`

### Containerize this project

You can [read this sample project](https://github.com/noahgift/container-from-scratch-python)

#### Build

`docker build --tag=cli-aws .`

#### Run

`docker run -it cli-aws python cli.py --color "Red"`


#### Pull it

`docker pull noahgift/cli-aws`

### Serverless

```python
def lambda_handler(event, context):
    print(f"This is the event {event}")
    if event["name"] == "Marco":
        return "Polo"
    return "No!"
```

`aws lambda invoke --function-name <MyFunction> \
    --payload '{"name": "Bob" }' out.txt`    

### Deploy to A Container as a Service

https://github.com/noahgift/cloudrun-flask
