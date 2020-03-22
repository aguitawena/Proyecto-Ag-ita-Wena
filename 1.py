from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib #para enviar correos
#definir url
my_url = 'https://www.oddsportal.com/sure-bets/'
class Scraper():
    def __init__(self): #inicio las variables 
        self.porcentaje=''
        self.profit=''
        self.listapo=[]
        self.listacasas=[]
        self.cuenta=[]
        self.final=[]

        
    def abrirpag(self):
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
        driver.get(my_url)
        content = driver.page_source
        self.soup = BeautifulSoup(content,"html.parser")
        self.porcentaje = (self.soup.find_all("td",{"center bold"}))
        self.odd = (self.soup.find_all("tr",{"odd"}))
        self.odd1 = (self.soup.find_all("td",{"center"}))
        
        driver.close()
    def values(self):
        for i in self.porcentaje:
            self.profit =i.get_text().strip() #busco los porcentajes
            self.listapo.append(float(self.profit[:-1])) #les quito el %
        for i in self.odd1:
            i=i.find("a")
            if i==None:
                pass
            if not i==None:
                i=i.get('title') #busco el nombre de las casas
                self.listacasas.append(i)

    def casas(self):
        for i in self.odd:
            
            i=i.findAll("div",{"odds-nowrp"})
            self.cuenta.append(int(len(i)))
        
    def gdf(self):
        
        listatemp=[]
        a=0
        b=0
            
        for i in self.listacasas:
            if a<int(self.cuenta[b]):
                listatemp.append(i)
                a=a+1
            if a==int(self.cuenta[b]):
                
                self.final.append([listatemp,self.listapo[b]])
                
                b=b+1
                listatemp=[]
                a=0
        print(self.final)
        
    def enviarcorreo(self):
        for i in self.listapo:
            if i>=6:
                print("Envia correo")       
                
                
scrap=Scraper()

scrap.abrirpag()
scrap.values()
scrap.casas()
scrap.gdf()
#scrap.enviarcorreo()