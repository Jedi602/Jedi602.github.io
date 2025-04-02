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
    pass

def get_twitter_trend():
    pass

def get_wikipedia_article():
    pass

if __name__ = "__main__":
    pass
