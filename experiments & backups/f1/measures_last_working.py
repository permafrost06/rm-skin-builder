#!/usr/bin/python3

RMSection = """[Rainmeter]
Update=1000
DynamicWindowSize=1
AccurateText=1
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
    "\"time\":\"(.*)\".*"
]

DriverMeasureTemplate = """[Driver{n}Measure]
Measure=WebParser
URL=[ResultsMeasure]
RegExp="{RegExp}"
StringIndex={n}
"""

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

# fieldsIndex = {"Number":1, "Position":2, "Points":3, "Code":4, "Nationality":5, "Constructor":6, "ConstructorCountry":7, "GridPosition":8, "Laps":9, "Status":10, "Time":11}

with open("skin.ini", "w") as fp:
    fp.write(RMSection)
    fp.write(ResultsMeasure.format(RegExp=ResultsMeasureRegExp))
    for n in range(1, 21):
        xPos = '0'
        xRel = '0'
        yRel = 'R'
        for field in fields:
            fp.write(FieldMeasureTemplate.format(
                n=n, Field=field, RegExp=DriverMeasureRegExp[fields.index(field)]))
            fp.write(MeterTemplate.format(
                n=n, Field=field, xPos=xPos, xRel=xRel, yRel=yRel))
            xPos = '5'
            xRel = 'R'
            yRel = 'r'
