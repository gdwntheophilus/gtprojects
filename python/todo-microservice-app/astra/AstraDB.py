from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


class AstraDB():
    def __init__(self):
        cloud_config = {
          'secure_connect_bundle': './secure.zip'
        }
        auth_provider = PlainTextAuthProvider('eTvzhqmnlgvAHxaqPFTNCtXl', 'T2ucSkqqoknTQGwXgqnSWRqfK+59ZUxcbg+WWNEJJpjTGm8U.uORTH+RWm80zv3D06oYg+RR0xNQ0yPAOaUQC42._rrul4JsJTeRyF7Z9HhB_XG-Hi4.ohXd7TB1gMUv')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
    def getConnection(self):
        return self.session

AstraDBSession = AstraDB()
# row = session.execute("select release_version from system.local").one()
# if row:
#   print(row[0])
# else:
#   print("An error occurred.")