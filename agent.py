from google.adk.agents import Agent
import random

from tools import (
    validate_move_tool,
    resolve_round_tool,
    update_game_state_tool
)

class RPSRefereeAgent(Agent):
    def __init__(self):
        super().__init__(
            name="rps_referee_agent",
            tools=[
                validate_move_tool,
                resolve_round_tool,
                update_game_state_tool
            ]
        )

    def choose_bot_move(self, bot_bomb_used: bool):
        moves = ["rock", "paper", "scissors"]
        if not bot_bomb_used:
            moves.append("bomb")
        return random.choice(moves)
