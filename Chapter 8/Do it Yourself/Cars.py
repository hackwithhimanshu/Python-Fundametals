def car_info(manufacturer, model_name, **extra_info):
    extra_info['Manufacturer'] = manufacturer
    extra_info['Model Name'] = model_name
    return extra_info

car = car_info('subaru', 'outback',
               color = 'blue',
               tow_package = True)

print(car)