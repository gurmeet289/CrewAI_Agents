# CrewAI-Agents Using Google-Gemini:

# Python Project with CrewAI

Welcome to the Python project using CrewAI! This guide will help you set up your environment, configure your API keys, and get your project up and running.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10
- pip (Python package installer)

## Setting Up Your Environment

1. **Clone the Repository**

       git clone https://github.com/gurmeet289/CrewAI_Agents.git

       **cd CrewAI_Agents**
   
3. **Create a Conda Environment**

      conda create -p venv python==3.10 -y
  
3. **Activate the Conda Environment**

     conda activate myenv
   
5. **Install Dependencies**

      If you don’t have a requirements.txt, you can install the dependencies directly using pip after activating the Conda environment:

         **pip install -r requirements.txt**

## Configuration

To configure the project, you'll need to create a .env file to store your API keys and other environment variables.

1. **Create a .env File**

    In the root directory of your project, create a file named .env.

2. **Add API Keys and Other Environment Variables**

       **GOOGLE_API_KEY=your-google-api-key**
       **SERPER_API_KEY=your-serper-api-key**

## Running the Project

    To run the project, use the following command:
       ** python main.py**

  **Note - Make sure your environment variables are set correctly and your Conda environment is activated.**
  
## Additional Information

  **Requirements**: Make sure all required packages are listed in requirements.txt. You can generate this file using:
  
         ** pip freeze > requirements.txt**

###############################################################################################################################################
