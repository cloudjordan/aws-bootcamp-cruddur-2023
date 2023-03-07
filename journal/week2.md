# Week 2 — Distributed Tracing

For week 2 I completed the following tasks:

| TABLE OF CONTENTS |
| :-------------- |
| [What is Distributed Tracing?](#what-is-distributed-tracing) |
| [Setting Up My Environment in Honeycomb](#setting-up-my-environment-in-honeycomb) |
| [Setting Up Honeycomb Environment Variables in Gitpod](#setting-up-honeycomb-environment-variables-in-gitpod) |
| [Instrumenting My Application With Honeycomb](#instrumenting-my-application-with-honeycomb) |
| [Instrumenting My Application With AWS X-Ray](#instrumenting-my-application-with-aws-x-ray) |
| [Sending Application Logs to CloudWatch](#sending-application-logs-to-cloudwatch) |
| [Implementing Rollbar](#implementing-rollbar) |
| [Building Security for Tracing in AWS](#building-security-for-tracing-in-aws) |

<br>

## What is Distributed Tracing?

<p>From my learning experience, observability is crucial for understanding complex distributed systems. The three pillars of observability, which are metrics, traces, and logs, provide a comprehensive approach to identifying and diagnosing issues.<p> 
  
<p>Logs alone are not sufficient for tracking events in large-scale distributed systems, and distributed tracing is needed to pinpoint the flow of data. Metrics allow me to see patterns over time, while logging provides timestamped events. Using these observability techniques, I can gain valuable insights into complex distributed systems and identify issues that may not be apparent through other means.<p>

<br>

## Setting Up My Environment in Honeycomb
  
I have learned that segmenting observability environments is crucial for issue identification and diagnosis. Separating development and production allows clearer insights for optimization, although we're currently using just one for this bootcamp.
  
After creating an environment in my Honeycomb account, I copied it's API key to the clipboard to assign to an environment variable in my Gitpod workspace. 

<p align="center">
<img src="assets/environment-created.png" >
</p>
<br>

## Setting Up Honeycomb Environment Variables in Gitpod

I saved my Honeycomb API key to a my `HONEYCOMB_API_KEY` environment variable and exported it. I also set the OTEL service name for the OTEL service name environment variable `OTEL_SERVICE_NAME`. This will determine the name Honeycomb uses for my application. I set this in my [docker-compose.yml](../docker-compose.yml) file.
<br>

I also set the required open telemetry environment variables for reaching the Honeycomb API endpoint and authenticating the sending of telemetry data from my application. These were also added to [docker-compose.yml](../docker-compose.yml).
<br>
<br>

## Instrumenting My Application With Honeycomb

To setup instrumentation in my application with Python and Flask, I installed the required dependencies using my [requirements.txt](../backend-flask/requirements.txt) file.
<br>
<br>
The next step was to add instrumentation and create and initialize a tracer in my [main](../backend-flask/app.py) flask file. This enabled data to be sent to Honeycomb. To do this I carried out the following steps:

1. Added the imports from Honeycomb to my [app.py](../backend-flask/app.py) file.
2. Added the code required to initialize tracing and an exporter that can send data to Honeycomb.
3. Added the code required to initialize automatic instrumentation with Flask.

### ***Confirming the frontend and backend are reachable...***

With dependencies installed for the frontend and backend, I launched my [docker-compose](../docker-compose.yml) environment and opened up the ports to confirm the the frontend and backend were reachable so that Honeycomb could receive the telemtry data. 

### ***Collecting Data in Honeycomb...***

The dataset was automatically created when it arrived with the service name set in docker-compose. 

<p align="center">
<img src="assets/honeycomb-dataset.png" >
</p>
<br>

After opening the dataset, I alos saw that I was succesful in receiving traces. Following this, I also hardcoded a traced span to mock what a realy one may look like. I did this in my [home_activities](../backend-flask/services/home_activities.py) file. I also experimented with Honeycomb queries, as an alternative way to view data. 

<p align="center">
<img src="assets/honeycomb-mockdata-span.png" >
</p>
<br>

## Instrumenting My Application With AWS X-Ray

X-Ray is an observability tool like Honeycomb. It uses a separate container, the X-Ray Daemon, to collect trace data from my application and send it to the X-Ray API for visualization. This ensures that the data collection does not impact the performance of my application
<br>
  
After installing the [dependencies](../backend-flask/requirements.txt), I instrumented the Flask [app](../backend-flask/app.py) by configuring and enabling the X-Ray middleware to allow it to trace data from my app. 
<br>

### ***Adding X-Ray Sampling Rules Resources...***

To control the rate at which trace data is captured from the Flask app, in JSON I defined a [sampling rule](../aws/json/xray.json) which specifies conditions that must be met for a request to be sampled, allowing me to control the volume of trace data generated by the app. 


## Sending Application Logs to CloudWatch

## Implementing Rollbar

## Building Security for Tracing in AWS


