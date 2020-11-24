# docker-compose hello world

This repo demonstrates the basic set up for docker-compose. 

Run the application: `docker-compose up --detach --build`

View the log of one of the running container, e.g. main: `docker logs --follow main`

Test the app: `curl http://localhost:5000/` 

If the application is successful, you will see an output like:

```
{"0d4b12902836":"hello from app2","9a249436c169":"hello from main","eca1050ca226":"hello from app1"}
```
Essentially, the main container is listening on port 5000 and the other containers are listening on ports 6000 and 7000.

The output shows we were able to reference a custom and a native environment variables.

Tear down the app: `docker-compose down`

# References
- Install docker-compose community edition: https://docs.docker.com/compose/install/ 
