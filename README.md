# Futureskills DevOps Engineer Assignment

# update to test github actions

## Overview

This project demonstrates a multi-container platform using Docker, NGINX, Apache, and Python Flask, with CI/CD automation and security best practices.

## Architecture

- **NGINX**: Reverse proxy, single entry point, routes `/` to Apache and `/api` to Flask backend.
- **Apache**: Serves static HTML content.
- **Flask API**: Provides `/api/health` endpoint.
- **Docker Compose**: Orchestrates all services, custom network for isolation.
- **CI/CD**: Automated with GitHub Actions.

## Directory structure

- docker
- apache # apache web server
  - dockerfile
  - static-html-dir
  - index.html # static html content
- nginx # nginx reverse proxy
  - dockerfile
  - conf
  - nginx.conf # nginx configuration file
- phthonapi # python api service
  - dockerfile
  - python
  - health.py # flask api with health check endpoint
- docker-compose.yml # docker compose file for multi container setup
- readme.md # project documentation

## Security

- NGINX blocks TRACE/OPTIONS methods.
- Sets security headers (`X-Frame-Options`, `Content-Security-Policy`).
- Only NGINX is exposed to host.

## How to Run

### Start All Services (App + Logging)

1. Clone repo and navigate to `Futureskills/docker`
2. Build and start all services (including ELK logging stack):

   ```bash
   docker-compose up --build
   ```

3. Test application endpoints:
   - `curl -i http://localhost` (should show HTML and NGINX headers)
   - `curl -i http://localhost/api/health` (should show `{ status: "ok" }`)

### View Logs in Kibana

1. Open Kibana in your browser: [http://localhost:5601](http://localhost:5601)
2. Use the "Discover" tab to search and view logs from all containers (NGINX, Apache, Python API).

## Linux Fundamentals

- File permissions managed via `chmod`/`chown`.
- Connectivity tested with `curl`, `ping`, `ip a`.
- Network isolation verified with Docker CLI.

## CI/CD Pipeline

- On push: builds images, lints Dockerfiles, validates Compose, tests containers, tags images, redeploys.

## Advanced Features

- HTTPS via NGINX (self-signed certs, config in `nginx.conf`).
- Health checks for all services.
- Environment variables via `.env`.
- Auto-restart and load balancing (NGINX upstream config).
- Centralized logging stack (add ELK/Loki as needed).

- Health checks for all services.
- Environment variables via `.env`.
- Auto-restart and load balancing (NGINX upstream config).
- Centralized logging stack (add ELK/Loki as needed).

## Documentation

- See assignment markdown for full requirements and evaluation criteria.
- Architecture diagram and test plans included at expert level.
