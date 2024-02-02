#coding:utf-8
import re
import math

units = {'一':1,
         '十':10,
         '百':100,
         '千':1000,
         '万':10000,
         '億':100000,
         '兆':1000000,
         '京':10000000}

def unichen(value_unit:str):
    if not bool(re.search(r'\d', value_unit)):
        return 'Please enter the numbers and units as shown in the example. (Ex.) 130百万円'
    else:
        value_unit_split = re.match(r'^([\d.]+)(\D+)$', value_unit)
        try:
            val, unit = float(value_unit_split.group(1)), value_unit_split.group(2)
        except AttributeError:
            return 'Please enter the number before the unit in half-width characters.'
        
        unit_split = list(unit)
        if unit_split[-1] == '円':
            del unit_split[-1]
        num_unit = [units.get(i) for i in unit_split]
        
        res = int(val * math.prod(num_unit))
        return res