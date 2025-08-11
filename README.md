# House Price Prediction Model

A machine learning model powered with Random Forest Regressor. A single ML workflow performed within a python script and deployed in a Docker Image.

## Why do we predict house prices?

Honestly, there is no specific reason but to learn a Machine Learning model. But in this case I intended to deploy the model for me to learn how to maintain a model container lifecycle.

## This is publicly accessible.

When the image run on a container, it will handle requests via API. However, this will not be maintained frequently. 

## Key Features
- API accessible
- Containerized, easy to deploy

# How to use the model (Run existing Docker Image in Docker Hub)

1. Run existing docker image in Docker Hub.
```shell
docker run -p 8000:8000 --name house-price-container maulanaysfi/house-price-model
```

2. Access URL `http://localhost:8000`.

# How to build the image

1. Clone this repository and enter the current project directory.
2. Build the Docker Image.
```shell
docker build -t house-price-model .
```

3. Run the image.
```shell
docker run --name house-price-model -p 8000:8000 house-price-model
```
