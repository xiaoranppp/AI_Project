# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:19:49 2018

@author: xrpeng
"""
import random
import sys
import random
import math
ins={0:6,1:7,2:8,3:3,4:4,5:5,6:0,7:1,8:2}
s = int(sys.argv[1])
random.seed(s);
def seed():
    k=math.floor(9 * random.random())
    return ins[k]

    

class game:
      def __init__(self):
        '''Initialize parameters - the game board, moves stack and winner'''
        self.lastmoves = []
        self.winner = None
        self.board=['-','-','-','-','-','-','-','-','-']
        
      def get_empty(self):
          move = []
          for i in range(9):
                  if self.board[i]=='-':
                      move.append([i])       
          return move
      
      def mark(self,marker,pos):
        
           self.board[pos[0]] = marker
           self.lastmoves.append(pos[0])

      def revert(self):
        
          temp=self.lastmoves.pop()
          self.board[temp]= '-'
          self.winner = None

      def is_end(self):
        

          win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8), (2,4,6)]

          for i,j,k in win_positions:
              if (self.board[i] == self.board[j] == self.board[k] and self.board[i] != '-'):
                  self.winner = self.board[i]
                  return True

          if '-' not in self.board:
              self.winner = '-'
              return True

          return False
def stupidx(game,i):
    i=i/2
    move=seed()
    for i in range(10):
        if game.board[move]=='-':
           game.mark('x',[move])
           break
        else:
           move=seed()
          
    

def printgame(game):
    A=[]
    B=[]
    C=[]
    for i in range(3):
        A.append(game.board[i])
        B.append(game.board[i+3])
        C.append(game.board[i+6])
    print A
    print B
    print C
    return [A,B,C]
    
    
    
def getscore(game):
    if game.is_end()==True:
        if game.winner=='o':
            score=100
        elif game.winner=='x':
            score=-100
        else:
            score=0
    return score   

def smartO(gameinstance):
        move_position,score = maximized_move(gameinstance)
        gameinstance.mark('o',move_position)



def maximized_move(gameinstance):
        ''' Find maximized move'''    
        bestscore = None
        bestmove = None

        for m in gameinstance.get_empty():
            gameinstance.mark('o',m)
        
            if gameinstance.is_end():
                score =getscore(gameinstance)
            else:
                move_position,score = minimized_move(gameinstance)
        
            gameinstance.revert()
            
            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

def minimized_move(gameinstance):
        ''' Find the minimized move'''

        bestscore = None
        bestmove = None

        for m in gameinstance.get_empty():
            gameinstance.mark('x',m)
        
            if gameinstance.is_end():
                score = getscore(gameinstance)
            else:
                move_position,score = maximized_move(gameinstance)
        
            gameinstance.revert()
            
            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore


Game=game()
i=0
result={}
import csv

while not Game.is_end():
      print(i)
      if i%2==0:
          
          stupidx(Game,i)
          result[i]=printgame(Game)
          i=i+1
         
      else:
          #kk=AI('O')
          smartO(Game)
          result[i]=printgame(Game)
          i=i+1
with open('tictactoe.txt','wb') as fb:
      writer = csv.writer(fb)
      for j in range(i):
          writer.writerows(result[j])
          writer.writerows('\n')
          
fb.close()


      
