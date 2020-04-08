def createFeature(id_, type_, geom, tags):
    feature = {
        "id": None if id_ is None else id_,
        "type": type_,
        "geometry": geom,
        "tags": tags,
        "minX": float('inf'),
        "minY": float('inf'),
        "maxX": float('-inf'),
        "maxY": float('-inf')
    }

    if type_ == 'Point' or type_ == 'MultiPoint' or type_ == 'LineString':
        calcLineBBox(feature, geom)
    elif type_ == 'Polygon':
        # the outer ring(ie[0]) contains all inner rings
        calcLineBBox(feature, geom[0])
    elif type_ == 'MultiLineString':
        for line in geom:
            calcLineBBox(feature, line)
    elif type_ == 'MultiPolygon':
        for polygon in geom:
            # the outer ring(ie[0]) contains all inner rings
            calcLineBBox(feature, polygon[0])
    return feature


def calcLineBBox(feature, geom):
    for i in range(0, len(geom), 3):
        feature['minX'] = min(feature.get('minX'), geom[i])
        feature['minY'] = min(feature.get('minY'), geom[i + 1])
        feature['maxX'] = max(feature.get('maxX'), geom[i])
        feature['maxY'] = max(feature.get('maxY'), geom[i + 1])


class Slice(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.start = 0.
        self.end = 0.
        self.size = 0.
