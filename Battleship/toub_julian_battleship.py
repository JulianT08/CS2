import random
Ba1 = ' 1'
Ba2 = ' 2'
Ba3 = ' 3'
Ba4 = ' 4'
Ba5 = ' 5'
Bb1 = ' 6'
Bb2 = ' 7'
Bb3 = ' 8'
Bb4 = ' 9'
Bb5 = ' 10'
Bc1 = ' 11'
Bc2 = ' 12'
Bc3 = ' 13'
Bc4 = ' 14'
Bc5 = ' 15'
Bd1 = ' 16'
Bd2 = ' 17'
Bd3 = ' 18'
Bd4 = ' 19'
Bd5 = ' 20'
Be1 = ' 21'
Be2 = ' 22'
Be3 = ' 23'
Be4 = ' 24'
Be5 = ' 25'
Ua1 = ' '
Ua2 = ' '
Ua3 = ' '
Ua4 = ' '
Ua5 = ' '
Ub1 = ' '
Ub2 = ' '
Ub3 = ' '
Ub4 = ' '
Ub5 = ' '
Uc1 = ' '
Uc2 = ' '
Uc3 = ' '
Uc4 = ' '
Uc5 = ' '
Ud1 = ' '
Ud2 = ' '
Ud3 = ' '
Ud4 = ' '
Ud5 = ' '
Ue1 = ' '
Ue2 = ' '
Ue3 = ' '
Ue4 = ' '
Ue5 = ' '
bot_positions = [
    Ba1, Ba2, Ba3, Ba4, Ba5,
    Bb1, Bb2, Bb3, Bb4, Bb5,
    Bc1, Bc2, Bc3, Bc4, Bc5,
    Bd1, Bd2, Bd3, Bd4, Bd5,
    Be1, Be2, Be3, Be4, Be5
]
user_positions = [
    Ua1, Ua2, Ua3, Ua4, Ua5,
    Ub1, Ub2, Ub3, Ub4, Ub5,
    Uc1, Uc2, Uc3, Uc4, Uc5,
    Ud1, Ud2, Ud3, Ud4, Ud5,
    Ue1, Ue2, Ue3, Ue4, Ue5
]

bot_board = f'''
 ________________________
| {Ba1} || {Ba2} || {Ba3} || {Ba4} || {Ba5} |
 ________________________
| {Bb1} || {Bb2} || {Bb3} || {Bb4} || {Bb5} | 
 ________________________
| {Bc1} || {Bc2} || {Bc3} || {Bc4} || {Bc5} |
 ________________________
| {Bd1} || {Bd2} || {Bd3} || {Bd4} || {Bd5} |
 ________________________
| {Be1} || {Be2} || {Be3} || {Be4} || {Be5} |
 ________________________
 '''

def show_user_board():
    user_board = f'''
 ________________________
| {Ua1} || {Ua2} || {Ua3} || {Ua4} || {Ua5} |
 ________________________
| {Ub1} || {Ub2} || {Ub3} || {Ub4} || {Ub5} | 
 ________________________
| {Uc1} || {Uc2} || {Uc3} || {Uc4} || {Uc5} |
 ________________________
| {Ud1} || {Ud2} || {Ud3} || {Ud4} || {Ud5} |
 ________________________
| {Ue1} || {Ue2} || {Ue3} || {Ue4} || {Ue5} |
 ________________________
 '''
    print(user_board)
def bot_setup():
    ship = random.choice(bot_positions)
    ship = "S"
    return ship

# I NEED IT TO CHOOSE A RANDOM VARIABLE NOT VALUE

bot_setup()
print(bot_board)
bot_setup()
bot_setup()
bot_setup()
bot_setup()
print(bot_board)
#show_user_board()