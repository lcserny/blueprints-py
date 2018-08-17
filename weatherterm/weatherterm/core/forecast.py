from datetime import date

from .forecast_type import ForecastType


class Forecast:
    def __init__(self, current_temp, humidity, wind, high_temp=None, low_temp=None,
                 description="", forecast_date=None, forecast_type=ForecastType.TODAY):
        self.current_temp = current_temp
        self.humidity = humidity
        self.wind = wind
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.description = description
        self.forecast_type = forecast_type

        if forecast_date is None:
            self.forecast_date = date.today()
        else:
            self.forecast_date = forecast_date

    @property
    def forecast_date(self):
        return self.forecast_date

    @forecast_date.setter
    def forecast_date(self, forecast_date):
        self.forecast_date = forecast_date.strftime("%a %b %d")

    @property
    def current_temp(self):
        return self.current_temp

    @property
    def humidity(self):
        return self.humidity

    @property
    def wind(self):
        return self.wind

    @property
    def description(self):
        return self.description

    def __str__(self):
        temperature = None
        offset = " " * 4

        if self.forecast_type == ForecastType.TODAY:
            temperature = (f'{offset}{self._current_temp}\xb0\n'
                           f'{offset}High {self._high_temp}\xb0 / '
                           f'Low {self._low_temp}\xb0 ')
        else:
            temperature = (f'{offset}High {self._high_temp}\xb0 / '
                           f'Low {self._low_temp}\xb0 ')

        return (f'>> {self.forecast_date}\n'
                f'{temperature}'
                f'({self._description})\n'
                f'{offset}Wind: '
                f'{self._wind} / Humidity: {self._humidity}\n')
