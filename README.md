# Rock Paper Scissors Referee Agent (RPS Plus)

## Overview
This project implements a minimal conversational AI referee for a Rock–Paper–Scissors–Plus game.  
The bot acts as a referee between the user and itself, enforcing rules, tracking state, and providing clear round-by-round feedback in a CLI-based conversational loop.

The game is best of 3 rounds and includes a special one-time “bomb” move.

---

## Game Rules
- Best of 3 rounds
- Valid moves: rock, paper, scissors, bomb
- Bomb can be used only once per player
- Bomb beats all other moves
- Bomb vs bomb results in a draw
- Invalid input wastes the round
- Game ends automatically after 3 rounds

---

## State Model
Game state is maintained explicitly in a Python dictionary, not in the prompt.  
The state includes:
- Current round number
- Maximum rounds (3)
- User score
- Bot score
- User bomb usage flag
- Bot bomb usage flag

This ensures state persistence across turns and clean separation between logic and interaction.

---

## Agent and Tool Design
The solution uses Google ADK primitives:
- A single ADK Agent (`RPSRefereeAgent`) orchestrates the game flow.
- Core game logic is encapsulated as explicit ADK `FunctionTool` definitions:
  - `validate_move` – validates user input and bomb usage
  - `resolve_round` – determines the winner of a round
  - `update_game_state` – mutates the game state after each round

These tools encapsulate all rule enforcement and state mutation, while the main conversational loop focuses on intent handling and response generation.

Due to limitations in the available ADK runtime interface, the underlying Python functions are invoked directly during execution, while remaining registered as ADK tools to clearly demonstrate tool-based design and separation of concerns.

---

## Architecture Separation
- **Intent Understanding**: User input parsing in `main.py`
- **Game Logic**: Encapsulated in tool functions (`tools.py`)
- **State Management**: Centralized game state object
- **Response Generation**: CLI-based conversational output

This structure keeps responsibilities clearly separated and easy to reason about.

---

## Tradeoffs
- Bot move selection is random for simplicity.
- The interface is CLI-based rather than graphical, as UI frameworks are explicitly disallowed.
- A single-agent design was chosen to keep the solution minimal and focused.

---

## Future Improvements
With more time, the following enhancements could be added:
- Smarter bot strategy instead of random selection
- Structured ADK schemas for richer tool outputs
- Natural language input handling
- Optional UI or API wrapper (if allowed)
