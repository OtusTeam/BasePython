issue certs:

```shell
mkcert \
  -cert-file certs/localhost.pem \
  -key-file certs/localhost-key.pem \
  localhost 127.0.0.1 ::1
```

run https:

```shell
hypercorn app:app \
  --bind 127.0.0.1:8443 \
  --certfile certs/localhost.pem \
  --keyfile certs/localhost-key.pem
```
