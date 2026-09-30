# SPATIAL_REFERENCE_STANDARD_V1

Status: ACTIVE_REFERENCE_STANDARD
Authority: USER_REQUEST_2026-09-29_COORDINATES_AND_DIMENSIONS
Purpose: canonical method for documenting world coordinates, dimensions, orientation, uncertainty, and spatial validity
Live-game clock effect: NONE

## 1. Principle

Every persistent location used by history, scenario generation, ecology, institutions, battles, portals, or Academy scenes should be spatially describable.

Spatial documentation must answer:
- where is it;
- relative to what frame;
- how large is it;
- what direction is it oriented;
- what occupies it;
- when is the spatial record valid;
- how certain are the measurements.

Coordinates are not flavor text. They are continuity data.

## 2. Units

Canonical unit system: metric.

- distance: meter (m)
- large distance: kilometer (km)
- area: square meter / square kilometer
- volume: cubic meter
- elevation/depth: meter
- orientation: degrees clockwise from true north where a planetary north exists
- portal aperture: width × height × depth/thickness in meters
- room/building dimensions: length × width × clear height

Do not mix feet, miles, or arbitrary tiles into canonical measurements without storing the metric conversion.

## 3. Spatial frames

### FRAME_EARTH_GEODETIC_001
Use for Earth locations when geography is locked.

Fields:
- latitude_deg
- longitude_deg
- elevation_m
- coordinate_epoch
- uncertainty_radius_m

### FRAME_PLANETARY_GEODETIC_*
Use for other approximately spherical worlds after their datum is established.

Required:
- world/body ID
- latitude
- longitude
- elevation/depth relative to local datum
- datum definition
- epoch

### FRAME_REGION_CARTESIAN_*
Use for regional maps.

Axes:
- X = east
- Y = vertical/up
- Z = north

Origin:
- explicitly defined geodetic/world anchor

Unit:
- meters unless region scale explicitly declares kilometers

### FRAME_SITE_LOCAL_*
Use for campuses, bases, settlements, ruins, laboratories, battlefields, caves, and neighborhoods.

Axes:
- X = local east/right
- Y = vertical/up
- Z = local north/forward

A site-local frame must link to a parent region/world frame.

### FRAME_BUILDING_LOCAL_*
Origin:
- southwest-lower structural reference point unless a file states another anchor.

### FRAME_PORTAL_ENDPOINT_*
A portal always stores two endpoints separately:
- source frame + coordinate
- destination frame + coordinate

Never treat one portal coordinate as sufficient for both sides.

## 4. Dimension standard

Rectangular spaces:
LENGTH × WIDTH × HEIGHT

Irregular spaces:
- bounding box;
- footprint area;
- maximum vertical extent;
- polygon or radius where needed.

Regions:
- north-south span;
- east-west span;
- area;
- elevation/depth range.

Settlements:
- inhabited footprint;
- administrative footprint;
- defensive/perimeter footprint where different.

Buildings:
- footprint;
- total height;
- floors;
- floor-to-floor height;
- major internal zones.

Rooms:
- clear internal dimensions;
- doorway dimensions;
- ceiling height;
- important fixed obstacles.

Creature territories:
- typical home-range radius/area;
- seasonal range;
- nesting radius;
- migration corridor width.

Battlefields:
- operational rectangle/polygon;
- major elevation changes;
- approach routes;
- cover density;
- chokepoints.

## 5. Measurement confidence

### SPATIAL_EXACT_SURVEY
Measured or authoritatively fixed.

### SPATIAL_AUTHORITATIVE_APPROX
Author-defined approximation suitable for scenario use; minor revision allowed.

### SPATIAL_HISTORICAL_ESTIMATE
Reconstructed from incomplete historical evidence.

### SPATIAL_PUBLIC_APPROX
What public maps claim; may differ from TRUE coordinates.

### SPATIAL_CLASSIFIED
Exact coordinates exist but are not public.

### SPATIAL_UNKNOWN
Not yet defined.

## 6. Temporal validity

Every coordinate/dimension record must include:
- valid_from
- valid_to or PRESENT
- change_reason if superseded

A city, habitat, coastline, portal site, or battlefield may change over time.

Do not use a 2670 city footprint for a 2473 scene without checking the historical version.

## 7. Vertical convention

Y/altitude positive = upward.
Depth may be stored as negative altitude or a separate depth field, but the convention must be explicit.

Underground structures require:
- surface anchor elevation;
- floor elevation;
- depth below surface.

## 8. Orientation

For structures:
- bearing_deg indicates the long-axis direction clockwise from true north.
- local plans may use north_arrow_deg if the drawing is rotated.

For creatures:
- facing is runtime state and is not part of permanent geographic coordinates unless recording a specific event.

## 9. Spatial hierarchy

WORLD
-> CONTINENT/OCEAN
-> REGION
-> SETTLEMENT/WILDERNESS_ZONE
-> DISTRICT/SECTOR
-> SITE/CAMPUS/BASE
-> BUILDING/STRUCTURE
-> FLOOR/LEVEL
-> ROOM/ZONE
-> POINT/OBJECT

Every child record should reference its parent spatial ID.

## 10. Scenario selection requirement

A scenario candidate must pass:
YEAR + WORLD + REGION + SITE + DIMENSIONS + ACCESS + BIOME + THREAT compatibility.

For a creature encounter, the space must physically support:
- body size;
- movement;
- nesting behavior;
- group size;
- escape routes;
- environmental requirements.

A 12 m long creature cannot be casually placed inside a 3 m corridor unless the scene explicitly explains structural destruction, juvenile size, or another valid reason.

## 11. Portal spatial rule

Each portal record must include:
- aperture dimensions;
- safe transit envelope;
- minimum clearance;
- source approach area;
- destination approach area;
- stability zone radius;
- exclusion radius;
- orientation relative to local gravity;
- maximum cargo dimensions if regulated.

## 12. Academy spatial rule

When Academy geography is eventually fixed, document:
- campus polygon;
- perimeter length;
- public/civilian zone;
- secured zone;
- dormitory blocks;
- classrooms;
- training grounds;
- medical facilities;
- beast/portal training zones;
- emergency routes;
- underground/service spaces;
- gate dimensions;
- building interiors.

Do not infer Jack's dorm or protagonist-specific route before canon establishes it.

## 13. Story integration

History chapters should not dump coordinates into prose unless relevant.

Instead:
- narrative chapter names the place naturally;
- technical cross-link points to spatial registry;
- spatial file stores coordinates/dimensions.

This keeps the book readable while preserving exact world geometry.

## 14. Anti-drift

- Never invent exact coordinates for a previously established location without checking its spatial record.
- Never move a fixed site silently.
- Never resize a room/building merely to make an encounter fit.
- Record renovations, destruction, expansion, terrain change, and portal drift as temporal spatial versions.
- Keep PROTAGONIST_MYSTERY locations sealed where necessary.
