# Bot.py: Main script to run the Telegram bot. 
# Initializes and configures the bot, including setting up state management for handling user interactions.

import os
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from connection import dp
from handlers import ai, buttons, other, responses

# Define states for managing user interactions in a conversational flow.
class Form(StatesGroup):
    waiting_for_answer = State()
    gpt = State()

# Function to perform initial setup when the bot starts.
async def on_startup(_):
    # Validate environment variables and display a running message.
    if not os.getenv('OPEN_AI_TOKEN'):
        raise ValueError('OPEN_AI_TOKEN is not provided')
    print('Bot is running!')

# Registering various handlers for the bot's commands and responses.
buttons.register_handlers_buttons(dp)
ai.register_handlers_ai(dp)
responses.register_handlers_responses(dp)

# Entry point to start the bot with polling.
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
