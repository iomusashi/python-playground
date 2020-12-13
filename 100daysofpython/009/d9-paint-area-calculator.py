def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    return round(number_of_cans)

test_h = 2
test_w = 4
coverage = 5
cans = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f'You\'ll need {cans} cans of paint.')
