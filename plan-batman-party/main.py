from huggingface_hub import login
from smolagents import CodeAgent, InferenceClientModel, tool, DuckDuckGoSearchTool
from dotenv import load_dotenv
import datetime

load_dotenv()


@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and soft drinks."
    elif occasion == "formal":
        return "Steak, salad, and wine."
    elif occasion == "superhero":
        return "Buffet with high energy and healthy food options."
    else:
        return "custom menu for the butler"


agent = CodeAgent(
    tools=[suggest_menu, DuckDuckGoSearchTool()],
    model=InferenceClientModel(),
    additional_authorized_imports=["datetime"],
)
agent.run("Search for the best music reccommendations for a party at the Wayne's Manor")
agent.run("Prepare a formal menu for the dinner party.")
agent.run("""
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """)


login()
agent.push_to_hub(repo_id="hclanka/alfred-party-planner", private=True)
