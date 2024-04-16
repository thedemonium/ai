import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

ollama_llm = Ollama(model="demonium:gpu", base_url="http://100.107.132.195:11434")

os.environ["OPENAI_API_KEY"] = ""

researcher = Agent(
  role='Знаток местности',
  goal='Придумывать новое. Генерировать идеи.',
  backstory="Вы знаток местности мирового класса.",
  verbose=True,
  allow_delegation=False,
  llm=ollama_llm,
)

writer = Agent(
  role='Писатель',
  goal='Создавать контент',
  backstory="Вы очень известный писатель, специализирующийся на написании контента.",
  verbose=True,
  allow_delegation=False,
  llm=ollama_llm
)

task1 = Task(
  description='Изучите все имеющиеся данные о городе Санкт-Петербурге.', 
  agent=researcher, 
  expected_output="Отчет на русском языке о самых интересных местах в городе Санкт-Петербург."
)

task2 = Task(
  description='На основе отчёта напишите сообщение в блоге.', 
  agent=writer, 
  expected_output="Черновой вариант записи в блоге. Используй для оформления разметку markdown. Без использования url-ссылок.",
  output_file='post_tver_places5.md'
)

crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  llm=ollama_llm,
  verbose=0, 
  process=Process.sequential 
)

# to work!!!
result = crew.kickoff()
