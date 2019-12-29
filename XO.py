import numpy as np
class board():
    def __init__(self):
        self.board = np.zeros((3,3), str)
        self.trylist = self.board.copy()
        self.board[0][0] = 'O'
        self.printt()
    def printt(self):
        print(self.board)
    def checkWin(self):
        for i in range(3):
            if(self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][2] != ''):
                return self.board[i][0] 
            if(self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[2][i] != ''):
                return self.board[0][i] 
            if(i == 1):
                if(self.board[i-1][i-1] == self.board[i][i] and self.board[i][i] == self.board[i+1][i+1] and self.board[i+1][i+1] != ''):
                    return self.board[i-1][i-1] 
                if(self.board[i+1][i-1] == self.board[i][i] and self.board[i][i] == self.board[i-1][i+1] and self.board[i-1][i+1] != ''):
                    return self.board[i+1][i-1]
        return ''
    
    def checkDraw(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == ''):
                    return False 
        return True
    
    def X(self,index):
        index -= 1
        residual = index % 3
        decimal = int(index / 3)
        self.board[decimal][residual] = 'X'
        if(self.checkWin()):
            print(self.checkWin() + ' ' + 'Win !!!')
            return
        if(self.checkDraw()):
            print('Draw !!')
        listOfEmpty = []
        listOfTargetValue = []
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == ''):
                    listOfEmpty.append((i,j))
        for i in range(len(listOfEmpty)):
            listOfTargetValue.append(self.tryO(listOfEmpty[i]))
        maxTargetValueIndex = listOfEmpty[listOfTargetValue.index(max(listOfTargetValue))]
        self.board[maxTargetValueIndex[0]][maxTargetValueIndex[1]] = 'O'
        self.printt()
        if(self.checkWin()):
            print(self.checkWin() + ' ' + 'Win !!!')
        if(self.checkDraw()):
            print('Draw !!')
        
                    
    def tryO(self, truple):
        self.trylist = self.board.copy()
        self.trylist[truple[0]][truple[1]] = 'O'
        return self.TargetFunction()
    def TargetFunction(self):
        return 1 - self.calcb('X') + 3 * self.calcb('O')
    
    def clear(self):
        self.board = np.zeros((3,3), str)
        self.printt()
    def calcb(self, key):
        summ = 0
        if(key == 'X'):
            key2 = 'O'
        else:
            key2 = 'X'
        for i in range(3):
            if(list(self.trylist[i,:]).count(key2) == 0):
                summ += list(self.trylist[i,:]).count(key)
            if(list(self.trylist[:,i]).count(key2) == 0):
                summ += list(self.trylist[:,i]).count(key)
        diag1 = [self.trylist[0][0], self.trylist[1][1], self.trylist[2][2]]
        diag2 = [self.trylist[2][0], self.trylist[1][1], self.trylist[0][2]]
        if(diag1.count(key2) == 0):
            summ += diag1.count(key)
        if(diag2.count(key2) == 0):
            summ += diag2.count(key)
        return summ

eiei = board()
eiei.printt()
eiei.X(2)

# 1, 2, 3
# 4, 5, 6
# 7, 8, 9





