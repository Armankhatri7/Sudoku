def make_row(row):
    final_row=[]
    for item in range(9):
        final_row.append(0)
    for item in range(9):
        final_row[8-item]=int(row%10)
        row=int(row/10)
    return final_row

def mod_range(s,t):
    r=[]
    for i in range(s):
        r.append(i)
    for i in range(s+1,t):
        r.append(i)
    return r

def display(matrix):
    for item in range(9):
        print(matrix[item])

def new_poss_matrix():
    poss_matrix=[]
    for x in range(9):
        matrix_two=[]
        for y in range(9):
            matrix_one=[]
            for z in range(9):
                matrix_one.append(z+1)
            matrix_two.append(matrix_one)
        poss_matrix.append(matrix_two)
    return poss_matrix

def setup(poss_matrix, matrix, check_matrix):
    for x in range(9):
        for y in range(9):
            if matrix[x][y]!=0:
                poss_matrix[x][y]=[matrix[x][y]]
                check_matrix[x][y]=1

def new_temp_matrix():
    temp_matrix=[]
    for x in range(9):
        matrix_two=[]
        for y in range(9):
            matrix_one=[]
            for z in range(9):
                matrix_one.append(0)
            matrix_two.append(matrix_one)
        temp_matrix.append(matrix_two)
    return temp_matrix

def set_check_matrix():
    check_matrix=[]
    for x in range(9):
        matrix_row=[]
        for y in range(9):
            matrix_row.append(0)
        check_matrix.append(matrix_row)
    return check_matrix

def update_matrices(check_matrix, poss_matrix, matrix):
    for x in range(9):
        for y in range(9):
            if len(poss_matrix[x][y])==1:
                check_matrix[x][y]=1
                matrix[x][y]=poss_matrix[x][y][0]

def bn(x,y):
    bn=(x//3)*3 + (y//3)
    return bn
        
def cond_remove(poss,value):
    if poss.count(value)!=0:
        poss.remove(value)

def box_contr(poss_matrix, matrix, check_matrix):
    for x in range(9):
        for y in range(9):
            if check_matrix[x][y]==1:
                i=bn(x,y)
                for p in range(3):
                    for q in range(3):
                        cond_remove(poss_matrix[p+(i//3)*3][q+(i%3)*3],matrix[x][y])
                poss_matrix[x][y].append(matrix[x][y])
            else:
                i=bn(x,y)
                for item in poss_matrix[x][y]:
                    check=True
                    for p in range(3):
                        x2=p+(i//3)*3
                        for q in range(3):
                            y2=q+(i%3)*3
                            if [x2,y2]!=[x,y]:
                                if poss_matrix[x2][y2].count(item)!=0:
                                    check=False
                                    break
                    if check==True:
                        poss_matrix[x][y]=[item]
    update_matrices(check_matrix,poss_matrix, matrix)


def row_contr(poss_matrix, matrix, check_matrix):
    for x in range(9):
        for y in range(9):
            if check_matrix[x][y]==1:
                for i in mod_range(y,9):
                    cond_remove(poss_matrix[x][i],matrix[x][y])
            else:
                for item in poss_matrix[x][y]:
                    check=True
                    for i in mod_range(y,9):
                        if poss_matrix[x][i].count(item)!=0:
                            check=False
                            break
                    if check==True:
                        poss_matrix[x][y]=[item]
    update_matrices(check_matrix,poss_matrix, matrix)


def matrix_unsolved(matrix):
    check=False
    for x in range(9):
        for y in range(9):
            if matrix[x][y]==0:
                check=True
                break
    return check

def col_contr(poss_matrix, matrix, check_matrix):
    for x in range(9):
        for y in range(9):
            if check_matrix[x][y]==1:
                for i in mod_range(x,9):
                    cond_remove(poss_matrix[i][y],matrix[x][y])
            else:
                for item in poss_matrix[x][y]:
                    check=True
                    for i in mod_range(x,9):
                        if poss_matrix[i][y].count(item)!=0:
                            check=False
                            break
                    if check==True:
                        poss_matrix[x][y]=[item]
    update_matrices(check_matrix,poss_matrix, matrix)

def make_copy(temp_matrix, poss_matrix):
    for x in range(9):
        for y in range(9):
            temp_matrix[x][y]=poss_matrix[x][y]
    return temp_matrix

matrix=[]
for item in range(9):
    row=make_row(int(input(f"Enter row {item + 1}: ")))
    matrix.append(row)
check_matrix=set_check_matrix()
poss_matrix=new_poss_matrix()
setup(poss_matrix,matrix, check_matrix)
temp_matrix=new_temp_matrix()
while temp_matrix!=poss_matrix:
    temp_matrix=make_copy(temp_matrix,poss_matrix)
    row_contr(poss_matrix,matrix,check_matrix)
    col_contr(poss_matrix,matrix,check_matrix)
    box_contr(poss_matrix,matrix,check_matrix)
display(poss_matrix)