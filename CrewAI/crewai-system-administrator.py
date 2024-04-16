import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

ollama_llm = Ollama(model="dolphin-mistral:7b-v2.8", base_url="http://100.107.132.195:11434")
os.environ["OPENAI_API_KEY"] = ""

linux_sysadmin = Agent(
  role='Linux System Administrator',
  goal='Install, configure, and maintain an organizations local area network (LAN), wide area network (WAN), data communications network, operating systems, and physical and virtual servers.',
  backstory='He has solved countless issues for the company, earning him a reputation as a trusted advisor in the IT department',
  verbose=True,
  allow_delegation=False,
  llm=ollama_llm,
)

task1 = Task(
  description='Suggest optimal KVM virtual machine settings. The virtual machine will use the OS: Windows and 1C. 1C application and MSSQL backend for 1C databases', 
  agent=linux_sysadmin, 
  expected_output='KVM virtual machine settings'
)

task2 = Task(
  description='Optimize your KVM virtual machine settings to get the fastest and most responsive disk configuration. For the needs of storing MSSQL databases passthrough two physical nvme disks to a virtual machine.', 
  agent=linux_sysadmin, 
  expected_output='KVM virtual machine settings. Using markdown for design',
  output_file='1c_kvm_settings.md'
)

crew = Crew(
  agents=[linux_sysadmin],
  tasks=[task1, task2],
  llm=ollama_llm,
  verbose=0, 
  process=Process.sequential 
)

# to work!!!
result = crew.kickoff()
