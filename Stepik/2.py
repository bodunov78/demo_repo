def get_data_fig(*args, **kwargs):
    suma = [sum(args)]
    for x in ('type','color','closed','width'):
        if x in kwargs:
            suma.append(kwargs[x])

    return tuple(suma)



print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))
print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False,  width=10))
print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))