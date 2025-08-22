FROM jenkins/jenkins:lts

# Switch to root to install packages
USER root

# Install Python, venv, pip, git
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip git && \
    apt-get clean

# Switch back to Jenkins user
USER jenkins

