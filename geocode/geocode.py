import boto3
import json

## UPDATE THESE VALES WITH VALUES FROM YOUR ENVIRONMENT
INDEX_NAME = "acb-index"
INPUT_FILE_NAME = "acb_country_list.csv"
##########

OUTPUT_FILE_NAME = "../data.geojson"
geo_client = boto3.client("location")


def make_geojson(address, coordinates, count):
    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": coordinates},
        "properties": {"address": address, "count": count},
    }


with open(INPUT_FILE_NAME, "r") as country_list:
    list_of_addresses = country_list.readlines()

# Strip whitespace
list_of_addresses = [item.strip() for item in list_of_addresses]

geocode_cache = {}
for i, address in enumerate(list_of_addresses):
    try:
        cache_result = geocode_cache.get(address)
        if not cache_result:
            print(f"Geocoding {address}...")
            search_result = geo_client.search_place_index_for_text(
                IndexName=INDEX_NAME, MaxResults=1, Text=address
            ).get("Results", [None])[0]
            if not search_result:
                print(f"No result found for {address}")
                continue

            cache_result = [search_result["Place"]["Geometry"]["Point"], 0]
            geocode_cache[address] = cache_result

        geocode_cache[address][1] += 1
    except ValueError as e:
        print(e)
        continue

geojson_list = [
    make_geojson(key, value[0], value[1]) for key, value in geocode_cache.items()
]

with open(OUTPUT_FILE_NAME, "w") as output_file:
    output_file.write(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": geojson_list,
            }
        )
    )
