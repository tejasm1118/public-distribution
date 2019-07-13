from django.shortcuts import render
from .models import Vendor,Packaging,Customer,item,Family
from django.shortcuts import redirect
from django.utils import timezone



def home(request):
	return render(request,'home.html')
	
	
def ven_login(request):
	if request.method == 'POST':
		v_name = request.POST['v_name']
		v_Id = request.POST['v_Id']
		v_password=request.POST['v_password']

		single_vendor = Vendor.objects.filter(v_id=v_Id).first()
		if single_vendor == None:
			msg="The vendor id is invalid..!"
			back='ven_login'
			return render(request,'error.html',{'msg':msg,'back':back})
			
		else:
			if single_vendor.password == v_password:
				return redirect('ven_Home',pk=v_Id)
			else:
				return render(request,'ven_login.html')
			

	return render(request,'ven_login.html')



def Pack_login(request):
	if request.method == 'POST':
		p_name = request.POST['p_name']
		p_Id = request.POST['p_Id']
		p_password=request.POST['p_password']

		
		
		single_packager= Packaging.objects.filter(p_id=p_Id).first()

		if single_packager == None:
			msg="The Packager id is invalid..!"
			back = "Pack_login"
			return render(request,'error.html',{'msg':msg,'back':back})

		else:
			if single_packager.password == p_password:
				return redirect('Pack_Home',pk=p_Id)
			else:
				return render(request,'Pack_login.html')
			
	return render(request,'Pack_login.html')



def ven_Home(request,pk):
	timezone.now().date()
	cur_date = timezone.now().day
	if request.method == 'POST':
		f_Id = request.POST['f_Id']
		c_adhar=request.POST['c_aadhar']

		if cur_date == 11:
			item.objects.all().delete()
			Family.objects.all().update(f_recieve='No')
			Family.objects.all().update(f_total=0)

		msg = ' '
		try:
			cus_c = Customer.objects.get(c_family=f_Id,c_aadhar=c_adhar)
		except:
			msg = 'Invalid Family Id or Aadhaar Number'
			return render(request,'cust_invalid.html',{'pk':pk,'msg':msg})
		try:
			fam_obj = Family.objects.get(f_id=f_Id,f_recieve='No')
		except:
			msg = 'You have already recieved the monthly comodities.'
			return render(request,'cust_invalid.html',{'pk':pk,'msg':msg})
		if cus_c == None and fam_obj == None:
			b = False

		else:
			b = True

		
		if b:
				
			count = 0
			cust_list = Customer.objects.filter(c_family=f_Id)
			for i in cust_list:
				count = count + 1

			if count > 5:
				count = 5

			rice_quan = count * 4
			wheat_quan = count 
			sugar_quan = 2 

			rice_price = rice_quan * 3
			wheat_price = wheat_quan * 3
			sugar_price = 2 * 10

			total_price = rice_price + wheat_price + sugar_price

			rice_list = item.objects.filter(i_name='Rice',i_vendor=pk,i_fam=None)

			i=0
			for j in rice_list:
				if i<count:
					j.i_fam_id=f_Id
					j.save()
					i=i+1

			wheat_list = item.objects.filter(i_name='Wheat',i_vendor=pk,i_fam=None)

			i=0
			for j in wheat_list:
				if i<count:
					j.i_fam_id=f_Id
					j.save()
					i=i+1

			sugar_list = item.objects.filter(i_name='Sugar',i_vendor=pk,i_fam=None)

			i=0
			for j in sugar_list:
				if i<1:
					j.i_fam_id=f_Id
					j.save()
					i=i+1
			Family.objects.filter(f_id=f_Id).update(f_total=total_price)
			Family.objects.filter(f_id=f_Id).update(f_recieve='Yes')
			return render(request,'cust_page.html',{'cust_list':cust_list,'rice_quan':rice_quan,'wheat_quan':wheat_quan,'sugar_quan':sugar_quan,'rice_price':rice_price,'wheat_price':wheat_price,'sugar_price':sugar_price,'total_price':total_price,'pk':pk})	
		else:
			return render(request,'ven_home.html',{'pk':pk})
		# else:
		# 	return render(request,'ven_home.html',{'pk':pk})
	return render(request,'ven_home.html',{'pk':pk})	


def Pack_Home(request,pk):
	i_list = item.objects.all()
	v_list = Vendor.objects.all()
	if request.method == 'POST':
		i_id = request.POST['i_id']
		i_unique = request.POST['i_unique']
		ven_id=request.POST['v_id']

		if i_id == "1":
			quan = 4
			naam = "Rice"
		elif i_id == "2":
			quan = 1
			naam = "Wheat"
		else:
			quan = 2
			naam = "Sugar"

		
		newitem = item.objects.create(
			i_name = naam,
			i_quantity = quan,
			i_vendor = Vendor.objects.get(v_id=ven_id),
			i_barcode=i_unique,
			i_pack = Packaging.objects.get(p_id=pk),
			i_fam = None
			)
		# back='Pack_login'
		return render(request,'Pack_home.html',{'i_list':i_list,'v_list':v_list,'pk':pk})
	return render(request,'Pack_home.html',{'i_list':i_list,'v_list':v_list,'pk':pk})


def request_return(request,pk):
	rice_list = item.objects.filter(i_fam=None,i_name='Rice')
	wheat_list = item.objects.filter(i_fam=None,i_name='Wheat')
	sugar_list = item.objects.filter(i_fam=None,i_name='Sugar')



	return render(request,'returning_page.html',{'rice_list':rice_list,'wheat_list':wheat_list,'sugar_list':sugar_list,'pk':pk})

def check_return(request,pk):
	rice_list = item.objects.filter(i_fam=None,i_name='Rice',i_vendor=pk)
	wheat_list = item.objects.filter(i_fam=None,i_name='Wheat',i_vendor=pk)
	sugar_list = item.objects.filter(i_fam=None,i_name='Sugar',i_vendor=pk)

	a = item.objects.filter(i_vendor=pk).count()
	b = item.objects.filter(i_vendor=pk,i_fam=None).count()
	r  = item.objects.filter(i_vendor=pk,i_name='Rice',i_fam=None).count()	
	w  = item.objects.filter(i_vendor=pk,i_name='Wheat',i_fam=None).count()	
	s  = item.objects.filter(i_vendor=pk,i_name='Sugar',i_fam=None).count()	

	rp = r *3
	wp = w * 3
	sp = s * 10

	t = rp + wp  + sp
	return render(request,'check_return.html',{'a':a,'b':b,'r':r,'w':w,'s':s,'rp':rp,'wp':wp,'sp':sp,'t':t,'rice_list':rice_list,'wheat_list':wheat_list,'sugar_list':sugar_list,'pk':pk})







