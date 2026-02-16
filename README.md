Snapp DevOps Task - Web Application Deployment

This project demonstrates a complete CI/CD pipeline and GitOps workflow for deploying a simple web application to a Kubernetes cluster.

📖 Table of Contents
Project Overview
Architecture
Features
Prerequisites
Getting Started
1. Infrastructure Setup (Ansible)
2. GitLab CI/CD Configuration
3. Deployment with ArgoCD
Security Considerations
Author



🚀 Project Overview
The goal of this task is to deploy a containerized web application using best practices in DevOps, including:

Configuration as Code (CaC): Using Ansible for GitLab Runner setup.
Containerization: Dockerizing a Python (FastAPI/Uvicorn) application.
Orchestration: Deploying to Kubernetes with Ansible using Kube-spray 
GitOps: Managing deployments via ArgoCD.
CI/CD: Automated build and manifest update using GitLab CI.



🏗 Architecture
The solution is designed with a separation of concerns:

Application Namespace (snapp-project): Hosts the core web application.
Proxy Namespace (nginx-gateway): Hosts an Nginx reverse proxy to handle ingress traffic.
Traffic Flow:User -> Nginx Ingress -> Nginx Proxy (nginx-gateway) -> Web App Service (snapp-project)


✨ Features
✅ Helm Charts: Modular and reusable manifests for App and Nginx Proxy.
✅ GitOps (ArgoCD): Automated sync and deployment from Git repository.
✅ CI/CD (GitLab): Automated Docker builds and manifest updates on new tags.
✅ Zero-Downtime Deployment: RollingUpdate strategy with Readiness/Liveness probes.
✅ Auto-Scaling (HPA): Horizontal Pod Autoscaler based on CPU utilization.
✅ Security Best Practices:
Non-root containers (runAsNonRoot).
Network Policies to restrict traffic.
Resource limits and requests defined.


⚙️ Prerequisites
Kubernetes Cluster
kubectl installed and configured.
Ansible installed (for runner setup).
GitLab account and repository.
ArgoCD installed on the cluster.


🏃 Getting Started
1. Infrastructure Setup (Ansible)
A GitLab Runner is required to execute CI/CD pipelines. The setup is automated using Ansible.

ansible-playbook playbook.yaml -i inventory.ini -u git-runner -bK
This installs the GitLab Runner and registers it with the GitLab instance.

2. GitLab CI/CD Configuration
Ensure the following CI/CD Variables are set in your GitLab project settings (Settings > CI/CD > Variables):

DEPLOY_TOKEN: A GitLab Deploy Token with write_repository scope (used for pushing changes to the manifest).
Pipeline Stages:

Build: Builds the Docker image and pushes it to the registry.
Update Manifest: Updates the values.yaml in the Helm chart with the new image tag (GitOps trigger).

3. Deployment with ArgoCD
Install ArgoCD in your cluster.
Create an ArgoCD Application pointing to this repository:
Path: snapp-chart (for the web app).
Namespace: snapp-project.
Enable Auto-Sync for automated reconciliation.
(Repeat similarly for the Nginx Proxy chart located in nginx-chart).

🛡 Security Considerations
This deployment implements several security measures:

Non-root User: The Dockerfile and Helm chart ensure the application runs as a non-privileged user (runAsUser: 1000).
Network Policies: Implemented to restrict ingress traffic. Only traffic from the nginx-gateway namespace or specific pods is allowed.
Resource Management: CPU and Memory limits are strictly defined to prevent resource exhaustion attacks.
Health Probes: Liveness and Readiness probes ensure traffic is only routed to healthy pods.



📂 Directory Structure

.
|__ k8s-manifests           # Contain all the manifests
├── snapp-chart/            # Helm Chart for Web Application
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── nginx-chart/            # Helm Chart for Nginx Proxy
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── .gitlab-ci.yml          # GitLab CI Pipeline definition
├── Dockerfile              # Multi-stage Docker build
└── README.md

📝 Author
Mohammad Reza