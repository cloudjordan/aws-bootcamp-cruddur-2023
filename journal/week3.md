# Week 3 — Decentralized Authentication

For week 3 I completed the following tasks:

| TABLE OF CONTENTS |
| :-------------- |
| [Configuring AWS Cognito](#configuring-aws-cognito) |
| [Configuring AWS Amplify](#configuring-aws-amplify) |
| [Using Access Token with JWT Server Side](#using-access-token-with-jwt-server-side) |


## Configuring AWS Cognito

To configure the web application with login and signup features, we used AWS Cognito user pools. Using a user pool ID, I created a user account. Here are some of the key configurations I made for the account:

- Used email address for username sign in option.
- Enabled self-service so the user can reset their own password if recovery is needed. 
- Disabled Cognito Hosted UI as we are using our web application's UI.
- Enabled pulbic app client to call unauthenticated API operations.


<p align="center">
<img src="assets/aws-cognito-user-pool-created.png" >
</p>
<br>


## Configuring AWS Amplify

To get started with Amplify, I first added the lirbabry to the list of dependencies in [package.json](../frontend-react-js/package.json) using `npm i aws-amplify --save`. 

Next, I configured the cognito pool in the [frontend app](../frontend-react-js/src/App.js ) by importing the Amplify package and adding the configuration code. The application is using environmental variables from my [docker-compose.yml](../docker-compose.yml) file to configure the behavior of the AWS Amplify library.

### ***Conditionally showing components based on authentication status...***

In [DesktopNavigation.js](../frontend-react-js/src/components/DesktopNavigation.js) and [DesktopSidebar.js](../frontend-react-js/src/components/DesktopSidebar.js), conditional statements are used to display components based on whether the user is logged in or not.
<br>
<br>
`DesktopNavigation.js` displays components like notifications, profile, and message links, while `DesktopSidebar.js` displays trending, suggested, and join links. These components are displayed on either side of the feed when the user is logged in to cruddur.<p>





## Using Access Token with JWT Server Side







