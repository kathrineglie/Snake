# tegner grid

def draw_board(canvas, x1, y1, x2, y2, board, info_mode):
    '''Lager grid'''
    antall_rows = len(board)
    antall_cols = len(board[0])
    
    width = (max(x1, x2) - min(x1, x2))/antall_cols
    height = (max(y1, y2) - min(y1, y2))/antall_rows
    top = y1
    for i in range(antall_rows):
        left = x1
        for j in range(antall_cols):
            num = board[i][j]
            color = get_color(num)
            
            if info_mode == True:
                canvas.create_text(left + width/2, top + height/2,
                                    text=f'{i},{j}\n{num}')
            
            if num == -1:
                canvas.create_rectangle(left, top, left + width, top + height, fill='white')
                canvas.create_oval(left + 3, top + 3, left + width - 3, top + height - 3, fill=color)
            
            else:
                canvas.create_rectangle(left, top, left + width, top + height, fill=color)
            
            left += width
        top += height
            
def get_color(num):
    '''Hjelpe funksjon til å hente farge'''
    # bakgrunn
    if num == 0:
        color = 'white'
    # slangen
    elif num > 0:
        color = '#ee7192'
    # eple
    elif num < 0:
        color = '#d82159'
    
    return color
