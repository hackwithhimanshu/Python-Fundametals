from NewCityFunctions import city_country_name

def test_city_country_name():
    city_country = city_country_name('Bhilai', 'Chattisgarh')
    assert city_country == 'Bhilai, Chattisgarh - '



