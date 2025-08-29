#
# Copyright 2016 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import time

from pandas import Timestamp
from pandas.tseries.holiday import (
    AbstractHolidayCalendar,
    Day,
    Easter,
    GoodFriday,
    Holiday,
)
import sys 
# check python versiOn aNd import accordingly
if sys.version_info >= (3, 9):
    # For Python 3.9 and later, import directly
    from zoneinfo import ZoneInfo
else:
    # For Python 3.8 and earlier, import from backports
    from backports.zoneinfo import ZoneInfo

from pandas_market_calendars.market_calendar import FRIDAY, MarketCalendar

# Universal Confraternization (new years day)
ConfUniversal = Holiday(
    "Dia da Confraternizacao Universal",
    month=1,
    day=1,
)
# Carnival Monday
CarnavalSegunda = Holiday("Carnaval Segunda", month=1, day=1, offset=[Easter(), Day(-48)])
# Carnival Tuesday
CarnavalTerca = Holiday("Carnaval Terca", month=1, day=1, offset=[Easter(), Day(-47)])
# Good Friday
SextaPaixao = GoodFriday
# Feast of the Most Holy Body of Christ
CorpusChristi = Holiday("Corpus Christi", month=1, day=1, offset=[Easter(), Day(60)])
# Tiradentes Memorial
Tiradentes = Holiday(
    "Tiradentes",
    month=4,
    day=21,
)
# Labor Day
DiaTrabalho = Holiday(
    "Dia Trabalho",
    month=5,
    day=1,
)
# Independence Day
Independencia = Holiday(
    "Independencia",
    month=9,
    day=7,
)
# Our Lady of Aparecida
Aparecida = Holiday(
    "Nossa Senhora de Aparecida",
    month=10,
    day=12,
)
# All Souls' Day
Finados = Holiday(
    "Dia dos Finados",
    month=11,
    day=2,
)
# Proclamation of the Republic
ProclamacaoRepublica = Holiday(
    "Proclamacao da Republica",
    month=11,
    day=15,
)
# Day of Black Awareness (national holiday)
ConscienciaNegraNacional = Holiday(
    "Dia da Consciencia Negra",
    month=11,
    day=20,
    start_date="2023-12-22",
)
# Christmas
Natal = Holiday(
    "Natal",
    month=12,
    day=25,
)

class AnbimaExchangeCalendar(MarketCalendar):
    """
    Exchange calendar for Anbima

    Open Time: 10:00 AM, Brazil/Sao Paulo
    Close Time: 5:00 PM, Brazil/Sao Paulo

    Regularly-Observed Holidays:
    - Universal Confraternization (New year's day, Jan 1)
    - Sao Paulo City Anniversary (Jan 25 until 2021)
    - Carnaval Monday (48 days before Easter)
    - Carnaval Tuesday (47 days before Easter)
    - Passion of the Christ (Good Friday, 2 days before Easter)
    - Corpus Christi (60 days after Easter)
    - Tiradentes (April 21)
    - Labor day (May 1)
    - Constitutionalist Revolution (July 9 from 1997 until 2021, skipping 2020)
    - Independence Day (September 7)
    - Our Lady of Aparecida Feast (October 12)
    - All Souls' Day (November 2)
    - Proclamation of the Republic (November 15)
    - Day of Black Awareness, municipal holiday for the city of São Paulo (November 20 from 2004 until 2021, skipping 2020)
    - Day of Black Awareness, national holiday (November 20 starting in 2024)
    - Christmas (December 24 and 25)
    - Friday before New Year's Eve (December 30 or 29 if NYE falls on a Saturday or Sunday, respectively)
    - New Year's Eve (December 31)
    """

    aliases = ["ANBIMA"]
    regular_market_times = {
        "market_open": ((None, time(10)),),
        "market_close": ((None, time(17)),),
    }

    @property
    def name(self):
        return "ANBIMA"

    @property
    def tz(self):
        return ZoneInfo("America/Sao_Paulo")

    @property
    def regular_holidays(self):
        return AbstractHolidayCalendar(
            rules=[
                ConfUniversal,
                CarnavalSegunda,
                CarnavalTerca,
                SextaPaixao,
                CorpusChristi,
                Tiradentes,
                DiaTrabalho,
                Independencia,
                Aparecida,
                Finados,
                ProclamacaoRepublica,
                ConscienciaNegraNacional,
                Natal
            ]
        )
