import mysql

import models


class VehicleRepositoryMysql:
    def __init__(self):
        self.db = mysql.connector.connect(user="root", password="", database='sovelluskehykset_bad1')
        
    def get_all(self):
        with self.db.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM vehicles")
            vehicles = cur.fetchall()
            vehicles_list = []
            for v in vehicles:
                vehicles_list.append(models.Vehicle(v['id'], v['make'], v['model']))
            return vehicles_list