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


With Docker installed in Gitpod, I created a new Docker file in the the backend-flask folder and used the following code to create my docker container. I created a diagram in lucid charts which is shown below, to break down what is happening here. 

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



