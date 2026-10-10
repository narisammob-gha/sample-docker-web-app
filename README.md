# Sample Docker Web App

A tiny Python web app that serves a page on port `8080`. It uses only the Python standard library, so no dependency installation is needed.

## 1. Build the image

Run these commands from the repository directory:

```bash
docker build -t sample-web-app:1.0 .
```

## 2. Run the container

```bash
docker run -d --name sample-web-app -p 8080:8080 sample-web-app:1.0
```

The app listens on `0.0.0.0` inside the container. The `-p 8080:8080` option publishes container port 8080 on host port 8080.

## 3. Open it in a browser

- On the same machine: http://localhost:8080
- From another machine: `http://<HOST_IP>:8080`

To find the host IP on Linux, run `hostname -I`. On Windows, run `ipconfig`; on macOS, run `ipconfig getifaddr en0` (Wi-Fi is commonly `en0`).

If connecting from another machine, make sure the host firewall/security group allows inbound TCP port `8080`.

## Useful commands

```bash
# View logs
docker logs -f sample-web-app

# Test health endpoint
curl http://localhost:8080/health

# Stop and remove the container
docker rm -f sample-web-app
```

## Change the host port

To access it on host port 9000 instead:

```bash
docker run -d --name sample-web-app -p 9000:8080 sample-web-app:1.0
```

Then open `http://<HOST_IP>:9000`.
