travel_log = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'Lille', 'Dijon']
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart']
    },
]


def add_new_country(country, num_visits, cities_visited):
    new_country = {
        'country': country,
        'visits': num_visits,
        'cities': cities_visited,
    }
    travel_log.append(new_country)


add_new_country('Russia', 2, ['Moscow', 'Saint Petersburg'])
print(travel_log)
