# Hanashiai

Interface for easily browsing Reddit discussion threads.

## Running

Once you have cloned the repository you will need to create a self-signed certificate in the certs directory
with the following command:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./certs/hanashiai.com.key -out ./certs/hanashiai.com.crt
```

In the `docker-compose.yml` file under the `hanashiai` service, you'll need to update the `CLIENT_ID` and `CLIENT_SECRET`
environment variables with those of your Reddit app.

After that you'll be ready to start the containers:

```
./start_containers.sh
```

## License

[MIT](LICENSE) (c) Trevalyan Stevens
