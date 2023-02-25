# langchain-openai-telegram-bot
A simple implementation of an intelligent telegram chatbot using langchain agents, OpenAI LLM.

The agent has access to two tools:
1. Search (SerpAPI)
2. Calculator (llm-math)
Which can be used when necessary.

## Instructions:
Create a virtual environment (highly suggested)
```
python -m venv ven
```
Activate the enviroment
- Linux
```
source venv/bin/activate
```
- Windows
```
.\venv\Scripts\activate
```
Install the required libraries
```
pip install -r requirements.txt
```
Run the bot
```
python bot.py
```

**Note:** You would need `OPENAI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `SERPAPI_API_KEY` to run the bot. Consider storing them in `.env` file instead of putting them in the code like I did. 

### Custom Agent:
You can use a custom agent by providing `agent_path` parameter in the `initialize_agent` function.

**Note:** You can provide either agent or agent_path (not both)

```
agent_chain = initialize_agent(tools, llm, agent_path="custom_agent.json", verbose=True, memory=memory)
```
Modify the prefix in `custom_agent.json` to suit you need.

The prefix that I provided in `custom_agent.json` is for a bot that solves queries related to taxes in UK

## Links
- [OpenAI API](https://openai.com/api/)
- [SerpAPI](https://serpapi.com/)
- [LangChain Documentation](https://langchain.readthedocs.io/en/latest/)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)



:smiley:
