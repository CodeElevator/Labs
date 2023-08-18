import chess

class Engine:
    def __init__(self, board, max_depth, color):
        self.board = board
        self.max_depth = max_depth
        self.color = color
    
    def eval_funct(self):
        pass

    def mate_opportuity(self):
        if self.board.legal_moves.count() == 0:
            if self.board.turn == self.color:
                return -999
            else:
                return 999
    
    def engine(self, candidate, depth):
        if depth == self.max_depth or self.board.legal_moves.count() == 0:
            return self.eval_funct()
        else:
            move_list = list(self.board.legal_moves)
            new_candidate = 0
            if depth % 2 != 0:
                new_candidate = float("-inf")
            else:
                new_candidate = float("inf")
        
            for i in move_list:
                self.board.push(i)
                value = self.engine(new_candidate, depth+1)

                # Basic minimax algorith
                if value > new_candidate and depth % 2 !=0: # type: ignore
                    new_candidate = value
                    if depth == 1:
                        move = i

                elif value < new_candidate and depth % 2 ==0: # type: ignore
                    new_candidate=value

                # Alpha beta pruning cuts
                if candidate is not None and value < candidate and depth % 2 == 0:
                    self.board.pop
                    break

                elif candidate is not None and value > candidate and depth % 2 != 0:
                    self.board.pop
                    break
        
            if depth > 1:
                return new_candidate
            else:
                return move