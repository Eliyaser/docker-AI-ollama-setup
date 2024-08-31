# Ollama Docker Setup

This repository contains scripts and configurations to run and interact with the Ollama AI model using Docker.

## Getting Started

### Step 1: Pull the Docker Image

First, pull the latest Ollama image from Docker Hub:

```bash
docker pull ollama/ollama:latest

$docker run -d -p 11434:11434 --name ollama_test ollama/ollama

$docker exec -it <containerID> /bin/bash

```
or 
using your docker desktop UI have this option.

### Step 2: Run the Docker Container
```bash
docker run -d -p 11434:11434 --name ollama_test ollama/ollama
```
### Step 3: Access the Container
```bash
docker exec -it <containerID> /bin/bash
```

### Step 4: Get Available Models
#### Once inside the container, list all available models:
```bash
ollama list

```
### Step 5: Pull the TinyLlama Model
#### To pull the TinyLlama model, run:
```bash
ollama pull tinyllama

```
### Step 6: Run the TinyLlama Model
#### Execute the following command to run the TinyLlama model:
```bash
ollama run tinyllama
```
# Accessing the Model via Python
### Navigate to the directory containing main.py.
#### Open a terminal in that directory.
### Step 1: Install the requests Library
Ensure that the requests library is installed:
```bash
pip install requests
````
### Step 2: Send a Request to the AI Model
Run the Python script to interact with the model:

```bash
python .\main.py
```


### To stop the running container:

```bash
Copy code
docker stop ollama_test.
```
### Remove Exited Containers
#### Clean up any exited containers:

```bash
Copy code
docker rm $(docker ps -a -f "status=exited" -q)

```
