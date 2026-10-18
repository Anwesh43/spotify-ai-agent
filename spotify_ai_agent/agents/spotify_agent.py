from tools.spotify_tools import getAvailableTools
from prompts.spotify_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv 
from pydantic_ai import Agent 

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    system_prompt = SYSTEM_PROMPT,
    tools = getAvailableTools()
)

async def recommendUserSpotifyData(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')