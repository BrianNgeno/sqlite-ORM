#!/usr/bin/python3

import sqlite3
CONNECT = sqlite3.connect('orm_test.db')
CURSOR = CONNECT.cursor()

class Car:
    all = []

    def __init__(self,model,y_o_m):
        print("car object initialized")
        self.model = model
        self.y_o_m = y_o_m
        self.add_to_all(self)
    
    @classmethod
    def add_to_all(cls,car):
        cls.all.append(car)
    
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE 
            IF NOT EXISTS cars(
            id INTEGER PRIMARY KEY,
            model TEXT,
            y_o_m INTEGER
        )"""
        CURSOR.execute(sql)

    def save(self):
        sql = """INSERT INTO cars (model,y_o_m) VALUES (?,?)"""
        CURSOR.execute(sql,(self.model,self.y_o_m))

    @classmethod
    def all_data(cls):
        sql = """SELECT * FROM cars"""
        all_items = CURSOR.execute(sql).fetchall()
        print(all_items)

    @classmethod
    def get_by_id(cls,id):
        sql = """SELECT * FROM cars WHERE id=? LIMIT 1"""
        car = CURSOR.execute(sql,(id,)).fetchone()
        print(car)


toyota = Car('supra',2020)
print(toyota)
toyota.save()
Car.get_by_id(7)

    
CONNECT.commit()
