# Main applikasjon - Snake

def app_started(app):
    
    app.direction = 'east'
    app.info_mode = True
    app.board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,-1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    app.snake_size = 3
    app.head_pos = (3, 4)
    app.state = 'startup'
    app.timer_delay = 300
    
    app.cx = app.width/2
    app.cy = app.height/2
    
    app.highscore_sum = 0
    
    if 'highscore_liste' not in app.__dict__:
        app.highscore_liste = []
    
def timer_fired(app):
    '''Får slangen til å bevege seg'''
    if app.info_mode == False and app.state == 'active':
        move_snake(app)

def key_pressed(app, event):
    '''Funksjon som registrerer tastetrykk'''
    if event.key == 'i':
            app.info_mode = not app.info_mode
    
    elif app.state == 'active':
        if event.key == 'Space':
            move_snake(app)
        elif event.key == 'Up':
            app.direction = 'north'
        elif event.key == 'Down':
            app.direction = 'south'
        elif event.key == 'Left':
            app.direction = 'west'
        elif event.key == 'Right':
            app.direction = 'east'
            
def mouse_pressed(app, event):
    app.cx = event.x
    app.cy = event.y
    
    if app.state == 'startup':
        check_mouseclick(app)
        
    elif app.state == 'gameover':
        check_mouseclick(app)
        
    elif app.state == 'highscore':
        check_mouseclick(app)
    
def redraw_all(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='#f8dff3', outline='')
    centerx = app.width/2
    centery = app.height/2
    
    # Tegner info
    if app.info_mode == True:
        canvas.create_text(centerx, 20,
                           text=f'Direction: {app.direction} Head_pos: {app.head_pos} Size: {app.snake_size} State: {app.state}')
    
    # Tegner start meny
    if app.state == 'startup':
        canvas.create_rectangle(app.width * 0.3, app.height * 0.2, app.width * 0.7, app.height * 0.3, fill='#639d62', outline='')
        canvas.create_rectangle(app.width * 0.3, app.height * 0.4, app.width * 0.7, app.height * 0.5, fill='#e7678d', outline='')
        canvas.create_rectangle(app.width * 0.3, app.height * 0.6, app.width * 0.7, app.height * 0.7, fill='#e7678d', outline='')
        canvas.create_rectangle(app.width * 0.3, app.height * 0.8, app.width * 0.7, app.height * 0.9, fill='#dd225a', outline='')
        
        canvas.create_text(centerx, app.height * 0.25, 
                           text='START', 
                           fill='white', 
                           font='Arial')
        canvas.create_text(centerx, app.height * 0.45, 
                           text='HIGHSCORES', 
                           fill='white', 
                           font='Arial')
        canvas.create_text(centerx, app.height * 0.65, 
                           text='INFO MODE', 
                           fill='white', 
                           font='Arial')
        canvas.create_text(centerx, app.height * 0.85, 
                           text='QUIT', 
                           fill='white', 
                           font='Arial')
    
    # Tegner highscore menyen
    if app.state == 'highscore':
        canvas.delete('all')
        canvas.create_rectangle(0, 0, app.width, app.height, fill='#f8dff3', outline='')

        y = app.height/100
        
        canvas.create_rectangle(5, app.height - 40, 115, app.height - 10, fill='#e7678d', outline='')
        canvas.create_text(60, app.height - 25,
                           text='Back to menu',
                           font=('Arial', 10),
                           fill='white')
        
        canvas.create_text(app.width/2, y + 20,
                           text=f'HIGHSCORE: {app.highscore_sum}',
                           font=('Arial', 20))

        if app.highscore_liste != []:
            y += 50
            for score in app.highscore_liste:
                y += 30
                canvas.create_text(app.width/2, y,
                                   text=f'{score}', 
                                   font=('Arial', 18))
              
    # Tegner brettet
    if app.state == 'active':
        draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.info_mode)
    
    # Tegner gameover meny
    if app.state == 'gameover':
        # if app.snake_size > max(app.highscore_liste):
        #     app.highscore_sum = app.snake_size
        #     canvas.create_text(centerx, centery - 100,
        #                        text='NEW HIGHSCORE',
        #                        fill='black',
        #                        font=('Arial', 10, 'bold'))
        
        canvas.create_text(centerx, centery - 35,
                           text=f'GAME OVER',
                           fill='#ee7192',
                           font=('Arial', 10, 'bold'))
        
        canvas.create_text(centerx, centery - 70,
                           text=f'{app.snake_size}',
                           fill='#ee7192',
                           font=('Arial', 40))
        
        canvas.create_rectangle(app.width * 0.3, centery - 20, app.width * 0.7, centery + 20, fill='#639d62', outline='')
        canvas.create_rectangle(app.width * 0.3, centery - 20, app.width * 0.7, centery + 20, fill='#639d62', outline='')

        canvas.create_text(centerx, centery,
                           text=f'RETRY',
                           fill='white',
                           font=('Arial', 18, 'bold'))
        
        # Tegner victory screen:
        # if app.status == 'victory':
        #     canvas.create_text(centerx, centery,
        #                        text='VICTORY',
        #                        fill='#ee7192',
        #                        font=('Arial', 30))
        #     
        #     canvas.create_text(60, app.height - 25,
        #                    text='Back to menu',
        #                    font=('Arial', 10),
        #                    fill='white')
    
