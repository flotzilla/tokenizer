# Tokenizer

Simple REST (ha-ha) service for tokenization

### Getting started
1. follow instructions in [senteser](https://github.com/flotzilla/sentenser_tes) app README file
2. Run sentenser `docker run -p 8082:8082 sentenser-0.0.1`
3. Run `docker-compose up -d` 
4. Send request, example: 
```bash
curl --request POST \
  --url http://0.0.0.0:5000/api/tokenize \
  --header 'Content-Type: application/json' \
  --data '{
	"text": "Good muffins cost $3.88 in New York.  Please buy me ntwo of them. Thanks"
}'
```

###### Possible improvements
**tokenizer**
* Reorganize config.py 
* Add dependency injection for a services
* Create tokenizer models instead of json handling by hand
* move to swagger and swaggerUI for better handling data models for main REST api
* implement logging

**[senteser](https://github.com/flotzilla/sentenser_tes)**
* coreNLP library can be used as standalone jar and can be executed from command line or service, 
wrapping around spring boot may not be the best solution in terms of saving memory and resources (memory consuming is around 2Gb idle)
* tomcat server under sping boot may be tuned `server.tomcat.max-threads`. Asynchronous processing can be used also 
* coreNLP can be used as [python package](https://stanfordnlp.github.io/stanfordnlp/)
* implement logging

**Overall**
* move infrastructure to etcd and kubernetes, to use service discovery and improve services extensibility
* Use protobuff and gRPC for communicating between services instead of REST and json approach may save some resources
* use additional dictionaries and rules for coreNLP 
* handle different languages
 
###### Implementation difficulties
* Confusions during implementing custom coreNLP `english.all.3class.distsim.crf.ser.gz` classifier. Didn't handle stacktrace errors.
