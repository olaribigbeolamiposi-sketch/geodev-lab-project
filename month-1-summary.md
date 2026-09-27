# Month 1 Summary: Education Facility Proximity in Lagos Mainland

## My question

Which parts of Lagos Mainland lie within 1 km straight-line distance of an education facility recorded in my prepared OpenStreetMap dataset?

## Operation and why

I created 1,000 m buffers in QGIS to show areas close to mapped education facilities.

I used WGS 84 / UTM zone 31N (EPSG:32631), a projected CRS with metre units.

My prepared dataset contained 16 point features and 15 polygon features. I used Point on Surface to create one representative point for each polygon, then merged these with the existing points to produce 31 input records.

I ran Buffer with:
- Distance: 1,000 metres
- Segments: 25
- Dissolve: disabled

This produced one buffer per input record. I then dissolved a separate copy for the final map to remove internal overlapping boundaries. I retained the original buffer layer for checking.

The 1 km distance is an exploratory threshold, not an official education access standard. The 31 records do not necessarily represent 31 unique institutions.

## What I expected

Before running the operation, I expected:
- 31 buffer features, one per input record.
- Each buffer to extend approximately 1,000 m from its input point.
- Overlapping buffers where mapped facilities were close together.
- No empty or null geometries.

## What I got

The original buffer output contained 31 features, matching my expectation. Buffers overlapped around clusters of mapped facilities, while some areas inside Lagos Mainland remained outside the buffers.

The buffers extended beyond the LGA boundary because I did not clip them.

## Four checks

### 1. Look at the map

I inspected the buffers against the input points and LGA boundary. The buffers appeared centred on the points and consistently sized. Overlaps were visible around clusters of mapped facilities.

### 2. Check the row count

The merged input contained 31 records. The original buffer attribute table also contained 31 features, matching the expected count.

### 3. Verify one feature by hand

I measured from one input point to its buffer edge in QGIS. The distance was approximately 1,000 m, consistent with the buffer setting.

### 4. Look for empty geometry

I checked the original buffer layer using:

`is_empty($geometry) OR $geometry IS NULL`

The expression selected 0 features, indicating no empty or null geometries in that output.

## What surprised me

The striking result was how much the buffers overlapped around clusters of mapped facilities while gaps remained elsewhere inside the LGA. Having 31 mapped records did not produce an even spread of proximity across Lagos Mainland.

These gaps describe the prepared dataset. They do not prove that no education facilities exist in those areas.

## Result map

The map includes a title, legend, scale bar, north arrow, sources and a limitation note.

![Mapped education facilities and 1 km buffers in Lagos Mainland](lagos_mainland_education_1km.png)

## Limitations

- The buffers represent straight-line proximity, not walking distance or travel time.
- Polygon representative points are not verified facility entrances.
- OpenStreetMap coverage may be incomplete.
- Some records may represent parts of the same institution or require classification checks.
- Nearby facilities outside Lagos Mainland were not included.
- Proximity does not establish school capacity, admission eligibility or suitability.
- I have not calculated the percentage of land or population covered.

## Data I still need

- An authoritative, current education facility list to verify names, types, operating status and duplicates.
- Verified facility locations and entrances.
- Nearby facilities outside the LGA boundary.
- Walkable roads, paths, crossings and barriers for route-based access analysis.
- Population or school-age population data.
- Information on education levels, capacity and admissions.

## Sources

- OpenStreetMap contributors / HOT via HDX:
  https://data.humdata.org/dataset/hotosm_nga_education_facilities
- Nigeria administrative boundaries via HDX:
  https://data.humdata.org/dataset/cod-ab-nga
