from crewai import Agent
from tools import tool
from dotenv import load_dotenv 

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os 

# Call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))


# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Identify the latest innovations and breakthroughs in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "As an expert researcher, you're passionate about discovering"
        "the newest technologies and trends. You thrive on uncovering"
        "insights that can drive progress and innovation."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

# Creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Create engaging and informative content about {topic}',
  verbose=True,
  memory=True,
  backstory=(
        "With a background in tech journalism, you have a knack for"
        "turning complex topics into compelling stories. Your mission"
        "is to inform and inspire readers with the latest tech news."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
