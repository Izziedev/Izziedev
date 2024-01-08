from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Apartment(models.Model):
    """Apartments model"""
    apartment_name = models.CharField(max_length=256,null=False,default='')
    location =models.CharField(max_length=256,null=False,default='')
    number_of_rooms = models.PositiveIntegerField(default=0,null=False)
    address=models.CharField(max_length=256,null=True)
    description =models.TextField(max_length=600,null=False,default='')

    def __str__(self):
        return self.name
    def save_apartment(self):
        return self.save()
    
    @classmethod
    def delete_item(cls,id,self):
        query = Apartment.objects.get(cls.id==id)
        for item in query:
            self.delete(item)

    def get_all():
        query = Apartment.objects.all()
        return query
    
    @classmethod
    def fetch_item(cls,itemname):
        query= cls.objects.filter(apartment_name=itemname)
        return query
    
class Room(models.Model):
    '''Rooms model'''
    name= models.CharField(max_length=10,null=False,default='')
    room_number=models.CharField(max_length=20,default='room number',null=False)
    room_price =models.IntegerField(default=0,null=False)
    room_description = models.TextField(max_length=600,null=False,default='')
    apartment = models.ForeignKey('Apartment',on_delete = models.CASCADE)

    def __str__ (self):
        return self.name
    
    def save_room(self):
        return self.save()
    
    def fetch_all():
        all_rooms = Room.objects.all().order_by('room_number')
        return all_rooms
    
    @classmethod
    def delete_room(cls,id,self):
        query = Room.objects.filter(id==id)
        for item in query:
            self.item.delete()
            return item
class RoomInventory(models.Model):
    item_name =models.CharField(max_length=256,null=False, default='Item name')
    type= models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0, null= False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    imageholder= models.FileField(upload_to='uploads/%Y%M%D%H%m%')

    def __str__(self):
        return  self.item_name
    
    
    def add_item(cls):
        cls.save()
        return cls.item_name

    def fetch_all(room):
        query = RoomInventory.objects.all(room=room)
        for item in query:
            return item
        
    def get_item(self,id):
        query = RoomInventory.objects.get(id=id)
        return query
    
    def add_inventory(self):
        pass

    @classmethod
    def delete(self,id):
        obj= RoomInventory.objects.filter(id=id)
        obj.delete()
        return self.item_name