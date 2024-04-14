### set the sites
1. put sitelist you want to study in sitelist.py

2. don't forget to run chromadb

3. run setter.py
```poetry run python src/setter.py```


### get the answer
1. run the server
```poetry run uvicorn main:app --port 8001```

2. ask question
```
curl -d '{"question": "create an example of writing an express app that outputs hello world as a response."}' \
 -H "Content-Type: application/json" \
 -X POST http://localhost:8001/
```

```
// window
curl -d "{""question"": ""create an example of writing an express app that outputs hello world as a response.""}" -H "Content-Type: application/json" -X POST http://localhost:8001/
```
