# 🔐 Secure API Platform Demo

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Security](https://img.shields.io/badge/Security-Authentication%20%26%20Hashing-critical)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)

A **secure backend API platform demo** built with **FastAPI**, **PostgreSQL**, and **Docker**.  
This project demonstrates **modern backend, platform, and security best practices** in a clean, beginner‑friendly way.

---

## 📑 Table of Contents

- [🧠 What This Project Demonstrates](#-what-this-project-demonstrates)
- [🏗️ Architecture Overview](#️-architecture-overview)
- [🔐 Security Design](#-security-design-plain-english)
  - [Passwords Are Never Stored](#passwords-are-never-stored-directly)
  - [Why We Pre-Hash Before Bcrypt](#why-we-pre-hash-before-bcrypt)
- [🧪 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started-step-by-step)
- [🧪 Testing the API](#-testing-the-api)
- [🔑 JWT Tokens](#-jwt-tokens)
- [🛡️ Why This Repo Is Secure by Design](#️-why-this-repo-is-secure-by-design)
- [📚 Who This Repository Is For](#-who-this-repository-is-for)
- [🧩 Possible Extensions](#-possible-extensions)

---

## 🧠 What This Project Demonstrates

This repo covers **real-world production concepts**, including:

- Secure password handling (bcrypt done correctly)
- JWT-based authentication
- Database-backed user accounts
- Environment-based configuration
- Dockerized infrastructure
- Clear separation of concerns (API, security, DB)
- Defensive programming and logging

---

## 🏗️ Architecture Overview

```mermaid
flowchart TD
    A[Client<br/>(curl / frontend)] --> B[FastAPI Application]

    B --> C1[Auth Routes<br/>(/auth/register, /auth/login)]
    B --> C2[Security Layer<br/>(hashing, JWTs)]
    B --> C3[Database Session Handling]

    B --> D[(PostgreSQL Database<br/>(Docker))]
```


---

## 🚀 Getting Started (Step by Step)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/secure-api-platform-demo.git
cd secure-api-platform-demo
```

### 2️⃣ Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ Create the .env file

DATABASE_URL=postgresql+psycopg2://postgres:postgres@127.0.0.1:5433/demo
JWT_SECRET=replace_with_a_long_random_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXP_MINUTES=60

### 5️⃣ Start PostgreSQL using Docker

docker compose up -d

Verify the container is running: docker ps

### 6️⃣ Create database tables

python -m app.db.init_db

### 7️⃣ Start the API server

uvicorn app.main:app --reload --log-level debug

The API will be available at:

http://127.0.0.1:8000


### 🧪 Testing the API

Health check:

curl http://127.0.0.1:8000/health

Response: 

{"status": "ok"}

Register a user:

curl -i -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"StrongPassword123!"}'

Login:

curl -i -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"StrongPassword123!"}'

### 🔑 JWT Tokens
On successful registration or login, the API returns a JWT access token.

This token can be used to:

- authenticate protected endpoints
- identify the user
- enforce authorization rules


### 🛡️ Why This Repo Is Secure by Design

- No plaintext passwords
- bcrypt used safely (no truncation bugs)
- Secrets kept out of source control
- Defensive assertions
- Explicit logging of security paths
- Clear separation of layers

### 📚 Who This Repository Is For: 

- Beginner computer science students
- Developers learning secure authentication
- Engineers transitioning into DevOps / Platform / Security roles


### 🧩 Possible Extensions:

- Add refresh tokens
- Add role-based access control
- Add rate limiting
- Add CI/CD pipeline
- Add Infrastructure as Code (Terraform)
- Add metrics and monitoring


---

## ✅ Running Tests

This repo includes a small set of high-signal tests focused on the most important security and platform behaviors:

- **Security invariants** (password hashing/verification and bcrypt safety)
- **Auth happy path** (register + login returns JWT)
- **Health endpoint** (basic uptime check)

### Run tests locally (recommended for beginners)

Make sure your virtual environment is activated and dependencies are installed:

```bash
source .venv/bin/activate
pip install -r requirements.txt

docker compose up -d
pytest -q
```





