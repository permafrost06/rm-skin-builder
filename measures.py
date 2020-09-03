#!/usr/bin/python3
GrandPrixNameMeasureRegExp = """(?siU)\\"raceName\\":\\"(.*)\\","""

GrandPrixNameMeasure = """[GrandPrixNameMeasure]
Measure=WebParser
URL=http://ergast.com/api/f1/current/last/results.json
RegExp=\"{RegExp}\"
StringIndex=1
"""

ResultsMeasureRegExp = """(?siU)\\"Results\\":\\[{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)},{(.*)}\\]"""

ResultsMeasure = """[ResultsMeasure]
Measure=WebParser
URL=http://ergast.com/api/f1/current/last/results.json
RegExp=\"{RegExp}\"
"""

DriverMeasureRegExp = [
    "\"number\":\"(.*)\".*",
    "\"positionText\":\"(.*)\".*",
    "\"points\":\"(.*)\".*",
    "\"code\":\"(.*)\".*",
    "\"nationality\":\"(.*)\".*",
    "\"name\":\"(.*)\".*",
    "\"grid\":\"(.*)\".*",
    "\"status\":\"(.*)\".*",
    "{\"millis\":\".*\",\"time\":\"(.*)\"",
]

FieldMeasureTemplate = """[Driver{n}{Field}Measure]
Measure=WebParser
URL=[ResultsMeasure]
RegExp="(?siU){RegExp}"
StringIndex={n}
StringIndex2=1
"""

MeterTemplate = """[Driver{n}{Field}Meter]
meter=string
x={xPos}{xRel}
y=0{yRel}
fontcolor=ffffff
measurename=Driver{n}{Field}Measure
DynamicVariables=1
"""

fields = [
    "Number",
    "Position",
    "Points",
    "Code",
    "Nationality",
    "Constructor",
    "GridPosition",
    "Status",
    "Time",
]

with open("measures.inc", "w") as fp:
    fp.write(GrandPrixNameMeasure.format(RegExp=GrandPrixNameMeasureRegExp))
    fp.write(ResultsMeasure.format(RegExp=ResultsMeasureRegExp))
    for n in range(1, 21):
        for field in fields:
            fp.write(FieldMeasureTemplate.format(
                n=n, Field=field, RegExp=DriverMeasureRegExp[fields.index(field)]))
            if field == "Position":
                fp.write('Substitute="R":"DNF","W":"DNS"\n')