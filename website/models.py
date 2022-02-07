from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# CREATE A TABLE TO STORE PICTURE OF PLACES & HEALTH ORGANISATIONS

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))
    passwordOri = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    name = db.Column(db.String(150))
    ic = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(100))
    type = db.Column(db.String(10))
    status = db.Column(db.String(10))
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    # Foreign key dkt child table.  KAT SINI PARENT TABLE NI, tambah db.relationship
    notes = db.relationship('Note')
    useradmin = db.relationship('UserAdmin')
    usercontact = db.relationship('UserContact')
    userho = db.relationship('UserHO')
    uservehicle = db.relationship('UserVehicle')
    #userplacepreferences = db.relationship('UserPlacePreferences')

class Admin(db.Model, UserMixin):
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_email = db.Column(db.String(150), unique=True)
    admin_password = db.Column(db.String(150))
    admin_gender = db.Column(db.String(10))
    admin_name = db.Column(db.String(150))
    admin_ic = db.Column(db.String(20))
    admin_phoneNumber = db.Column(db.String(20))
    admin_address = db.Column(db.String(100))
    admin_type = db.Column(db.String(10))
    admin_status = db.Column(db.String(10))
    # Foreign key dkt child table.  KAT SINI PARENT TABLE NI, tambah db.relationship
    adminplace = db.relationship('AdminPlace')
    adminvehicle = db.relationship('AdminVehicle')
    adminho = db.relationship('AdminHO')
    admincontact = db.relationship('AdminContact')
    useradmin = db.relationship('UserAdmin')

#class Preferences(db.Model):
#    preference_id = db.Column(db.Integer, primary_key=True)
#    preference_name = db.Column(db.String(30))
    # Foreign key dkt child table.  KAT SINI PARENT TABLE NI, tambah db.relationship
#    userplace = db.relationship('UserPlace')

class Place(db.Model):
    place_id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(50))
    place_address = db.Column(db.String(100))
    place_phoneNum = db.Column(db.String(13))
    place_email = db.Column(db.String(50))
    #place_pic1 = db.BLOB()
    #place_pic2 = db.BLOB()
    #place_pic3 = db.BLOB()
    place_description = db.Column(db.String(500))
    place_fee = db.Column(db.String(13))
    place_rating = db.Column(db.Integer)
    place_numrater = db.Column(db.Integer)
    place_website = db.Column(db.String(50))
    place_keyword = db.Column(db.String(50))	
    place_attractions = db.Column(db.String(50))
    #place_type = db.Column(db.String(50))
    place_operatingHour = db.Column(db.String(50))
    image1_img = db.Column(db.Text, unique=True, nullable=False)
    #image2_img = db.Column(db.Text, unique=True, nullable=True)
    #image3_img = db.Column(db.Text, unique=True, nullable=True)
    # Foreign key dkt child table.  KAT SINI PARENT TABLE NI, tambah db.relationship
    userplace = db.relationship('UserPlace')
    adminplace = db.relationship('AdminPlace')

class Restaurant(db.Model):
    rest_id = db.Column(db.Integer, primary_key=True)
    rest_name = db.Column(db.String(50))
    rest_phonenum = db.Column(db.String(50))
    rest_website = db.Column(db.String(50))
    rest_address = db.Column(db.String(50))
    rest_email = db.Column(db.String(50))
    rest_desc = db.Column(db.String(500))
    rest_rating = db.Column(db.Integer)
    rest_num_rater = db.Column(db.Integer)
    rest_keyword = db.Column(db.String(50))
    rest_attractions = db.Column(db.String(50))
    rest_operatingHour = db.Column(db.String(50))
    image1_img = db.Column(db.Text, unique=True, nullable=False)
    image2_img = db.Column(db.Text, unique=True, nullable=True)
    image3_img = db.Column(db.Text, unique=True, nullable=True)
    #userrestaurant = db.relationship('UserRestaurant')           #cam userplace atas
    #adminrestaurant = db.relationship('AdminRestaurant')         #cam adminplace atas

class Vehicle(db.Model):
    vehicle_id = db.Column(db.Integer, primary_key=True)
    vehicle_model = db.Column(db.String(30))
    vehicle_brand = db.Column(db.String(30))
    vehicle_plateNum = db.Column(db.String(10))
    vehicle_seatNum = db.Column(db.Integer)
    vehicle_amt = db.Column(db.String(10))
    vehicle_yyProduction = db.Column(db.String(5))
    vehicle_type = db.Column(db.String(20))
    vehicle_medicalEquipment = db.Column(db.String(50))
    vehicle_rating = db.Column(db.Integer)
    vehicle_pic = db.BLOB()
    # Foreign key dkt child table.  KAT SINI PARENT TABLE NI, tambah db.relationship
    uservehicle = db.relationship('UserVehicle')
    adminvehicle = db.relationship('AdminVehicle')

class Ho(db.Model):
    ho_id = db.Column(db.Integer, primary_key=True)
    ho_name = db.Column(db.String(30))
    ho_phoneNum = db.Column(db.String(13))
    ho_address = db.Column(db.String(50))
    ho_email = db.Column(db.String(50))
    ho_operatingHour = db.Column(db.String(50))
    image1_img = db.Column(db.Text, unique=True, nullable=False)
    #ho_rating = db.Column(db.Integer)
    ho_website = db.Column(db.String(50))
    # Foreign key dkt child table.  KAT SINI PARENT TABLE NI, tambah db.relationship
    userho = db.relationship('UserHO')
    adminho = db.relationship('AdminHO')

class Contact(db.Model, UserMixin):
    contact_id = db.Column(db.Integer, primary_key=True)
    contact_phoneNumber = db.Column(db.String(13))
    contact_email = db.Column(db.String(50))
    contact_HQaddress = db.Column(db.String(100))
    # Foreign key dkt child table.  KAT SINI PARENT TABLE NI, tambah db.relationship
    usercontact = db.relationship('UserContact')
    admincontact = db.relationship('AdminContact')




class UserAdmin(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), primary_key=True)

class UserContact(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.contact_id'), primary_key=True)

class UserHO(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    ho_id = db.Column(db.Integer, db.ForeignKey('ho.ho_id'), primary_key=True)

class UserVehicle(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'), primary_key=True)



#Preference table - bridge between User and Place
class UserPlace(db.Model):
    userplace_id = db.Column(db.Integer, primary_key=True)
    userplace_name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.place_id'), primary_key=True)

#Preference table - bridge between User and Place
class UserRestaurant(db.Model):
    userrestaurant_id = db.Column(db.Integer, primary_key=True)
    userrestaurant_name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.rest_id'), primary_key=True)

class AdminPlace(db.Model):
    place_id = db.Column(db.Integer, db.ForeignKey('place.place_id'), primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), primary_key=True)

class AdminRestaurant(db.Model):
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.rest_id'), primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), primary_key=True)
    
class AdminVehicle(db.Model):
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'), primary_key=True)

class AdminHO(db.Model):
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), primary_key=True)
    ho_id = db.Column(db.Integer, db.ForeignKey('ho.ho_id'), primary_key=True)

class AdminContact(db.Model):
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.contact_id'), primary_key=True)

class imageplace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)


class Rating(db.Model):
    rate_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer,nullable=False)
    rate_date = db.Column(db.Text, nullable=False)
    rate_type = db.Column(db.Text, nullable=False)
    review = db.Column(db.Text, nullable=False)
    id_attraction = db.Column(db.Integer, nullable=False)