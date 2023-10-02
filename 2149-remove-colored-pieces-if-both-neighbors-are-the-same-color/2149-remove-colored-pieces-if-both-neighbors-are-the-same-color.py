class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_moves = 0
        bob_moves = 0
        for i in range(len(colors)-2):
            if colors[i] == 'A' and colors[i+1] == 'A' and colors[i+2] == 'A':
                alice_moves += 1
            if colors[i] == 'B' and colors[i+1] == 'B' and colors[i+2] == 'B':
                bob_moves += 1
        return alice_moves > bob_moves