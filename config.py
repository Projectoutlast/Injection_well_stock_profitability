MONTHS_OF_WORKING = False  # взять в расчет только те скважины, которые работали последние Х месяцев

# расчет только с учетом скважин работающих на дату оценки
HAS_WORKING_HOURS_FOR_THE_LAST_YEAR = False   # расчет с учетом скважин, находившихся в работе за последний год

min_length_horizont_well = 150  # минимальная длина между точками Т1 и Т3, чтобы считать скважину горизонтальной
time_work_min = 0  # минимальное время работы скважины в месяц, дней

drainage_areas = None    # зона дренирования
dynamic_coefficient = None    # динамический коэффициент

# CONSTANT
DEFAULT_HHT = 0.1  # meters
MAX_DISTANCE: int = 1000  # default maximum distance from injection well for reacting wells

