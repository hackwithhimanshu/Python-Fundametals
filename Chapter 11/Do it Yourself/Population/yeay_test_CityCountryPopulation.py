from NewCityFunctions import city_country_name

def test_city_country_population_data():
    data_content = city_country_name('dhamtari', 'chhattisgarh', 500000)
    assert data_content == 'Dhamtari, Chhattisgarh - 500000'