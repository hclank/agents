from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel, tool
from dotenv import load_dotenv

load_dotenv()

agent = CodeAgent(tools=[DuckDuckGoSearchTool()],model=InferenceClientModel())
agent.run("Search for the best music reccommendations for a party at the Wayne's mansion")

login()