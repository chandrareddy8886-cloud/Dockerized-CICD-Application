# Dockerized CI/CD Application

A production-style FastAPI service demonstrating containerization, automated testing, continuous integration, Docker image builds, and release automation through GitHub Actions.

## Architecture

Developer -> Git Push -> GitHub Actions -> Tests -> Docker Build -> Container Registry

For tagged releases:

`git tag v1.0.0 && git push origin v1.0.0`

The release workflow builds and publishes the Docker image to GitHub Container Registry.

## Features

- FastAPI REST service
- Health endpoint
- Version endpoint
- Environment-based configuration
- Docker containerization
- Docker Compose local development
- Pytest automated tests
- GitHub Actions CI
- Docker image build verification
- Automated image publishing on version tags

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

`http://localhost:8000/docs`

## Run with Docker

```bash
docker compose up --build
```

Check:

`http://localhost:8000/health`

## Run tests

```bash
pytest -q
```

## CI pipeline

Every push to `main` and every pull request:

1. Checkout source
2. Install Python
3. Install dependencies
4. Run automated tests
5. Build Docker image
6. Verify image exists

## Release pipeline

A semantic version tag such as `v1.0.0` triggers the release workflow.

The workflow:

1. Checks out the repository
2. Authenticates to GitHub Container Registry
3. Generates image metadata
4. Builds the Docker image
5. Pushes the image to GHCR

## Interview talking points

- Why containerize an application?
- Difference between an image and a container
- Why use Docker Compose locally?
- What does CI solve?
- What is the difference between CI and CD?
- Why should tests run before building/releasing?
- Why use GitHub Container Registry?
- What are image tags and why should releases be versioned?
- How would you deploy this to AWS?
- How would you add rollback and health checks?
