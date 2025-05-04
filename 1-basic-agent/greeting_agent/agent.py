from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    #model="gemini-2.0-flash",
    model=LiteLlm(
        # Specify the OpenRouter model using 'openrouter/' prefix
        model="openrouter/google/gemini-2.0-flash-001",
        # Explicitly provide the API key from environment variables
        api_key=os.getenv("OPENROUTER_API_KEY"),
        # Explicitly provide the OpenRouter API base URL
        api_base="https://openrouter.ai/api/v1"
    ),
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)
