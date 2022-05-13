# Rainmeter Skin Builder Script

## Instructions

1. Clone the project.
2. run `pip install -r requirements.txt`
3. Create a folder `src` in project root.
4. Create a file with `.rms` extension. (An example file is provided)
5. Write some RainMeterScript code in the file. (See ## RainMeterScript Section for more information)

Your project is now ready to be transpiled.

## Usage

`python builder.py [-h] [--watch] [--export-to-skins] inputFile outputFile`
or use whatever python interpreter you choose e.g. `python3`
`inputFile` should be only the filename in folder `src`.
Incorrect: `python builder.py src/test.rms test.ini` ❌
Correct: `python builder.py test.rms test.ini` ✅
The output file will be saved in `dist` directory.

## Options

The `--watch` flag starts the script in watch mode and the skin file is transpiled on inputFile change.
The `--export-to-skins` flag copies the transpiled skin file to the default Rainmeter skins folder `%USERPROFILE%/Documents/Rainmeter` and activates the skin. If the skin it already activated, it's refreshed. To change the default path, change the `path` variable in `builder.py`.

## RainMeterScript

The script works sort of like php. The code is enclosed with two instances of `;@;`. For example: `;@;arr times = Fajr, Duhur, Asr, Maghrib, Isha;@;` creates an array `times` with items `Fajr`, `Duhur`, `Asr`, `Maghrib`, and `Isha`.

Right now, only arrays can be created and loops can be used to iterate over the arrays.

### arrays

The array initialization syntax is as follows:
`;@;arr array_name = array_item1, array_item2, array_item3, ..., array_itemN;@;`
Example: `;@;arr times = Fajr, Duhur, Asr, Maghrib, Isha;@;` will create an array `times` with items `Fajr`, `Duhur`, `Asr`, `Maghrib`, and `Isha`.

All items in the array are strings. Therefore, `1, 2, 3` will not be parsed as ints `1`, `2`, and `3` but as strings `"1"`, `"2"`, and `"3"`. This does not have any implications right now as numbers and strings are represented the same way in Rainmeter and you can't do arithmetic using RainMeterScript yet.

### loops

Only foreach loop is available right now. The syntax is as follows:

```
;@;loop array_name
[{item}Measure]
Measure=WebParser
URL=[MainParseMeasure]
StringIndex={idx}
;@;
```

`array_name` is the array that will be looped over. The items in the array can be accessed using `{item}` and the index using `{idx}`. Note that indices are 1-indexed rather than 0-indexed following Rainmeter style.
Example:

```
;@;loop times
[{item}Measure]
Measure=WebParser
URL=[MainParseMeasure]
StringIndex={idx}
;@;
```

The above loop will result in the following given that array `times` is the one from the array example above:

```
[FajrMeasure]
Measure=WebParser
URL=[MainParseMeasure]
StringIndex=1
[DuhurMeasure]
Measure=WebParser
URL=[MainParseMeasure]
StringIndex=3
[AsrMeasure]
Measure=WebParser
URL=[MainParseMeasure]
StringIndex=4
[MaghribMeasure]
Measure=WebParser
URL=[MainParseMeasure]
StringIndex=6
[IshaMeasure]
Measure=WebParser
URL=[MainParseMeasure]
StringIndex=7
```

## ToDos

1. Move the huge strings to another file. New extension I'm thinking .rms (RainMeterScript). ✅
1. Make a ~~parser~~transpiler to ~~parse~~transpile aforementioned .rms files. ✅
1. Modify the script to build to `.rmskin` and/or skin with correct folder structure.
1. Reusable styles.
1. Add row/column placement option (similar to Bootstrap CSS).
1. Add common meter/measure presets.
1. Create a hack that changes the default `StringAlign` behaviour so that using the value "R" on X option of next meter places the two meters side by side. Abstract this away somehow.
1. Make the script installable via pip and make script globally available.
