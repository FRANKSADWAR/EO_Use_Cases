import rasterio
from pystac_client import Client
from odc.stac import stac_load

address = 'https://explorer.digitalearth.africa/stac'
catalog = Client.open(address)  

product_name = 'rainfall_chirps_daily'
measurement_name = 'rainfall'
measurement_dtype = 'float32'
measurement_nodata = -9999
measurement_unit = 'mm'

config = {
    product_name :{
        "assets":{
            measurement_name: {
                "data_type" : measurement_dtype,
                "nodata": measurement_nodata,
                "unit": measurement_unit,
            }
        }
    }
}

def load_rainfall_data_from_chirps (lat, lng, start_date, end_date):
    """
    This function will return a dataset with rainfall values for the lat, lng 
    entered.
    """

    buffer_lat, buffer_lng = 0.02, 0.02  ## This is roughly a grid of 2km by 2km
    ## compute the bounding box
    xmin, xmax = (lng - buffer_lng, lng + buffer_lng)
    ymin, ymax = (lat - buffer_lat, lng -buffer_lat)

    # create the bounding box
    bbox = [xmin, ymin, xmax, ymax]

    ## create a datetime range
    timerange = f'{start_date}/{end_date}'

    # choose the ranfall_chirps_daily product
    products = ['rainfall_chirps_daily']

    ## create the query to get the data
    query = catalog.search(
        bbox = bbox,
        collections = products,
        datetime = timerange
    )

    items = list(query.items())

    print(f"--- Found: {len(items): d} datasets ---")

    crs = 'EPSG:4326'
    resolution = 0.05

    data = stac_load(
        items,
        crs = crs,
        resolution = resolution,
        chunks = {},
        groupby ="solar_day",
        stac_cfg = config, 
    )

    subset = data.sel(longitude = slice(bbox[0], bbox[2]), latitude = slice(bbox[1], bbox[3]))


    #load data into memory and mask no-data values in the xarray dataset
    with rasterio.Env(AWS_S3_ENDPOINT = 's3.af-south-1.amazonaws.com',AWS_NO_SIGN_REQUEST = 'YES'):
        loaded_data = subset.where(subset.rainfall != measurement_nodata).persist()

    return loaded_data    
