import rasterio
import json

file_path = "data/3RIMG_01AUG2025_0545_L2G_AOD_V02R00_AOD.tif"
output_json = "data/valid_aod_points.json"

points = []

with rasterio.open(file_path) as src:
    data = src.read(1)
    transform = src.transform

    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            value = data[row, col]
            if value > 0:
                lon, lat = rasterio.transform.xy(transform, row, col)
                points.append({
                    "lat": round(lat, 3),
                    "lon": round(lon, 3),
                    "aod": round(float(value), 3)
                })

with open(output_json, "w") as f:
    json.dump(points, f, indent=2)

print(f"✅ Extracted {len(points)} valid AOD points to {output_json}")
