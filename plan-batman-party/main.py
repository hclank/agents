from huggingface_hub import login
from smolagents import CodeAgent, InferenceClientModel, tool
from dotenv import load_dotenv

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


agent = CodeAgent(tools=[suggest_menu], model=InferenceClientModel())
agent.run("Prepare a formal menu for the dinner party.")

login()
