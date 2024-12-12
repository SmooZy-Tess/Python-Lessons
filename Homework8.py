import re

print("--------------number 3--------------")

def replace_time(text):
    time_pattern = r'\b(2[0-3]|[01]?[0-9]):([0-5][0-9])(:([0-5][0-9]))?\b'
    result = re.sub(time_pattern, '(TBD)', text)
    return result

text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
otext = replace_time(text)
print(otext)

print("--------------number 4--------------")

def abb(text):
    abbreviation = r'\b([A-Z]{2,}(?:\s+[A-Z]{2,})*)\b'
    abbreviations = re.findall(abbreviation, text)
    abbreviations_s = sorted(set(abbr.strip() for abbr in abbreviations))
    return abbreviations_s


texti = "В этом документе указаны ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и другие аббревиатуры, такие как ФСБ и МВД."
abbreviations = abb(texti)
print(abbreviations)