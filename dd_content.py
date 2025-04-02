def get_random_quote(quotes_file='quotes.csv'):
    try:
        with open(quotes_file) as csvfile:
                quotes = [{'author':line[0],
                           'quote': line[1] for line in csv.reader(csvfile, delimiter ='|')]
    except Exception as e:
        quotes = [{'author':'Eric Idle',
                   'quote':'Always look on the bright side of life.'}]
    return random.choice(quotes)

def get_weather_forecast():
    try:
        api_key =
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}'
        data = json.load(request.urlopen(url))

        forecast = {'city': data['city']['name'],
                    'country':data['city']['country'],
                    'periods':list()}
        for period in data['list'][0:9]:
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period['weather']
        return forecast
                                                                                    except 

def get_twitter_trend():
    pass

def get_wikipedia_article():
    pass

if __name__ = "__main__":
    pass
