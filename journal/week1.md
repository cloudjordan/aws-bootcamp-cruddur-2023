# Week 1 — App Containerization

This week was my first time using containirzation. As something breifly touched on when I was studying for the AWS Cloud Practitioner exam, I was looking forward to getting hands on with this concept using Docker. The tasks I completed for this weeks homeworks are listed in the table below. 

| TASKS COMPLETED |
| :-------------- |
| Setting Up Docker Containers in the Gitpod Workspace |
| Setting Up The Backend of The Social Media Application |
| |
| |
| |
| |
| Container Security Considerations |
| Learning About Cloud Roles |

<br>


## 1. Setting Up Docker Containers in the Gitpod Workspace


<p>With Docker installed in Gitpod, I created a new `Dockerfile` in the `backend-flask` folder and added the following code to it. <p>
  
<p>This is the set of instructions I am using to build the Docker image. It is a self-contained piece of software that is used to run the image.<p>

<p>This means that anyone can use the image without having to make any changes to it. Regardless of the operating system being used, the Docker image will run:<p>

```
# Use the Python 3.10 slim image as the base
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /backend-flask

# Copy the dependencies file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the application code
COPY . .

# Set the Flask environment variable to development
ENV FLASK_ENV=development

# Expose the specified port
EXPOSE ${PORT}

# Start the Flask application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

```

I created a diagram in lucid charts which is shown below, to break down what is happening here: 
<br>
- The Gitpod host environment is a virtual machine running Linux.
- The workspace directory `/backend-flask` is located within the Gitpod host environment.
- The Docker container is a sub-environment created within the Gitpod host environment, using the Docker engine installed on the host.
- The guest OS is the operating system running inside the Docker container.
- The Docker container has a duplicate copy of the "/backend-flask" directory from the host environment, mounted as a volume inside the container.
<br>
Link to my Lucid Chart Diagram: https://lucid.app/lucidchart/fa37464f-661f-4279-86d8-bd6aa036a189/edit?viewport_loc=-78%2C-208%2C3196%2C1598%2C0_0&invitationId=inv_9b9bdea1-6c15-4aa6-ba67-c124cdcadb30
<br>
<br>
<p align="center">
  <img src="assets/docker-diagram.png" width="500">
</p>

<br>

To test the API endpoint, from `/workspace/aws-bootcamp-cruddur-2023`, I navigated to the backend-flask folder. To get it to run, I need to add some temp environment variables for the frontend and backend. I then started the flask application as shown below:

```
# Change directory
cd backend-flask

# Add environment variables
export FRONTEND_URL="*"
export BACKEND_URL="*"

# Run flask
python3 -m flask run --host=0.0.0.0 --port=4567

# Go back to main project directory
cd ..
```

I then unlocked the port to make it public in the "PORTS" tab, then clicked the port URL and added the extension needed `/api/activities/home` and was able to see the JSON data for the backend as show below: 

<p align="center">
<img src="assets/port-JSON-data.png" width="500">
</p>

#### Troubleshooting the backend
<p>I ran into issues the first time round where upon opening the port URL I received a "Not Found" error where the URL was not found on the server.<p>

<p>The server was running and accepting requests but they were returning a 404 HTTP status code. This was resolved by adding the temporary environment vairables I mentioned earlier.<p> 
  
<p>Now that it is working, I removed these temporary environment variables using the following command:<p>
  
  ```
unset FRONTEND_URL
unset BACKEND_URL  
  ```
---
#### Container setup for the backend

Back in the main directory `gitpod /workspace/aws-bootcamp-cruddur-2023 (main)` I ran the following code to build the container from the set of instructions I have set in the Dockerfile. This causes Docker to build the image using the set of instructions listed in the Dockerfile:
 
```
  
docker build -t  backend-flask ./backend-flask  
  
```
  
The image has now been created and is vsible under the image section in Gitpod. 

<p align="center">
  <img src="assets/docker-image.png" width="500">
</p>

With the image created, I ran the following command to create a container and run an instance of the image inside of it:

```
docker run --rm -p 4567:4567 -it backend-flask
```

As shown, the container is now created:

<p align="center">
  <img src="assets/docker-container.png" width="500">
</p>


As I will need frontend and backend URL environment variables, I added the following code:
```
set FRONTEND_URL='*'
set BACKEND_URL='*'
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
docker run --rm -p 4567:4567 -it  -e FRONTEND_URL -e BACKEND_URL backend-flask
unset FRONTEND_URL="*"
unset BACKEND_URL="*"
```

Confirmed the container was running by using the `docker ps` command which output the following:
```

CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                                       NAMES
96f1185b4de8   backend-flask   "python3 -m flask ru…"   9 minutes ago   Up 9 minutes   0.0.0.0:4567->4567/tcp, :::4567->4567/tcp   magical_bouman

```
---
#### Container setup for the frontend

Changed directory into front end directory `cd frontend-react-js/`

```
gitpod /workspace/aws-bootcamp-cruddur-2023/frontend-react-js (main) $
```

Installed node.js packages using: `npm i`. Frontend is using node.js

Once installed, in `frontend-react-js` directory I created a new `Dockerfile` and added the following instructions to it. Similar to how I did before:
```
FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js

WORKDIR /frontend-react-js

RUN npm install

EXPOSE ${PORT}

CMD ["npm", "start"]
```

---
#### Managing multiple containers with docker-compose 

I created a `docker-compose.yml` file in my root directory. This allows me to define and run multiple Docker containers as a single application.

<p align="center">
  <img src="assets/all-directories.png" width="500">
</p>


As I have a Flask backend and a Node.js frontend, each running in its own Docker container. Instead of manually starting each container with its own docker run command and setting up the necessary network connections and environment variables, I am using a `docker-compose` file:

```
version: "3.8"
services:
  backend-flask:
    environment:
      FRONTEND_URL: "https://3000-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
      BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./backend-flask
    ports:
      - "4567:4567"
    volumes:
      - ./backend-flask:/backend-flask
  frontend-react-js:
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js

# the name flag is a hack to change the default prepend folder
# name when outputting the image names
networks: 
  internal-network:
    driver: bridge
    name: cruddur
```

<p>To start the frontend and backend services I have configured in this file, I used the `docker compose up` command. It is doing a docker build and docker run on both the containers I created, while also configuring the environment variables and mounting etc.<p>
  
Now I have ports for the front end code and back end. With both ports unlocked/set to public, I can now view the URLs.  
  
<p align="center">
  <img src="assets/ports.png" >
</p>
<br>


## 2. Setting Up The Backend of The Social Media Application


