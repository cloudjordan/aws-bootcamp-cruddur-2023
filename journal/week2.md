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

## Instrumenting My Application With Honeycomb

## Instrumenting My Application With AWS X-Ray

## Sending Application Logs to CloudWatch

## Implementing Rollbar

## Building Security for Tracing in AWS


