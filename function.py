import sqlite3
CONNECT = sqlite3.connect('test_database.db')
CURSOR = CONNECT.cursor()

class Car:
    all=[]
    year = 0
    MODELS = ['BMW', 'audi','toyota']
    def __init__(self,name,year,model):
        print("car initialized")
        if self.check_model(model):
            self.name = name
            self._speed = 0
            self.year = year
            self.model = model
            
    @classmethod
    def add_car_to_all(cls, car):
        cls.all.append(car)
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS cars(
            id INTEGER PRIMARY KEY,
            name TEXT,
            year TEXT,
            model TEXT
        )
        """
        CURSOR.execute(sql) 
    @classmethod
    def new_from_db(cls, row):
        car = cls(row[1], row[2])
        car.id = row[0]
        
    def save(self):
        sql="""
        INSERT INTO cars(name, year, model)
        VALUES (?,?,?)
        """
        CURSOR.execute(sql,(self.name,self.year,self.model))
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM cars").fetchone()[0]
        
    @classmethod
    def create(cls, name, year,model):
        car = Car(name, year,model)
        car.save()
        return car  
    @classmethod
    def all(cls):
        sql= """
        SELECT * 
        FROM cars
        """
        all = CURSOR.execute(sql).fetchall()   
    @classmethod
    def get_by_id(cls,id):
        sql= """ 
            SELECT *
            FROM cars
            WHERE id = ?
            LIMIT 1
         """
        car = CURSOR.execute(sql,(id,)).fetchone()
        return cls.new_from_db(car)
    @classmethod
    def check_model(cls, model):
        return model in cls.MODELS
    
    
    @classmethod
    def qeued_import_count(cls):
        cls.import_count+=1
    
    def check_manufacture_year(func):
        def wrapper(year):
            if 2008 >= int(year) <= 2023:
                func(year) 
            else:
                print("the cannot be imported")
        return wrapper   
    @check_manufacture_year
    def make_import(year):
        print("working on import duty")
    @check_manufacture_year
    def complete_taxes(year):
        print("working on taxes")
    @check_manufacture_year
    def register_client(year):
        print("transfer logbook details")    
    def get_speed(self):
        return self._speed
    def set_speed(self, speed):
        if(type(speed)in (int, float)) and (0 <= speed <= 80):
            print(f'set speed to {speed}')
            self._speed = speed
        else:
            print("speed is supposed to be  between 0 to 80")

   

    speed = property(get_speed, set_speed)

    
car = Car("Q7",'2023', 'audi')
car.save()
CONNECT.commit()