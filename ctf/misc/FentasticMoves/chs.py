import chess
import chess.engine
from stockfish import Stockfish

def get_best_move(fen_position):
    # 启动Stockfish引擎
    engine_path = './stockfish-ubuntu-x86-64-avx2'  # 替换为你的Stockfish引擎路径
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)

    # 加载给定的FEN位置
    board = chess.Board(fen_position)

    # 使用Stockfish计算最佳走法
    result = engine.play(board, chess.engine.Limit(time=2.0))  # 这里的时间限制可以根据需要进行调整

    # 关闭引擎
    engine.quit()

    return result.move

# 在这里输入你的FEN位置

position = '8/3n4/1N4N1/2Q5/4K3/8/4R3/3k1nR1'
#position = "4k3/q7/3Q3B/4K3/2Q5/1R3r2/5p2/4R3"
your_fen_position = position + " w - - 0 1"

best_move = get_best_move(your_fen_position)
print("Best move:", best_move)

engine_path = './stockfish-ubuntu-x86-64-avx2'
stockfish = Stockfish(engine_path)

stockfish.set_fen_position(your_fen_position)
best_move = stockfish.get_best_move()
print("Best move:", best_move)
