import os
import csv
set_images ={'.jpeg','.png','.jpg', '.gif'}
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        self.photo = self.photo_file_name
        self.type_file = os.path.splitext(self.photo)
        return self.type_file[1]



class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = 'car'
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.car_type = 'truck'
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)
        self.body_whl = body_whl
        self.body_length = float(0)
        self.body_width = float(0)
        self.body_height = float(0)
        self.list_whl = self.body_whl.split('x')
        self.body_width
        
        try:
            if len(self.list_whl) == 3:
                self.body_length = float(self.list_whl[0])
                self.body_width = float(self.list_whl[1])
                self.body_height = float(self.list_whl[2])
        except:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        self.volume = float(self.body_length*self.body_width*self.body_height)
        return self.volume

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = 'spec_machine'
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] == 'car':
                        brand = str(row[1])
                        passenger_seats_count = int(row[2])
                        photo_file_name = str(row[3]) 
                        carrying = float(row[5])
                        if brand !='' and os.path.splitext(photo_file_name)[-1] in set_images:
                            car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                if row[0] == 'truck':
                        brand = str(row[1])
                        photo_file_name = str(row[3]) 
                        carrying = float(row[5])
                        body_whl = str(row[4])
                        if brand !='' and os.path.splitext(photo_file_name)[-1] in set_images:
                            car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                if row[0] == 'spec_machine':
                        brand = str(row[1])
                        photo_file_name = str(row[3]) 
                        carrying = float(row[5])
                        extra = str(row[6])
                        if brand !='' and os.path.splitext(photo_file_name)[-1] in set_images and extra != '':
                            car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
            except Exception:
                print('wrong')
    return car_list
