from google.adk import Agent, run_agent
from google.adk.state import AgentState
from dotenv import load_dotenv

load_dotenv()

class MyAgent(Agent):
    def run(self, state: AgentState):
        user_input = state["user_input"]
        return {"response": f"Gemini response to: {user_input}"}

if __name__ == "__main__":
    run_agent(MyAgent)
