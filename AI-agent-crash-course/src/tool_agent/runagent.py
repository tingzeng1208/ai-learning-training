#!/usr/bin/env python3
"""
Script to run the tool_agent interactively.
This script loads the tool_agent and allows you to interact with it via command line.
"""

import os
import sys
import asyncio
import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Add the current directory to the Python path so we can import tool_agent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv()

# Import the agent after setting up the path
from tool_agent.agent import root_agent


async def run_agent_interactive():
    """Run the tool agent in interactive mode."""
    print("🤖 Tool Agent Interactive Session")
    print("=" * 50)
    print("This agent can use Google Search to help answer your questions.")
    print("Type 'quit', 'exit', or 'bye' to stop the session.")
    print("=" * 50)
    
    # Setup session service and runner
    session_service = InMemorySessionService()
    APP_NAME = "Tool Agent"
    USER_ID = "user"
    SESSION_ID = str(uuid.uuid4())
    
    # Create session
    new_session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state={}
    )
    
    # Create runner
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
    
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print("👋 Goodbye!")
                break
            
            # Skip empty input
            if not user_input:
                continue
                
            # Process the input with the agent
            print("\n🤖 Agent: ", end="", flush=True)
            
            # Create content for the agent
            content = types.Content(role="user", parts=[types.Part(text=user_input)])
            
            # Run the agent and collect response
            response_text = ""
            async for event in runner.run_async(
                user_id=USER_ID,
                session_id=SESSION_ID,
                new_message=content
            ):
                if event.is_final_response():
                    if event.content and event.content.parts:
                        response_text = event.content.parts[0].text
                        break
            
            # Print the response
            print(response_text)
            
        except KeyboardInterrupt:
            print("\n\n👋 Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'quit' to exit.")


async def run_agent_single_query(query: str):
    """Run the agent with a single query."""
    print(f"🤖 Processing query: {query}")
    print("=" * 50)
    
    # Setup session service and runner
    session_service = InMemorySessionService()
    APP_NAME = "Tool Agent"
    USER_ID = "user"
    SESSION_ID = str(uuid.uuid4())
    
    # Create session
    new_session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state={}
    )
    
    # Create runner
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
    
    try:
        # Create content for the agent
        content = types.Content(role="user", parts=[types.Part(text=query)])
        
        # Run the agent and collect response
        response_text = ""
        async for event in runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=content
        ):
            if event.is_final_response():
                if event.content and event.content.parts:
                    response_text = event.content.parts[0].text
                    break
        
        print("🤖 Agent Response:")
        print(response_text)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


async def main_async():
    """Main async function to handle command line arguments."""
    
    # Check if Google API key is set
    if not os.getenv('GOOGLE_API_KEY'):
        print("❌ Error: GOOGLE_API_KEY environment variable not set!")
        print("Please set your Google API key in the .env file or as an environment variable.")
        return 1
    
    # Check command line arguments
    if len(sys.argv) > 1:
        # If arguments provided, treat them as a single query
        query = ' '.join(sys.argv[1:])
        return await run_agent_single_query(query)
    else:
        # No arguments, run in interactive mode
        await run_agent_interactive()
        return 0


def main():
    """Main function to handle command line arguments."""
    return asyncio.run(main_async())


if __name__ == "__main__":
    sys.exit(main())
