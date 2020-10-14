# Experimental Rainmeter Skin Builder Script
## Skin build process
The skin consists of two files: "measures.inc" where all the measures reside and "skin.ini" where the rainmeter section, styles, variables and meters are.

To build the "measures.inc" file, run the measures.py script

To build the "skin.ini" file, run the meters.py script

## ToDos
1. Move the huge strings to another file. New extension I'm thinking .rms (RainMeterScript).
1. Make a parser to parse aforementioned .rms files.
1. Modify the script to build to .rmskin and/or skin with correct folder structure.
1. Reusable styles.
1. Add row/column placement option (similar to Bootstrap CSS).
1. Add common meter/measure presets.
1. Create a hack that changes the default ```StringAlign``` behaviour so that using the value "R" on X option of next meter places the two meters side by side. Abstract this away somehow.
