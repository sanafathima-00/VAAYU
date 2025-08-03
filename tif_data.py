import rasterio

# Replace this with the actual path to one of your .tif files
file_path = "data/3RIMG_01AUG2025_0545_L2G_AOD_V02R00_AOD.tif"

# Open the GeoTIFF file
with rasterio.open(file_path) as src:
    aod_data = src.read(1)  # Read the first band
    print("✅ File Loaded:", file_path)
    print("📏 Shape (rows x cols):", aod_data.shape)
    print("🗺️ CRS:", src.crs)
    print("🌐 Bounds:", src.bounds)
    print("📊 AOD Data Sample (first 5x5 pixels):")
    print(aod_data[:5, :5])
