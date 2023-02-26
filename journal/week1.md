# Week 1 — App Containerization

This week was my first time using containirzation. As something breifly touched on when I was studying for the AWS Cloud Practitioner exam, I was looking forward to getting hands on with this concept using Docker. The tasks I completed for this weeks homeworks are listed in the table below. 

| TASKS COMPLETED |
| :-------------- |
| Setting up Docker Containers |
| Setting up the backend API with Docker Compose |
| Setting up The Frontend Application with Docker Compose |
| Troubleshooting Issues |
| Installing Dynamo DB |
| Installing PostgresSQL |
| Container Security Considerations |
| Learning About Cloud Roles |

<br>


## Setting Up Docker Containers in the Gitpod Workspace


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

I then unloacked the port to make it public in the "PORTS" tab, then clicked the port URL and added the extension needed `/api/activities/home` and was able to see the JSON data for the backend as show below: 

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


Back in the main directory `gitpod /workspace/aws-bootcamp-cruddur-2023 (main)` I ran the following code to build the container from the set of instructions I have set in the Dockerfile. This causes Docker to build the image using the set of instructions listed in the Dockerfile:
 
```
  
docker build -t  backend-flask ./backend-flask  
  
```
  
The image has now been created and is vsible under the image section in Gitpod. 

  <p align="center">
  <img src="assets/docker-image.png" width="500">
</p>


