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



### IAM User Account
To create an IAM user I took the following steps. 

1. Opened AWS IAM. And clicked Add users. 
2. Chose the settings. i.e. for password and username and console access then clicked Next.
3. Created a group to add the user to. This helps allows users permissions to access and use different services etc. I will add admin access. 
4. Give it a name and assign it the relevant permission.
5. Click Create user group. Once created check the box to make sure IAM account will be added to the group.
6. Will take you to the summary page to confirm the settings you entered then can click Create. 
7. Showed me the summary page with my credentials. 
8. Account now created. 

Account shows my username to prove this is my image. 
<img src="assets/IAM-user.png" width="1000">



### IAM User Access Keys
To create access keys for my IAM user I took the following steps. 

1. In IAM under Users, selecting the user, then security credentials tab you can create various secrutiy credentials for the user, such as Access Keys, password and MFA.
2. Clicked on Access Keys and selected the option for where the access keys are intended to be used. As will be using them for the CLI, selected that option. 
3. On the next screen can give an optional description for access key then click **Create key**. 
4. Then showed me a page with my access key and secret key. 



### Setting up and using AWS CLI in Gitpod
To install and use AWS CLI in Gitpod, I took the following steps. 

1. Ran the following commands as shown in the aws documentation:
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
2. After installing, confirmed it was installed by running the following: aws --version which showed me the version of aws cli installed. 
```
gitpod /workspace $ aws --version
aws-cli/2.9.23 Python/3.9.11 Linux/5.15.0-47-generic exe/x86_64.ubuntu.20 prompt/off
```
3. To setup environment variables for the AWS user account, used environment variables as demonstrated in the [user guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html). Copied these lines into a plain text file in GitPod:
```
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION=""
```
4. To configure the credentials, I added the access key credentials (I generated earlier for the IAM account) to the environment variables I just created. Including adding a default region. Then copied each line into the terminal. 
```
export AWS_ACCESS_KEY_ID="KEY WENT HERE"
export AWS_SECRET_ACCESS_KEY="KEY WENT HERE"
export AWS_DEFAULT_REGION="REGION WENT HERE"
```

5. Ran the command aws sts get-caller-identity. Which outputted:
```
{
    "UserId": "USER ID SHOWED HERE",
    "Account": "ACCOUNT ID SHOWED HERE",
    "Arn": "AMAZON RESOURCE NAME SHOWED HERE"
}
```

6. To make sure everything I have been doing in GitPod will be saved if closing the window and opening again. Inside the .gitpod.yml template, I added the following task. 
```
tasks:
  - name: aws-cli
    env:
			# environment variable to auto-complete aws cli typing commands on partial mode.
      AWS_CLI_AUTO_PROMPT: on-partial
		# installing the aws cli in our chosen directory
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```

7. Next ran the following command in the terminal gp env  followed by each credential. This saves the credentials in a secure place in gitpod so our credentials will be available for use every time we launch GitPod.  
```
gp env AWS_ACCESS_KEY_ID="KEY WENT HERE"
gp env AWS_SECRET_ACCESS_KEY="KEY WENT HERE"
gp env AWS_DEFAULT_REGION="REGION WENT HERE"
```

8. In gitpod user settings, I could then see the environment variables I just made.

<img src="assets/environment-variables.png" width="450">

9. To commit the changes I just made, while in the workspace directory, I went to the source control panel on the left hand side of window. Entered a message for the change we made, then clicked commit. 

10. A prompt window opened, clicked yes to stage changes. And clicked synch after the commit button changed.
 
11. To confirm the changes have beed committed, went back to my github repo, opened the gitpod.yml file to check. Changes now are commited. 

12. Now everytime I closed down the Gitpod environment and reopened it, AWS CLI will automatically install. 



### Setting Up AWS Billing Alarm and Budget
By default AWS is not giving my IAM account access to billing and budgeting. So in root account had to activate it.

As I had already setup budgeting in the console, I deleted the 2 budgets I had made to not be charged when recreating my budgets in AWS CLI to prevent going over the free tier limit. 

1. In GitPod created in a new folder in the side panel called “aws”. Within that folder created another folder called “json”. 

2. Inside the json folder created 2 files: budget.json and budget-notifications-with-subscribers.json

