import api_handler
from database import DB
from api_handler import GeoAPI
from IPython.display import display
import pandas as pd
import requests 
import time

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})

_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
"heladoFrozen"]

discount_lst = _AVAILABLE_DISCOUNT_CODES

class Bot:
    def __init__(self, db, discount_lst, geoApi):
        self.__MAXIMUN_NUMBER_CHAR = 255
        self.__DB = db
        self.__discount_lst = discount_lst
        self.__set_of_lst = [set(i for i in row) for row in self.__discount_lst]
        self.__geoApi = geoApi
        self.__request_dict = dict()
        self.__catalogue = (self.__DB).available_items() 

    def inform_products_and_quantities(self):
        """
        Precondition: true  \n
        Postcondition: show a slice of catalogue by products which them quantity is greater than 0 

        """
        print(self.__catalogue)

    def validate_discount_code(self, discount_code):
        """
        Precondition: discount_code: str  \n
        Postcondition: return True if it finds a discount code in a list of codes that has less than 3\n 
                       elements difference compared to the input or False for everything else cases

        """
        return self.__search_differences(discount_code, 3)

    def __search_differences(self, discount_code, diff):
        """
        Precondition: discount_code: str and diff: int  \n
        Postcondition: return True if it finds a discount code in a list of codes that has less than 3\n 
                       elements difference compared to the input or False for everything else cases

        """

        discount_code_set = set(discount_code)
        count_diff = 0
        i = 0
        while(i < len(self.__set_of_lst) ):
            interception = discount_code_set.intersection(self.__set_of_lst[i])
            if(abs(len(interception) - len(discount_code_set)) < diff):
                count_diff += 1
                break
            i += 1


        return count_diff > 0        


    def __buy_product(self):
        """
        Precondition: true  \n
        Postcondition: a product with its quantities is removed from the cart\n 
                       and the database of the store is updated 3\n 

        """
        product = self.__request_dict.popitem()
        self.__DB.extract_by_id(product[0], product[1])
        

    def __order_request(self):
        """
        Precondition: true  \n
        Postcondition: if the user enters a valid id and a valid quantity of a product of the store's\n 
                database it will update the cart, otherwise, it terminates the operation instantly  \n 

        """

        print("Informe sus productos en el catálogo: ")
        
        self.inform_products_and_quantities() 
        print("===========================")

        try: 
            id = int(input("Seleccione id: "))
            quantity = int(input("Seleccione la cantidad: "))
        except:
            id = -1
            quantity = -1    


        while( self.__DB.id_in_range(id) and self.__DB.quantity_in_range(id, quantity)):   
            
            self.__add_to_cart(id, quantity)

            try: 
                id = int(input("Seleccione id para seguir comprando o -1 para continuar: "))
            except:
                break    
        

            if(id < 0):
                break        

            try:        
                quantity = int(input("Seleccione la cantidad: "))
            except:
                break 
               
   

           



    def __add_to_cart(self, id, quantity):
        """
        Precondition: id:Nat  \n
        Postcondition: update the cart with the purchased product and them quantity   \n 

        """
        self.__request_dict[id] = quantity   
    

# MAIN METHOD
    def call(self):
        """
        Precondition: true  \n
        Postcondition: clear the cart if its length is greater than 0 and show a small interface\n 
                       so that the user can carry out purchase operations\n
                                of which are:
                                    -order a purchase
                                    -validate discount code's of the user
                                    -buy the product and update the store's database 

        """

        if(self.__geoApi.is_hot_in_pehuajo() == True):
            print("Bienvenida 1")    
        else:
            print("Bienvenida 2")

        print("seleccione una opción: ")
        print("1. Solicitar pedido ")
        print("0. Salir")
        
        option = input()

        if(option[0].isdigit() and option[0] == '1'):
            self.__order_request()
        

            discount_code = list(input("Inserte código de descuento: " ))
        
            while(not self.validate_discount_code(discount_code)):
                
                discount_code = list(input("Inserte código de descuento: " ))

            option = input("Presione 1 para confirmar pedido o 0 para rechazar: ")

        if(option[0].isdigit() and option[0] == '1'):  

            print("Muchas gracias por su compra :)")      

            while(len(self.__request_dict.keys()) > 0):
                self.__buy_product()
            
        else:
            if(len(self.__request_dict.keys()) > 0):
                self.__request_dict.clear()     

        
       
            


     

    

print("Si ejecuta la documentaction.py presione 0 para verla")
geo = GeoAPI()
db = DB(_PRODUCT_DF)
bot = Bot(db, discount_lst, geo)
bot.call()
