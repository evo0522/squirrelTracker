# squirrelTracker

## Introduction
In this project, we implemented a django web applicaiton to visualize a dataset of roughly 3000+ squirrel sightings at New York central park. It has 8 features: 
1. Importing dataset
2. Exporting dataset 
3. Viewing the location of all the squirrel sightings
4. Listing all squirrel sightings in a page
5. Updating existing squirrel sighting 
6. Adding new squirel sighting 
7. Deleting all the sightings that are related to a specifc squirrel 
8. An analytics about the squirrel dataset.

## Data source
[Squirrel data 2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

## Webapp Link
The deployed webapp can be found here: [link](https://uplifted-valor-252914.appspot.com/sightings/)

## Management & Functional Commands
Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.

```
python manage.py import_squirrel_data ./data.csv
```
Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.
```
python manage.py export_squirrel_data ./result.csv
```
Create geojson: A command that reads in the entire dataset and export an geojson formated file to create the squirrel sighting map. Run this command under utilities directory: 
```
python create_geojson.py 
```
⚠️Notes: For the demo purpose, currently the map page depicts a portion of the squirrel sightings (by reading in data2.csv). We can simply change the input file to the full sightings list (data.csv) to generate a complete map of 3000+ squirrel sightings. 
(at line #5 in /utilities/create_geojson.py)

## APIs 
### Map
/Map will show a map that displays the location of the squirrel sightings on an

### Full list of squirrel sightings
[/sightings] (https://uplifted-valor-252914.appspot.com/sightings/) lists all squirrel sightings with links to edit and add sightings

### Sighting Edit page 
[/sightings/<unique-squirrel-id>](https://uplifted-valor-252914.appspot.com/sightings/37F-PM-1014-03/) allows user to update a particular sighting

### Adding sighting 
[/sightings/add](https://uplifted-valor-252914.appspot.com/sightings/add/) allows user to create a new sighting

### Deleting sightings
/sightings/<unique-squirrel-id> allows user to delete all sightings related to a specific squirrel. However, since delete does does not require a front-end page to illustrate it. We simply just implemented as a method, which can be triggered via Postman. 
```
⚠️ Method: DELETE ⚠️
```
### General stats
[/sightings/stats](https://uplifted-valor-252914.appspot.com/sightings/stats/) shows some particular stats about this dataset, including: 
* Statistics about estimated center of all squirrel sightings coordinates
* Statistics about the time when squirrel are sighted
* Statistics about the colors of the sighted squirrels
* Statistics about the age group of the sighted squirrels
* Statistics about the kinetic status the sighted squirrels


## Contributors:
Group Name: [TODO]

Section: [TODO]

Contributors: Yihan Wang, Jiayun Liu

UNIs: [yw3407], [jl5528]
