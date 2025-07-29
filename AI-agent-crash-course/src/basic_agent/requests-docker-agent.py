import requests

def send_message_to_agent(user_input: str):
    url = "http://localhost:8081/agent/greeting_agent/message"
    headers = {"Content-Type": "application/json"}
    payload = {"input": user_input}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        print("Agent replied:", data.get("output", "No output field"))
    except requests.RequestException as e:
        print("Error talking to the agent:", e)

if __name__ == "__main__":
    send_message_to_agent("Hello! What’s your name?")
