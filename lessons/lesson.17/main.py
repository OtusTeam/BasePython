from weather import Weather


if __name__ == '__main__':
    weather = Weather('Москва')
    report = weather.create_forecast()
    print(report)
