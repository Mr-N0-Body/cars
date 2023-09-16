#library importing 
import requests
from bs4 import BeautifulSoup
import os
import urllib.request

#some functions 
o_path = os.getcwd()
#helpful Functions
def aff(T):
	for i in range(0,len(T)):
		print(T[i])

#variables
marq_links = []
marq_modl_links = []
name_marq_modl_links = []
x1 = []
f_marq_links = open("cars_marques_links.txt","w+")

#starting requests
f_url = "https://www.moteur.ma/fr/neuf/fiche-technique-prix?marque=0&modele=0"
result = requests.get(f_url)
print(result)
src = result.content
soup = BeautifulSoup(src,"html.parser")

#scarping marques Links
gr_links = soup.find_all("div",{"class":"col-md-12 col-sm-3"})
for x in range(0,len(gr_links)):
	x1.append(gr_links[x].find('a'))
	o = x1[x].attrs['href']
	#print(o)
	f_marq_links.write(f"{o}\n")
	marq_links.append(o)
f_marq_links.close()
#aff(marq_links)
# HEre we have a list countain 


L_link_model =  []
L_name_model = []
L_pack = []
L_nm_pack = []
L_img_link = []

#le'ts start up 
db = []
for x in range(0,len(marq_links)):
	N_fr_link = marq_links[x][51:-1]
	os.chdir(f"{o_path}")
	os.system(f"mkdir {N_fr_link}")
	os.chdir(f"{o_path}/{N_fr_link}")
	f_link_models = open(f"{N_fr_link}_links.txt","w+")
	f_models_names = open(f"{N_fr_link}_model.txt","w+")
	res = requests.get(marq_links[x])
	print(res)
	soup = BeautifulSoup(res.content,"html.parser")
	db = soup.find_all("div",{"class":"title_mark_model"})
	for x in range(0,len(db)):
		link_models = db[x].find('a').attrs['href']
		name_models = db[x].text.replace('\n','').replace('\t','').replace('\r','').replace(' ','_')
		f_link_models.write(f"{link_models}\n")
		f_models_names.write(f"{name_models}")
		L_link_model.append(link_models)
		L_name_model.append(name_models)
	f_link_models.close()
	f_models_names.close()
	Oo_path = os.getcwd()
	L_name_model.clear()
	kk = []
	for x in range(0,len(L_link_model)):
		os.chdir(Oo_path)
		os.system(f"mkdir {L_name_model[x]}")
		os.chdir(f"{Oo_path}/{L_name_model[x]}")
		oxx_path = os.getcwd()
		r = requests.get(L_link_model[x])
		soup = BeautifulSoup(r.content,"html.parser")
		#searshing for every pack link
		kk = soup.find_all("div",{"class":"col-md-3 col-sm-3","style":"padding:0;"})
		'''
		#searshing for images :
		imm = soup.find_all("div",{"class":"mySlides fade-slide"})
		for i in range(0,len(imm)):
			z = imm[i].find("img").attrs['src']
			L_img_link.append(z)
			urllib.request.urlretrieve(f"{L_img_link[i]}",f"{i}.jpg")
			print(f"image {i} has been downloaded from this link {L_img_link[i]}")

		'''
		
	f_link_models.close()
	f_models_names.close()


print(po)





