This is my portfolio version 2

##Tech:
- python3.6
- sanic (backend)
- vuejs (frontend)
- docker

# Sections
- [How to run the project locally](#how-to-run-the-project)

## How to Run the project
1. [using python](#run-locally-using-python)
2. [using dockler](#run-locally-using-docker)

##Run locally using python
1. Clone the project
2. Create a virtual environment with python3.6
```sh
# create a virtual environment
virtualenv venv --python=python3.6

# activate the environment
source venv/bin/activate
```
3. Install the required python packages
```sh
# this should install all required python packages
pip install -r requirements.txt
```

5. Install npm and npm packages then do a build
```sh
# this will install the required package of this project
npm install
# build
npm run build:dev
# or for production
npm run build:prod
```
4. Run the project
```sh
# this will spawn a python server in localhot:8000
python manage.py
```
5. to stop, just do the usual `CTRL` + `C` to terminate

##Run locally using docker
1. Clone the project
2. Install docker if you don't have it yet [instruction/guide](https://docs.docker.com/get-started/#prepare-your-docker-environment)
3. Install npm and npm packages then do a build
```sh
# this will install the required package of this project
npm install
# build
npm run build:dev
# or for production
npm run build:prod
```
4. Do a Docker build
```sh
# since we have the Dockerfile in another folder, we use  -f to specify its location but still build from the root directory
docker build -f /docker/Dockerfile . -t portfolio:v1
```
5. Run the newly built docker image locally
```sh
# -d means to run in background so you can reuse the terminal for other stuff
docker run -d -p 8000 -t portfolio:v2
```
6. to stop, just call the docker stop {CONTAINER_ID} then its done
```
# to know the docker container ID do
docker ps
# docker ps will list all running containers
docker stop 09ba4d9f6fae
# ^ that will stop the running container with a container ID of 09ba4d9f6fae
```
