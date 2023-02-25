from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI, LLMMathChain, SerpAPIWrapper
from langchain.agents import initialize_agent


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

import os
os.environ['OPENAI_API_KEY'] = 'your_openai_api_key'
telegram_token = 'your_telegram_token'
os.environ['SERPAPI_API_KEY'] = 'your_serp_api_key'

llm=OpenAI(temperature=0)

# Load the tool configs that are needed.
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain(llm=llm, verbose=True)
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    )
]

# dictionary for story memory for each user.
# key is user_id, value is the ConversationBufferMemory object
user_memory = {}

#function to get retrieve the memory for the user or create a new one if it doesn't exist
def get_user_memory(user_id):
    if user_id in user_memory:
        return user_memory[user_id]
    else:
        user_memory[user_id] = ConversationBufferMemory(memory_key="chat_history")
        return user_memory[user_id]


async def message(update: Update, context):
    memory = get_user_memory(update.message.from_user.id)
    agent_chain = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True, memory=memory)
    response = agent_chain.run(input=update.message.text)

    await update.message.reply_text(response)


app = ApplicationBuilder().token(telegram_token).connect_timeout(60).build()

app.add_handler(MessageHandler(None, message))
print("Starting bot...")
app.run_polling(print("Bot started!"))
