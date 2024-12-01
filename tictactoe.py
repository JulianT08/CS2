rowbot, colbot = botmove(board)
                board[rowbot][colbot] = "O"
                print("\n NOW THE BOT WILL MOVE: ")
                time.sleep(1)
                board_print(board)
                print()
                checkwin(board, "X")
                checkwin(board, "O")
