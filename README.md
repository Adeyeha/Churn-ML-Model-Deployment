## Churn Prediction ML Model Deployment with FastAPI and Docker
This project is a demonstration of deploying a churn prediction machine learning model using FastAPI and Docker. The model takes customer data as input and returns a prediction of whether the customer is likely to churn or not. The API is built using FastAPI, a fast and easy-to-use web framework for building APIs, and the model is packaged and deployed as a Docker container.

### Requirements
- Docker
- Python 3.x
- Required libraries: FastAPI, scikit-learn, pandas, cx_Oracle etc.

### Installations
- Install docker EE for windows server [here](https://computingforgeeks.com/how-to-run-docker-containers-on-windows-server-2019/)
- Install compose for windows server [here](https://cloudinfrastructureservices.co.uk/how-to-install-docker-compose-on-windows-server-2016-2019-2022/)
- Create local certs [here](https://github.com/FiloSottile/mkcert)

### How to run
Clone the repository and navigate to the directory.

``` sh
git clone https://github.com/Adeyeha/Churn-ML-Model-Deployment.git
cd <repo-directory>
```
Build the Docker image:

``` sh
docker build -t <image_name> .
```
Replace <image_name> with the desired name for the Docker image.

Run the Docker container:
```sh
docker run -p 8000:8000 <image_name>
```
The API will be available at http://localhost:8000/.
### API Endpoints
The API provides the following endpoints:
- /docs: Swagger API documentation.
- /predict: Accepts customer data as input and returns a prediction of whether the customer is likely to churn or not.

### Contributing
If you want to contribute to this project, please create a pull request with a detailed description of your changes.

### License
MIT
### Author
[Temitope Adeyeha](https://github.com/Adeyeha)

