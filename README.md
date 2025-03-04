# Small instructs

To update configuration (set host and redirect each n requests) use `/api/v1/cdn`


redirect_each_n_requests <= 0 all requests will be redirected to original host


redirect_each_n_requests > 0 every n requests will be redirected to CDN

# How to run in prod

```bash
cp .env.example .env

docker compose up -d --build
```

# How to run in dev

```bash
cp .env.example .env

ln -s ./docker-compose.dev.override.yml ./docker-compose.override.yml

docker compose up -d --build
```