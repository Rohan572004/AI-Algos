import java.util.Scanner;

public class TicTacToeAI {
    static char player, ai;
    static char[][] board = { { ' ', ' ', ' ' }, { ' ', ' ', ' ' }, { ' ', ' ', ' ' } };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Player chooses their symbol
        System.out.print("Choose your symbol (X or O): ");
        player = Character.toUpperCase(scanner.next().charAt(0));
        while (player != 'X' && player != 'O') {
            System.out.print("Invalid choice. Choose X or O: ");
            player = Character.toUpperCase(scanner.next().charAt(0));
        }
        ai = (player == 'X') ? 'O' : 'X';

        System.out.println("You are " + player + ". AI is " + ai + ".");
        printBoard();

        // Main game loop
        while (true) {
            playerMove(scanner);
            if (isGameOver(player)) {
                System.out.println("You win!");
                break;
            }
            if (isBoardFull()) {
                System.out.println("It's a tie!");
                break;
            }

            System.out.println("AI's turn...");
            aiMove();
            printBoard();
            if (isGameOver(ai)) {
                System.out.println("AI wins!");
                break;
            }
            if (isBoardFull()) {
                System.out.println("It's a tie!");
                break;
            }
        }
        scanner.close();
    }

    private static void playerMove(Scanner scanner) {
        int row, col;
        while (true) {
            System.out.print("Enter your move (row and column): ");
            row = scanner.nextInt();
            col = scanner.nextInt();
            if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == ' ') {
                board[row][col] = player;
                break;
            } else {
                System.out.println("This move is not valid");
            }
        }
    }

    private static void aiMove() {
        int[] bestMove = minimax(board, ai);
        board[bestMove[1]][bestMove[2]] = ai;
    }

    private static int[] minimax(char[][] board, char currentPlayer) {
        char opponent = (currentPlayer == ai) ? player : ai;

        if (isGameOver(ai))
            return new int[] { 1 };
        if (isGameOver(player))
            return new int[] { -1 };
        if (isBoardFull())
            return new int[] { 0 };

        int bestScore = (currentPlayer == ai) ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        int[] bestMove = new int[3];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ') {
                    board[i][j] = currentPlayer;
                    int score = minimax(board, opponent)[0];
                    board[i][j] = ' ';

                    if ((currentPlayer == ai && score > bestScore) ||
                            (currentPlayer == player && score < bestScore)) {
                        bestScore = score;
                        bestMove = new int[] { score, i, j };
                    }
                }
            }
        }
        return bestMove;
    }

    private static boolean isGameOver(char player) {
        for (int i = 0; i < 3; i++)
            if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
                    (board[0][i] == player && board[1][i] == player && board[2][i] == player))
                return true;
        return (board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
                (board[0][2] == player && board[1][1] == player && board[2][0] == player);
    }

    private static boolean isBoardFull() {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == ' ')
                    return false;
        return true;
    }

    private static void printBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j]);
                if (j < 2)
                    System.out.print(" | ");
            }
            System.out.println();
            if (i < 2)
                System.out.println("---------");
        }
        System.out.println();
    }
}
