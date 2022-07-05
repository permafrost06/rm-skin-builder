# Rainmeter Skin Builder Script

## Instructions

1. Clone the project.
2. run `pip install -r requirements.txt`
3. Create a file with `.rms` extension. (See [`examples`](https://github.com/permafrost06/rm-skin-builder/tree/master/examples) folder for example scripts)
4. Write some RainMeterScript code in the file. (See [RainMeterScript](https://github.com/permafrost06/rm-skin-builder#rainmeterscript) Section for more information)

Your project is now ready to be transpiled.

#### Note: I keep writing transpile but in reality what I've written isn't technically a transpiler yet. A transpiler needs to tokenize the code then feed the tokens to a parser that will generate an AST then generate native code from that AST. What I've written essentially regex matches some patterns, then replaces those matches with generated code. The rest of the code is left untouched. It does not even have error checking. So, just be aware of that.

## Usage

`python builder.py [-h] [--watch] [--export-to-skins] inputFile outputFile`
`python builder.py [-h] [-w] [-e EXPORT_TO_SKINS] inputFile outputFile`
or use whatever python interpreter you choose e.g. `python3`

### Command line options:

```
RainMeterScript Transpiler

positional arguments:
  inputFile             input .rms file in folder "src"
  outputFile            output .ini file in folder "dist"

optional arguments:
  -h, --help            show this help message and exit
  -w, --watch           Turn watch mode on
  -e skin_name, --export-to-skins skin_name
                        Export to Rainmeter/Skins/skin_name folder
```

## Options

The `--watch` flag starts the script in watch mode and the skin file is transpiled on inputFile change.
The `--export-to-skins` flag copies the transpiled skin file to the default Rainmeter skins folder `%USERPROFILE%/Documents/Rainmeter/rmsdev/your_output_file` and activates the skin. If the skin it already activated, it's refreshed. To change the default path, change the [`path` variable in `builder.py`](https://github.com/permafrost06/rm-skin-builder/blob/master/builder.py#L23).

## RainMeterScript

The script works sort of like php. It is written alongside vanilla Rainmeter code. The RMS code is enclosed with two instances of `;@;`. For example: `;@;arr times = Fajr, Duhur, Asr, Maghrib, Isha;@;` creates an array `times` with items `Fajr`, `Duhur`, `Asr`, `Maghrib`, and `Isha`. See [`src/test.rms`](https://github.com/permafrost06/rm-skin-builder/blob/master/src/test.rms) for example.

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

The above loop will result in the following given that array `times` is the one from [the array example above](https://github.com/permafrost06/rm-skin-builder#arrays):

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
2. Make a ~~parser~~transpiler to ~~parse~~transpile aforementioned .rms files. ✅
3. Modify the script to build to `.rmskin` and/or skin with correct folder structure.
4. Reusable styles.
5. Add row/column placement option (similar to Bootstrap CSS).
6. Add common meter/measure presets.
7. Create a hack that changes the default `StringAlign` behaviour so that using the value "R" on X option of next meter places the two meters side by side. Abstract this away somehow.
8. Make the script installable via pip and make script globally available.
9. Fix the export functionality - export to custom skin folder instead of just `rmsdev`. ✅
10. Check if export folder is empty before export, prompt user.
11. Add project settings to file like webpack config but simpler.
12. Fix foreach loop in transpiler - change syntax to `foreach var in array` and add support for multiple array enumeration.
13. Add number array generation support - similar to range() in python to transpiler.
14. Add section templates support to transpiler.
