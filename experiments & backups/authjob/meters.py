#!/usr/bin/python3

RMSection = """[Rainmeter]
Update=1000
DynamicWindowSize=1
BackgroundMode=2
SolidColor=48,48,48
AccurateText=1
"""

variables = """
[Variables]
JobParser=(?siU)<a.*href="(.*)".*"wpjb_jb_title">(.*)</span>.*wpjb_cat">(.*)</span>.*"wpjb_exp_text">(.*)</span>.*wpjb_type">(.*)</div>
"""

styles = """
[TextStyle]
FontFace=Poppins
FontColor=236,233,224
X=R
Y=r
AntiAlias=1
Padding=10,5,10,3

[HeadingStyle]
FonSize=14
FontWeight=700
Padding=10,15,10,4

[Column1]
W=320

[Column2]
W=80

[Column3]
W=60
"""

heading = """
[HeadingNameMeter]
Meter=String
MeterStyle=TextStyle | HeadingStyle | Column1
Text=Job Listing

[HeadingExperienceMeter]
Meter=String
MeterStyle=TextStyle | HeadingStyle | Column2
Text=Experience

[HeadingTypeMeter]
Meter=String
MeterStyle=TextStyle | HeadingStyle | Column3
Text=Type
"""

ulMeter = """
[HeadingUnderline]
Meter=Image
Y=R
X=5
W=510
H=2
SolidColor=236,233,224
"""

MainMeasure = """
[MainParseMeasure]
Measure=WebParser
URL=https://authlab.io/jobs/
RegExp=(?siU)<div class="wpjb_job_lists">(?(?=.*<div data-.*class="wpjb_each_job")(.*)<\/a>.*<\/div>)(?(?=.*<div data-.*class="wpjb_each_job")(.*)<\/a>.*<\/div>)(?(?=.*<div data-.*class="wpjb_each_job")(.*)<\/a>.*<\/div>)(?(?=.*<div data-.*class="wpjb_each_job")(.*)<\/a>.*<\/div>)(?(?=.*<div data-.*class="wpjb_each_job")(.*)<\/a>.*<\/div>)(?(?=.*<div data-.*class="wpjb_each_job")(.*)<\/a>.*<\/div>)
"""

EntryMeasuresTemplate = """
[Job{n}Link]
Measure=WebParser
URL=[MainParseMeasure]
RegExp=#JobParser#
StringIndex={n}
StringIndex2=1

[Job{n}Listing]
Measure=WebParser
URL=[MainParseMeasure]
RegExp=#JobParser#
StringIndex={n}
StringIndex2=2

[Job{n}Name]
Measure=WebParser
URL=[MainParseMeasure]
RegExp=#JobParser#
StringIndex={n}
StringIndex2=3

[Job{n}Experience]
Measure=WebParser
URL=[MainParseMeasure]
RegExp=#JobParser#
StringIndex={n}
StringIndex2=4

[Job{n}Type]
Measure=WebParser
URL=[MainParseMeasure]
RegExp=#JobParser#
StringIndex={n}
StringIndex2=5
"""

# [Job{n}LinkMeter]
# Meter=String
# MeasureName=Job{n}Link
# Y=R

# [Job{n}NameMeter]
# Meter=String
# MeasureName=Job{n}Name
# X=R
# Y=r

EntryTemplate = """
[Job{n}ListingMeter]
Meter=String
MeterStyle= TextStyle | Column1
MeasureName=Job{n}Listing
X=0
Y=R
LeftMouseUpAction=[Job{n}Link]

[Job{n}ExperienceMeter]
Meter=String
MeterStyle= TextStyle | Column2
MeasureName=Job{n}Experience
X=R
Y=r
LeftMouseUpAction=[Job{n}Link]

[Job{n}TypeMeter]
Meter=String
MeterStyle= TextStyle | Column3
MeasureName=Job{n}Type
X=R
Y=r
LeftMouseUpAction=[Job{n}Link]
"""

with open("skin.ini", "w") as fp:
    fp.write(RMSection)
    fp.write(styles)
    fp.write(heading)
    fp.write(ulMeter)
    fp.write(variables)
    fp.write(MainMeasure)
    for n in range (1,6):
        fp.write(EntryMeasuresTemplate.format(n=n))
    for n in range (1,6):
        fp.write(EntryTemplate.format(n=n))
