def city_country_name(city, country, population=None):
    if population:
        full_data = f"{city}, {country} - {int(population)}"
    else:
        full_data = f"{city}, {country}"

    return full_data.title()