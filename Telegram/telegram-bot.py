import os
from textwrap import dedent
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

ollama_llm = Ollama(model="demonium:cpu", base_url="http://100.107.6.134:11434")
os.environ["OPENAI_API_KEY"] = ""

async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf'Hello: {user.mention_html()}!',
        reply_markup=ForceReply(selective=True),
    )

async def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    user_message = update.message.text.replace("<|im_end|>", "")
    user_message = update.message.text.replace("<|im_start|>", "")
    file_name = 'dialog.txt'
    with open(file_name, mode='a') as f:
        f.write(f'User: {user_message}\n')

    print("The variable, name is of type:", type(user_message))
    


    bot = Agent(
        role=dedent("""Ты интерактивный помошник"""),
        goal=dedent("""
                       Ты можешь отвечать только на русском языке.
                    """),
        backstory=dedent("""
                       Ты много помогал в решении возникающих вопросов. 
                    """),
        verbose=True,
        allow_delegation=False,
        llm=ollama_llm,
    )

    task = Task(
        description=dedent("""Было получено сообщение от пользователя: """) + user_message,
        agent=bot,
        expected_output="Сообщение содержит только текст ответа от лица бота."
    )

    crew = Crew(
        agents=[bot],
        tasks=[task],
        llm=ollama_llm,
        verbose=0,
        process=Process.sequential
    )

    bot_response = crew.kickoff()
   
    with open(file_name, mode='a') as f:
        bot_response = bot_response.replace("<|im_end|>", "") 
        bot_response = bot_response.replace("<|im_start|>", "") 
        f.write(f'Bot: {bot_response }\n')


    await update.message.reply_text(bot_response.replace('<|im_end|>', ''))
    

def main() -> None:
    """Start the bot."""
    application = Application.builder().token('TOKEN').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()

if __name__ == '__main__':
    main()