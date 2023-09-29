# Earth Observatiion  Use Cases
This reposotory explores the applications in Earth Observation using open datasets. Specifically, the use of open-data cubes using the STAC standard.
DEA (Digital Earth Africa) datasets are being here, to explore agricultural use cases.

odc-stac allows download of datasets from Digital Earth Africa. It is a set of tools that converts STAC (Spatial Temporal Assets Catalog) metadata to the Open Data Cube (ODC) data model.

odc-stac allows loading STAC items into xarray.datasets, and process them locally or distribute data loading and computation with Dask.

## Analysis of rainfall and NDVI, EVI,  for a field in Western Kenya
In this use case, we want to monitor the crop health in a field throughout a season. This will be accompanied by the rainfall values through that season.
From this, we can be able to evaluate the correlation between rainfall and vegation indices such as NDVI.
Using Sentinel-2 data, the reflectance values are obtained in an xarray dataset, from which band dimensions are used to compute the vegetation indices.

### Cloud-masking routine
Clouds are a major obstacle when handling optical remote sensing data from satellites. This is because optical remote sensing relies on the visible range of the electromagnetic spectrum which is oftlenly reflected back by particles in the atmosphere, giving clouds their distict colors. 

Several algorithms exists, some taking a more disruptive approach towards cloud detection. Sentinel-2 data from ESA comes with a SCL cloud mask band which can be used to mask the clouds.
Howerver, this mask also has some limitations. Instead, the S2Cloudless mask has proven to have better results and has been used as an approach for masking out clouds.
The discussin and approach used to obtain a cloud mask is better left for another repository.

### Significance & Differences between vegetaion indices 

**NDVI** : Normalized Difference Vegetation Index
**EVI** : Enhanced Vegatation Index 
**NDMI**: Normalized Difference Moisture Index

