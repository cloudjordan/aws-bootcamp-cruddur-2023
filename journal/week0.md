# Week 0 — Billing and Architecture

## Required Homework

### Conceptual Diagram

For the first part of the homework I completed the conceptual diagram based on what was learned in the week 0 video lecture. 

This diagram gives a conceptual overview of how an end user would be connected to the social media platform. 


LINK: https://lucid.app/lucidchart/846115f0-36b3-46ba-8b8c-b64a45c0d407/edit?viewport_loc=-537%2C-453%2C2988%2C1486%2C0_0&invitationId=inv_53e0172b-baf8-4629-9e1c-092ae10463ef
<img src="assets/conceptual-diagram.png" width="700" height="400">


### Architectural Diagram

Next I created the logical architectural diagram. Here I demonstrate how the end user would be connected to the social media platform through AWS. 


LINK: https://lucid.app/lucidchart/d2a2ef28-29fc-4f34-b9d4-1486ce61e5ec/edit?viewport_loc=-1463%2C-272%2C4118%2C2049%2C0_0&invitationId=inv_79a09a68-1011-47af-a2fa-a69b4ca19aeb
<img src="assets/architectural-diagram.png" width="700" height="625">

### Billing Alerts and Budgets
For billing alerts, I did it using both methods; through the management console AND through AWS CLI. 

#### CloudWatch Alarm
To setup billing alarm in the AWS management console I went to cloudwatch and made sure I was in N.virginia us-east-1.

In the side panel I went to Alarms > In alarm then clicked the Create alarm button. It then opend up a wizard to go through the steps of creating the alarm. Here are the steps I took:

1. Click Select metric then scroll down a bit and select Billing. 
2. Then select Total Estimated Charge
3. Select USD and click Select Metric
4. Give it a recognisable name.
5. Scroll down and select the money threshold you want the alert to trigger at then click Next. 
6. Alarm state trigger should be in Alarm. Create new SNS topic. Give it a name and assign the email endpoint then click Create topic. Scroll down and click Next. 
7. Give the alert a name then click Next. 
8. Confirm your settings, scroll down and click Create alarm. Alarm now created, 


I have included my username alias in the screenshot to prove it is my image. 
<img src="assets/cloudwatch-alarm.png" width="1000">

#### Budget

AWS Budgets allows me to get alerted when I reach or am near my budget threshold. 

Back in AWS Billing, go to budgets in the left panel and create new Budget. I then took the following.

1. Clicked Create budget
2. Choose your settings. I chose option for zero spend budget. This alerts me to any spend over $0.01
3. Make sure to add your email address and set budget low. When done, click Create budget. 
4. Budget now created. Can take up to 24 hours to populate all your spend data. 

I have included my username alias in the screenshot to prove it is my image. 
<img src="assets/budget.png" width="1000">






```

```

### IAM and Account Security

### Setting up and using AWS CLI in Gitpod

```

```

### AWS Organizations and Service Control Policies

```

```