3. inside budget.json I added the following code from the aws cli reference user guide:
```
{
    "BudgetLimit": {
        "Amount": "10",
        "Unit": "USD"
    },
    "BudgetName": "Example Tag Budget",
    "BudgetType": "COST",
    "CostFilters": {
				# Filters for costs based on usage attributes (e.g. tags)
        "TagKeyValue": [
            "user:Key$value1",
            "user:Key$value2"
        ]
    },
		# Types of costs to include in the budget
    "CostTypes": {
        "IncludeCredit": true,
        "IncludeDiscount": true,
        "IncludeOtherSubscription": true,
        "IncludeRecurring": true,
        "IncludeRefund": true,
        "IncludeSubscription": true,
        "IncludeSupport": true,
        "IncludeTax": true,
        "IncludeUpfront": true,
        "UseBlended": false
    },
		# The time period for the budget
    "TimePeriod": {
        "Start": 1477958399, 
        "End": 3706473600
    },
    "TimeUnit": "MONTHLY"
}```

```

4. inside budget-notifications-with-subscribers.json I added the following code from the user guide:
```
[
    {
        "Notification": {
            "ComparisonOperator": "GREATER_THAN",
            "NotificationType": "ACTUAL", # The type of notification (e.g. actual, forecasted)
            "Threshold": 80, # Threshold value for the notification to send
            "ThresholdType": "PERCENTAGE" # Type e.g. percentage, absolute value etc.
        },
				# The list of subscribers for the notification
        "Subscribers": [
            {
                "Address": "example@example.com",
                "SubscriptionType": "EMAIL"
            }
        ]
    }
]
```

5. I stored my account ID in an environment variable using the following command:
```
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
```
6. To save the environment variable I used the following command:
```
gp env AWS_ACCOUNT_ID="ACCOUNT ID WENT HERE"
```

7. It now is saved in the GitPod environment variables.

8. I then copied and pasted the following command (which included the Account ID environment variable) into the command line:
```
aws budgets create-budget \
    --account-id $AWS_ACCOUNT_ID \
    --budget file://aws/json/budget.json \
    --notifications-with-subscribers file://aws/json/budget-notifications-with-subscribers.json
```

9. Back in the aws console, the budget has now been created.

I have included my username alias in the screenshot to prove it is my image. 
<img src="assets/budget.png" width="1000">


#### Creating a Billing Alarm in AWS CLI

1. First I need to setup SNS topic before I create an alarm. To do so used the following command:
```
aws sns create-topic --name billing-alarm
```

Topic created:
```
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ aws sns create-topic --name billing-alarm
{
    "TopicArn": "arn:aws:sns:ca-central-1:123456789010:billing-alarm"
}
```

2. next I input this command:
```
aws sns subscribe \
    --topic-arn="arn:aws:sns:ca-central-1:ACCCOUNT_ID_GOES_HERE:billing-alarm" \
    --protocol=email \
    --notification-endpoint=your@email.com
```

Output was:
```
{
    "SubscriptionArn": "pending confirmation"
}
```

3. Received a confirmation email in my mailbox. Once clicked to confirm, a new window opened confirming my subscription. 

4. In AWS console, SNS topic created in the region that was configured (ca-central-1):

<img src="assets/SNS-topic.png" width="1000">


5. Created a new json file in GitPod named alarm-config.json. Pasted the following code snippet into it: 
```
{
  "AlarmName": "DailyEstimatedCharges",
  "AlarmDescription": "This alarm would be triggered if the daily estimated charges exceeds 1$",
  "ActionsEnabled": true,
  "AlarmActions": [
      "arn:aws:sns:<REGION>:<ACCOUNT_ID>:<SNS_TOPIC_NAME>"
  ],
  "EvaluationPeriods": 1,
  "DatapointsToAlarm": 1,
  "Threshold": 1,
  "ComparisonOperator": "GreaterThanOrEqualToThreshold",
  "TreatMissingData": "breaching",
  "Metrics": [{
      "Id": "m1",
      "MetricStat": {
          "Metric": {
              "Namespace": "AWS/Billing",
              "MetricName": "EstimatedCharges",
              "Dimensions": [{
                  "Name": "Currency",
                  "Value": "USD"
              }]
          },
          "Period": 86400,
          "Stat": "Maximum"
      },
      "ReturnData": false
  },
  {
      "Id": "e1",
      "Expression": "IF(RATE(m1)>0,RATE(m1)*86400,0)",
      "Label": "DailyEstimatedCharges",
      "ReturnData": true
  }]
}
```

6. Under the “AlarmActions” section, pasted the topic arn I generated earlier when I used the create-topic command:
```
"AlarmActions": [
      "arn:aws:sns:ca-central-1:ACCOUNT_ID_GOES_HERE:billing-alarm"
  ],
```

7. Ran the following command in the terminal:
```
aws cloudwatch put-metric-alarm --cli-input-json file://aws/json/alarm-config.json
```

8. Alarm created and can see it in the aws cloudwatch console.

<img src="assets/cloudwatch-alarm.png" width="1000">