def move_snake(app):
    app.head_pos = get_next_head_position(app.head_pos, app.direction)
    row, col = app.head_pos
    
    if is_legal_move(app.head_pos, app.board) == False:
        app.state = 'gameover'
        app.highscore_liste.insert(0, app.snake_size)
        return
    
    elif app.board[row][col] == -1:
        app.snake_size += 1
        add_apple_at_random_location(app.board)
        
    else:
        app.board = subtract_one_from_all_positives(app.board)
        
    app.board[row][col] = app.snake_size
    
def get_next_head_position(head_pos, direction):
    '''Returnerer den nye posisjonen til hodet'''
    row, col = head_pos
    if direction == 'north':
        row -= 1
    elif direction == 'south':
        row += 1
    elif direction == 'east':
        col += 1
    elif direction == 'west':
        col -= 1
    return (row, col)

def subtract_one_from_all_positives(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0:
                grid[i][j] -= 1
    
    return grid
                
def add_apple_at_random_location(grid):
    while True:
        rand_row = random.choice(range(len(grid)))
        rand_col = random.choice(range(len(grid[0])))
        if grid[rand_row][rand_col] == 0:
            grid[rand_row][rand_col] -= 1
            return
        
def is_legal_move(pos, board):
    row, col = pos
    if (row in range(len(board)) and
    col in range(len(board[0])) and
    (board[row][col] == 0 or board[row][col] == -1)):
        return True
    else:
        return False
    
def check_mouseclick(app):
    '''Sjekker hvor museklikket er'''
    centerx = app.width/2
    centery = app.height/2
    
    # Sjekker for Gameover og starter spillet på nytt
    if app.state == 'gameover':
        if point_in_rectangle(app.width * 0.3, centery - 20, app.width * 0.7, centery + 20, app.cx, app.cy):
            app.state = 'startup'
            app_started(app)
    
    # Starter spillet og tar av infomode
    elif app.state == 'startup':
        if point_in_rectangle(app.width * 0.3, app.height * 0.2, app.width * 0.7, app.height * 0.3, app.cx, app.cy):
            app.state = 'active'
            app.info_mode = not app.info_mode
    
        # Viser highscore
        if point_in_rectangle(app.width * 0.3, app.height * 0.4, app.width * 0.7, app.height * 0.5, app.cx, app.cy):
            app.state = 'highscore'
            app.info_mode = not app.info_mode

        # Viser brettet i infomodus
        if point_in_rectangle(app.width * 0.3, app.height * 0.6, app.width * 0.7, app.height * 0.7, app.cx, app.cy):
            app.info_mode = not app.info_mode

        # Avslutter spillet
        if point_in_rectangle(app.width * 0.3, app.height * 0.8, app.width * 0.7, app.height * 0.9, app.cx, app.cy): 
            sys.exit()
    
    elif app.state == 'highscore':
        if point_in_rectangle(5, app.height - 40, 115, app.height - 10, app.cx, app.cy):
            print(app.cx, app.cy)
            app.state = 'startup'
            app.info_mode = not app.info_mode
            app_started(app)
           
        
def point_in_rectangle(x1, y1, x2, y2, xp, yp):
    '''Finner ut om punktet er i rektangelet'''
    return ((xp <= max(x1, x2) and xp >= min(x1, x2)) and
             (yp <= max(y1, y2) and yp >= min(y1, y2)))
    
if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    from snake_view import draw_board
    import random
    import sys
    run_app(width=500, height=400, title='Snake')