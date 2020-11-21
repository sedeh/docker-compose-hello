# docker-compose hello world

This repo demonstrates the basic set up for docker-compose. 

To run the application, execute `docker-compose up --detach --build`

To view the log of any of the running containers, execute `docker logs --follow <container_name>`

If the application is successful, `curl http://localhost:5000/` will output something like:

```
{"0d4b12902836":"hello from app2","9a249436c169":"hello from main","eca1050ca226":"hello from app1"}
```
Essentially, the main container is listening on port 5000 and the other containers are listening on ports 6000 and 7000.

The output shows we were able to reference a custom-defined and a native environment variables.

To tear down the application, execute `docker-compose down`

# References
- Install docker-compose community edition: https://docs.docker.com/compose/install/ 
