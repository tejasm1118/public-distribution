from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    v_id = models.CharField(max_length=10)
    v_address = models.CharField(max_length=200,null=False)
    v_description = models.CharField(max_length=300)
    v_phoneNum = models.CharField(max_length=10)


    def __str__(self):
        return self.name

class Unit(models.Model):
	u_name= models.CharField(max_length=100)
	u_address = models.CharField(max_length=300)
	u_contact = models.CharField(max_length=10)

	def __str__(self):
		return self.u_name


class Packaging(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    p_id = models.CharField(max_length=10)
    p_contact = models.CharField(max_length=10)
    p_UnitName=models.ForeignKey(Unit, related_name='unit_id', on_delete=models.CASCADE,)


    def __str__(self):
        return self.name


recieved_choices = [('Yes','Yes'),('No','No')]
class Family(models.Model):
	f_id = models.CharField(max_length=10,unique=True)
	f_recieve = models.CharField(max_length=10,choices=recieved_choices,default='No')
	f_total= models.IntegerField(null=True,default=0)

	def __str__(self):
		return self.f_id




item_choices = [('Rice','Rice'),('Wheat','Wheat'),('Sugar','Sugar')] 
quan_choices = [('1','1'),('2','2'),('4','4')]

class item(models.Model):
	i_name = models.CharField(max_length=20,choices=item_choices)
	i_quantity = models.IntegerField(choices=quan_choices)
	i_barcode = models.CharField(max_length=20,default=0)
	i_vendor=models.ForeignKey(Vendor, related_name='i_ven_id', on_delete=models.CASCADE,)
	i_pack=models.ForeignKey(Packaging, related_name='i_pack_id', on_delete=models.CASCADE,)
	i_fam=models.ForeignKey(Family, related_name='i_fam_id', on_delete=models.CASCADE,blank=True, null=True)

	def __str__(self):
		newname=i_fam.f_id + ' ' + i_name 
		return self.newname


class Customer(models.Model):
	c_aadhar = models.CharField(max_length=12,unique=True)
	c_name = models.CharField(max_length=100)
	c_dob = models.DateField()
	c_family = models.ForeignKey(Family, related_name='c_fam_id', on_delete=models.CASCADE,)


	def __str__(self):
		return self.c_name