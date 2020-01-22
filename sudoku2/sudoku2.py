def line_is_valid(row):
    tmp_dict = {}
    valid = True    
    
    if len(row) > 0:
        for r in row:
            if r in tmp_dict:
                tmp_dict[r] += 1
            else:
                tmp_dict[r] = 1
            
        if tmp_dict[max(tmp_dict, key=tmp_dict.get)] > 1:
            valid = False

    return valid
            
            
def grid_is_valid(grid):
    valid = True
    
    for i in range(len(grid)):
        row = [int(x) for x in grid[i] if x != '.']
        
        valid = line_is_valid(row)
        if not valid:
            break

    return valid
        
    
def sudoku2(grid):
    result = False
    
    #checando linhas
    rows_valid = grid_is_valid(grid)
    
    #checando colunas
    