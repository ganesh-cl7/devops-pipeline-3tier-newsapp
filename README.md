# DevOps 3-Tier News App

A simple project demonstrating a CI/CD pipeline integrating a Flask backend with a React frontend. This repository includes Docker configuration and GitHub Actions workflows for automated testing and deployment, along with Ansible automation for deploying on AWS EC2.
---

## Project Overview

This project replicates **real-world DevOps practices**.
The app fetches **live news** from an API and displays it in a modern, responsive UI.

---

## Tech Stack

### **Frontend**

* React.js
* TailwindCSS
* Axios (API calls)

### **Backend**

* Flask (Python)
* REST API integration with News API
* MongoDB connection

### **Database**

* MongoDB (NoSQL)
* Stores news data for quick retrieval

### **DevOps Tools**

* **Git & GitHub** – Source Code Management
* **Docker** – Containerization of frontend, backend, and database
* **Docker Compose** – Multi-container setup
* **Jenkins** – CI/CD automation
* **Ansible** – Deployment on AWS EC2
* **AWS EC2** – Cloud hosting
* **Nginx** – Reverse proxy

---

## 1. Clone the Repository

```bash
git clone https://github.com/ganesh-cl7/devops-pipeline-3tier-newsapp.git
cd devops-pipeline-3tier-newsapp
```

---

## 2. Run Locally with Docker

Build and start the services with Docker Compose:

```bash
docker-compose up --build
```

* **Frontend:** http://localhost:3000
* **Backend API:** http://localhost:5000

---

## 3. Deploy on AWS EC2 with Ansible

**Steps:**

1. Launch an AWS EC2 instance (Ubuntu recommended)
2. Install Docker and Docker Compose on the EC2
3. Update the Ansible inventory file with your EC2 IP

Run:

```bash
ansible-playbook deploy.yml
```

---

## Features

1. Live news updates via News API
2. Fully containerized setup
3. CI/CD automation with Jenkins
4. Deployment automation with Ansible
5. Scalable 3-tier architecture
6. MongoDB caching for faster load times
7. Responsive UI with TailwindCSS

