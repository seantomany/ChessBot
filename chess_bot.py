import chess
import random
from typing import Optional

class ChessBot:
    def __init__(self, color: chess.Color = chess.WHITE):
        self.board = chess.Board()
        self.color = color
        
    def make_move(self) -> Optional[chess.Move]:
        """
        Make a move on the chess board.
        Returns the move made, or None if no legal moves are available.
        """
        legal_moves = list(self.board.legal_moves)
        if not legal_moves:
            return None
            
        # Simple random move strategy for now
        # We'll improve this with better AI later
        move = random.choice(legal_moves)
        self.board.push(move)
        return move
    
    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.board.is_game_over()
    
    def get_board(self) -> chess.Board:
        """Get the current board state."""
        return self.board

def main():
    # Create a bot playing as white
    bot = ChessBot(chess.WHITE)
    
    print("Welcome to Chess Bot!")
    print("Enter moves in UCI format (e.g., 'e2e4')")
    print("Type 'resign' to give up the game")
    
    while not bot.is_game_over():
        if bot.board.turn == chess.WHITE:
            # Bot's turn
            move = bot.make_move()
            if move:
                print(f"Bot played: {move}")
            else:
                print("No legal moves available for bot")
                break
        else:
            # Human's turn
            move_str = input("Enter your move: ").lower().strip()
            
            # Check for resignation
            if move_str == "resign":
                print("\nYou resigned the game!")
                print("Bot wins!")
                break
                
            try:
                move = chess.Move.from_uci(move_str)
                if move in bot.board.legal_moves:
                    bot.board.push(move)
                else:
                    print("Illegal move! Try again.")
                    continue
            except ValueError:
                print("Invalid move format! Please use UCI format (e.g., 'e2e4') or type 'resign' to give up")
                continue
        
        # Print the current board
        print("\nCurrent board position:")
        print(bot.board)
    
    # Print final board state
    print("\nFinal board position:")
    print(bot.board)

if __name__ == "__main__":
    main() 