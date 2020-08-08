#!/usr/bin/env python
# coding: utf-8

# In[10]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[11]:


def player_input():
    marker=''
    while marker !='X' and marker!='O':
        marker=input('Player1: choose X Or O: ').upper()
    if marker =='X':
        return ('X',"O")
    else:
        return ('O',"X")


# In[12]:


def place_marker(board, marker, position):
    
    board[position]=marker


# In[24]:


def win_check(board, marker):
     return ((board[7] == marker and board[8] == marker and board[9] == marker) or 
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[1] == marker and board[2] == marker and board[3] == marker) or 
    (board[7] == marker and board[4] == marker and board[1] == marker) or 
    (board[8] == marker and board[5] == marker and board[2] == marker) or 
    (board[9] == marker and board[6] == marker and board[3] == marker) or 
    (board[7] == marker and board[5] == marker and board[3] == marker) or 
    (board[9] == marker and board[5] == marker and board[1] == marker)) 
    


# In[20]:


import random

def choose_first():
    flip=random.randint(0,1)
    if flip==1:
        return 'player2'
    else:
        return 'player1'


# In[14]:


def space_check(board, position):
    
     return board[position]==' '


# In[15]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[16]:


def player_choice(board):
    
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choose a position: (1-9)'))
    return position


# In[17]:


def replay():
    choice=''
    choice =input("play again? enter Yes or No")
    return choice =='Yes'


# 
# 

# In[ ]:


print('Welcome to Tic Tac Toe!')
while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    
    turn = choose_first()
    print(turn+'will go first')
    
    play_game=input(' ready to play ? y or n')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        if turn =='player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!")
                    game_on=False
                else:
                    turn='player2'
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!")
                    game_on=False
                else:
                    turn='player1'
    if not replay():
        break
            
       


# In[ ]:




