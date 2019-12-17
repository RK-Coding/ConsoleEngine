import ConsoleEngine as CE #Need to be in same direcory


CE.set_title('Smiley Face')
CE.set_draw_color('2')
CE.set_size(10, 120)
Face = CE.Sprite([['1  1'], [' '], ['-------']], 2, 2) #Each string in list is a part and each list is a new line
#'1 1' part 1 line 1
#' ' part 2 line 2
#'-------' part 3 line 3

CE.start_up(10, 10)
while True:
    CE.render(0)
    CE.erase()
    Face.draw()
    Face.right(1)
