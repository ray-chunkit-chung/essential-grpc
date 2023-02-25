import os
import json
import route_guide_pb2

PWD = os.path.abspath(os.path.dirname(__file__))

def read_route_guide_database():
    """Reads the route guide database.
    Common resources used in the gRPC route guide example.

    Returns:
      The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    feature_list = []
    db_path = os.path.join(PWD, 'route_guide_db.json')
    with open(db_path, 'r') as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            feature = route_guide_pb2.Feature(
                name=item["name"],
                location=route_guide_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"]))
            feature_list.append(feature)
    return feature_list
