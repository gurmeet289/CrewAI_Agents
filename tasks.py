from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  description=(
        "Investigate the most recent advancements in {topic}. Highlight"
        "the key innovations and their implications. Your report should"
        "outline the benefits, challenges, and future prospects of these advancements."
  ),
  expected_output='A detailed analysis report summarizing the latest AI trends in 3 paragraphs.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
        "Write an informative and engaging article about {topic}. Focus on"
        "the impact of current trends on the industry and the potential"
        "future developments. The article should be accessible to a wide audience."
  ),
  expected_output='A 7-paragraph article detailing {topic} advancements, formatted in markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-tech-article.md'  # Example of output customization
)