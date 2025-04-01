# 💸Stock Calculator Web App

A simple web application built with Flask that calculates stocks amount, stop loss, and deal cost for stock trading. It allows users to input the high and low values of a candle along with the desired risk amount. 

- **Stock Amount**: The number of stocks to buy based on the risk.
- **Total Deal Cost**: The total cost of the deal based on stock amount.

## Features

- User-friendly form to input candle high, low, and risk amount.
- Displays results dynamically after submitting the form:
  - Enter position At, Stop loss 
  - Stock amount to buy
  - Total deal cost $
- Saves results to MongoDB for future reference.
- Allows scrolling back and forward through previous results.

## Technologies Used

- **Flask**: Web framework for building the application.
- **MongoDB**: Stores calculation results for historical reference.
- **HTML**: For structuring and styling the frontend.
- **Python**: Backend logic for calculations.
- **Jenkins**: Automates the CI pipeline.  
- **Docker & Docker Compose**: Containerizes the application and manages dependencies.  
- **Jira**: Tracks issue.  
- **GitHub Webhook**: Triggers Jenkins builds upon code changes pushed to the GitHub repository.
- **Ngrok**: Exposes the local Jenkins server to the internet (for Github Webhook).  


## Pipeline Steps
1. **Environment** - Set the issue key as an environment variable.  
2. **Checkout the repository** - Clones the latest code from Git.  
3. **Build the Docker image** - Creates a Docker image from the applications source code.  
4. **Run unit tests** - Executes tests within the Docker container.  
5. **Cleanup** - Removes the Docker images and cleans the environment.
6. **Results**:
  - ✅If the pipeline succeeds, the Jira issue moves to **Done**.
  - ❌Else, a failure comment is added to the issue

  
## Pipeline
![Alt text](images/Jenkins_Pipeline.png)


## Required Jenkins Plugins  

Before running the pipeline, ensure you have the following Jenkins plugins installed:  
🔹 Git & GitHub Plugins, Jira Plugin, Docker Pipeline Plugin

You can install these plugins in **Jenkins > Manage Jenkins > Manage Plugins** under the **Available Plugins** tab.  
