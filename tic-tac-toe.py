# ---Code Section---
# Tic Tac Toe Game

# Initialize the board
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# פונקציה שבודקת אם השחקן הנוכחי ניצח
def check_winner():
    # שורות
    if board[0] == board[1] == board[2] == current_player:
        return True
    if board[3] == board[4] == board[5] == current_player:
        return True
    if board[6] == board[7] == board[8] == current_player:
        return True
    
    # עמודות
    if board[0] == board[3] == board[6] == current_player:
        return True
    if board[1] == board[4] == board[7] == current_player:
        return True
    if board[2] == board[5] == board[8] == current_player:
        return True
    
    # אלכסונים
    if board[0] == board[4] == board[8] == current_player:
        return True
    if board[2] == board[4] == board[6] == current_player:
        return True
    
    return False  # חשוב! אם אין ניצחון

# פונקציה שבודקת אם יש תיקו (הלוח מלא בלי מנצח)
def check_tie():
    if all(cell in ['X', 'O'] for cell in board):
        return True
    return False

# משתנה שמחזיק את השחקן הנוכחי
current_player = 'X'

# לולאת המשחק הראשית
while True:
    print_board()
    print(f"תור של שחקן {current_player}")
    
    # לולאה פנימית - מבקשת בחירה תקינה
    while True:
        choice = input("בחרי מספר תא (1-9): ")
        if choice.isdigit() and 1 <= int(choice) <= 9:
            position = int(choice)
            index = position - 1
            if board[index] not in ['X', 'O']:
                # כאן הבחירה תקינה ופנויה
                board[index] = current_player
                break  # יוצאים מהלולאה הפנימית
            else:
                print("התא הזה כבר תפוס! בחרי תא אחר.")
        else:
            print("בבקשה הקלידי מספר תקין בין 1 ל-9.")
    
    # בודקים ניצחון לפני שמחליפים שחקן!
    if check_winner():
        print_board()
        print(f"כל הכבוד! שחקן {current_player} ניצח!!! 🎉")
        break
    
    # בודקים אם יש תיקו
    if check_tie():
        print_board()
        print("הלוח מלא – תיקו! 🤝")
        break
    
    # רק עכשיו מחליפים שחקן
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    else:

        current_player = 'X'
