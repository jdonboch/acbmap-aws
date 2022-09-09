# AWS Community Builder Map

AWS Community Builder map implemented via AWS Location Services

## Prerequisites

- Need an AWS Account and a user/role with admin privileges
- Python 3.8 for geocoding script
- A modern browser to display the map
- A newline separated file contains a list of locations to geocode

### Creating Cognito and Location resources

1. Create a Cognito Identity Pool for anonymous access and getting credentials that support read-only access for retrieving tiles.
   - [Allowing unauthenticated guest access to your
     application using Amazon Cognito](https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html)
2. Create an Amazon Location Service Map resource to support retrieving tiles.
   - [Creating a Map Resource](https://docs.aws.amazon.com/location/latest/developerguide/maps-prerequisites.html#create-map-resource)
3. Create an Amazon Location Service Place Index resource to support geocoding.
   - [Creating a Place Index Resource](https://docs.aws.amazon.com/location/latest/developerguide/places-prerequisites.html#create-place-index-resource)

## Geocoding script

To run the geocoding script, ensure you have the requirements installed.

```
$ cd geocode
$ pip install -r requirements.txt
```

Open the `geocode.py` file and update the `INDEX_NAME` and `INPUT_FILE_NAME` with the values of your input file (newline separated list of locations) and the AWS Location Services Place Index name that you created as part of the Prerequisites.

Since the inputs are hardcoded at the top of the script, simply run the script with python and it will generate the `data.geojson` needed by the map page.

```
$ python geocode.py
```

## Static Map

Note the Cognito Identity Pool ID and the AWS Location Service Map name that you created as part of the Prerequisites. Open the `index.html` and find the lines contains `<REPLACE ` and update the value of the two fields with the Cognito Identity Pool ID and the map name.

## Opening the map

Assuming you have run the geocoding script (i.e. the `data.geojson` file is present in the root directory) and you have updated the `index.html` with your resource names: you should be able to open the `index.html` file with a modern browser and see the markers displayed on the map :)

## Hosted version

This static map is hosted at the following location and currently displays the country locations of the 2300+ AWS Community Builders as of September 2022.

https://acbmap.humbleg.com/aws/
