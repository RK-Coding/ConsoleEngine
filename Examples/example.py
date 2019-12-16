import ConsoleEngine as CE


CE.set_title('Smiley Face')
CE.set_draw_color('2')
CE.set_size(10, 120)
Face = CE.Sprite([['1  1'], [' '], ['-------']], 2, 2)

CE.start_up(10, 10)
while True:
    CE.render(0)
    CE.erase()
    Face.draw()
    Face.right(1)
