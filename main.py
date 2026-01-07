from agent import RPSRefereeAgent
from tools import validate_move, resolve_round, update_game_state

agent = RPSRefereeAgent()

state = {
    "round": 1,
    "max_rounds": 3,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False
}

print("Rock Paper Scissors Referee")
print("Best of 3. Bomb usable once. Invalid input wastes round.\n")

while state["round"] <= state["max_rounds"]:
    print(f"Round {state['round']}")
    user_move = input("Your move: ").strip().lower()

    # ✅ Validate move
    validation = validate_move(
        move=user_move,
        bomb_used=state["user_bomb_used"]
    )

    bot_move = agent.choose_bot_move(state["bot_bomb_used"])

    if not validation["valid"]:
        print("Invalid input. Round wasted.\n")
        state["round"] += 1
        continue

    # ✅ Resolve round
    winner = resolve_round(
        user_move=user_move,
        bot_move=bot_move
    )

    # ✅ Update state
    state = update_game_state(
        state=state,
        winner=winner,
        user_move=user_move,
        bot_move=bot_move
    )

    print(f"You played {user_move}, Bot played {bot_move}")
    print(f"Round winner: {winner.upper()}\n")

print("Game Over")
print(f"Final Score → You: {state['user_score']} Bot: {state['bot_score']}")

if state["user_score"] > state["bot_score"]:
    print("YOU WIN!")
elif state["user_score"] < state["bot_score"]:
    print("BOT WINS!")
else:
    print("DRAW!")
