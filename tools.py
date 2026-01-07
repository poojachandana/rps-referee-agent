from google.adk.tools import FunctionTool

# ---------- Game Logic Functions ----------

def validate_move(move: str, bomb_used: bool) -> dict:
    valid_moves = ["rock", "paper", "scissors", "bomb"]

    if move not in valid_moves:
        return {"valid": False, "reason": "Invalid move"}

    if move == "bomb" and bomb_used:
        return {"valid": False, "reason": "Bomb already used"}

    return {"valid": True}


def resolve_round(user_move: str, bot_move: str) -> str:
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"
    if bot_move == "bomb":
        return "bot"

    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    return "user" if rules[user_move] == bot_move else "bot"


def update_game_state(state: dict, winner: str, user_move: str, bot_move: str) -> dict:
    state["round"] += 1

    if winner == "user":
        state["user_score"] += 1
    elif winner == "bot":
        state["bot_score"] += 1

    if user_move == "bomb":
        state["user_bomb_used"] = True
    if bot_move == "bomb":
        state["bot_bomb_used"] = True

    return state


# ---------- ADK Tool Declarations (REQUIRED) ----------

validate_move_tool = FunctionTool(validate_move)
resolve_round_tool = FunctionTool(resolve_round)
update_game_state_tool = FunctionTool(update_game_state)
