#!/usr/bin/python3

RMSection = """[Rainmeter]
Update=1000
DynamicWindowSize=1
AccurateText=1
"""

variables = """[Variables]
ALB=6,0,239
BOT=0,210,190
GAS=255,255,255
GIO=150,0,0
GRO=120,120,120
HAM=0,210,190
KVY=255,255,255
LAT=0,130,250
LEC=220,0,0
MAG=120,120,120
NOR=255,135,0
OCO=255,245,0
PER=245,150,200
RAI=150,0,0
RIC=255,245,0
RUS=0,130,250
SAI=255,135,0
STR=245,150,200
VER=6,0,239
VET=220,0,0
"""

styles = """[HeaderStyle]
FontFace=Formula1 Display Regular
SolidColor=000000f4
FontColor=ffffff
X=R
StringCase=Upper
Padding=10,5,10,5
AntiAlias=1
[EntryStyle]
FontFace=Formula1 Display Bold
FontColor=ffffff
Padding=5,3,0,3
X=10R
Y=r
AntiAlias=1
"""

heading = """[GrandPrixHeading]
Meter=String
MeasureName=GrandPrixNameMeasure
MeterStyle=HeaderStyle
StringAlign=Center
ClipString=2
W=260
X=140
Y=R
"""

topLine = """[TopLine]
Meter=Shape
Shape=Line 0,0,280,0 | StrokeWidth 5 | Stroke Color 208,5,4,255
"""

EntryTemplate = """[BackDrop{n}]
Meter=Image
Y=R
H=25
W=280
SolidColor=00000099
[Position{n}]
Meter=String
MeasureName=Driver{n}PositionMeasure
MeterStyle=EntryStyle
StringAlign = Center
W=20
Padding=0,3,0,3
X=32r
Y=r
[DriverColor{n}]
Meter=Shape
MeasureName=Driver{n}CodeMeasure
X=18r
Y=r
Shape=Line 0,0,0,18 | StrokeWidth 4 | Stroke Color [#[&Driver{n}CodeMeasure]]
Padding=5,3,0,3
DynamicVariables=1
[DriverCode{n}]
Meter=String
MeasureName=Driver{n}CodeMeasure
MeterStyle=EntryStyle
W=40
[Time{n}]
Meter=String
MeasureName=Driver{n}TimeMeasure
MeterStyle=EntryStyle
StringAlign=Right
X=100R
W=90
[Points{n}]
Meter=String
MeasureName=Driver{n}PointsMeasure
MeterStyle=EntryStyle
X=15r
H=19
Text=+%1
"""

with open("skin.ini", "w") as fp:
    fp.write(RMSection)
    fp.write(styles)
    fp.write(heading)
    fp.write(variables)
    fp.write("@include=measures.inc\n")
    for n in range (1,21):
        fp.write(EntryTemplate.format(n=n))
    fp.write(topLine)