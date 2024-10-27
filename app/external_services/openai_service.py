import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_PERSONAL_KEY"),
)

# In-memory store for conversation history
conversation_history = []

def add_message(role, content):
    conversation_history.append({"role": role, "content": content})


async def get_chat_response(message: str) -> str:
    # Add user message to the conversation history
    add_message("user", message)

    chat_completion = await client.chat.completions.create(
        messages=conversation_history,
        model="gpt-4o-mini",
    )
    # Extract the assistant's response
    assistant_message = chat_completion.choices[0].message.content

    # Add assistant's response to the conversation history
    add_message("system", assistant_message)

    return assistant_message