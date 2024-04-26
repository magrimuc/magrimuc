from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import sys

from traitlets import This

api_key = ""
model = "mistral-large-latest"

client = MistralClient(api_key=api_key)

import sys

def main():
    command_line_argument = sys.stdin.read().strip()
    desired_part = command_line_argument.split('|')[-1].strip()

    chat_response = client.chat(
    model=model,
    messages=[ChatMessage(role="user", content=command_line_argument)]
    )

    print(chat_response.choices[0].message.content)



if __name__ == "__main__":
    main()


