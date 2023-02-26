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


With Docker installed in Gitpod, I created a new Docker file in the the backend-flask folder and used the following code to create my docker container. I created a diagram in lucid charts which is shown below, to break down what is happening here: 

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

From /workspace/aws-bootcamp-cruddur-2023, I navigated to the backend-flask folder. To get the application to run, I need to add some environment variables for the frontend and backend. I then started the flask application as shown below. 

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

I then unloacked the port to make it public in the "PORTS" tab, then clicked the port URL and added the extension needed `/api/activities/home` and was able to see the JSON data for the backend. 







Inside the backend-flask directory in my host environment, I installed flask and the other necessary python packages needed for the application. Then started the application with the last line of code listed below:

```
# Changed directory to workspace directory
/workspace/aws-bootcamp-cruddur-2023 (main) $ cd backend-flask/

# Installed required python packages including flask from my requirements.txt file.  
pip3 install -r requirements.txt

# Ran the flask application listening on port 4567
python3 -m flask run --host=0.0.0.0 --port=4567

```



