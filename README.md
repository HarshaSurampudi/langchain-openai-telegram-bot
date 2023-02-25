# langchain-openai-telegram-bot
A simple implementation of an itelligent telegram chatbot using langchain agents, OpenAI LLM.

The agent has access to two tools:
1. Search (SerpAPI)
2. Calculator (llm-math)
Which can be used when necessary.

## Instructions:
Install the required libraries
```
pip install -r requirements.txt
```
Run the bot
```
python bot.py
```

### Note:
You would need OPENAI_API_KEY, telegram_token, SERPAPI_API_KEY to run the bot.

Custom Agent:
You can use a custom agent by providing `agent_path` parameter in the `initialize_agent` function.

```
agent_chain = initialize_agent(tools, llm, agent_path="custom_agent.json", verbose=True, memory=memory)
```
Modify the prefix in `custom_agent.json` to suit you need.

:)
