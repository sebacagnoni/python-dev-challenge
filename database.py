import pandas as pd
from IPython.display import display

class DB:
    def __init__(self, df):
        self.__key_column = df.columns[0]
        self.__value_column = df.columns[1]
        self.__db_ord = df
        df.sort_values(by= self.__key_column, ascending=True, inplace=True, kind='mergesort', ignore_index=True)
        #display(df)
        #display(self.__db_ord)

    def id_in_range(self, id):
        """
        Precondition: id:int  \n
        Postcondition: return True if the id is a valid id in the database or False in otherwise cases  \n 

        """
        id = int(id)
        len = (self.__db_ord)[self.__key_column].size

        return 0 <= id and id < len 

    def quantity_in_range(self, id, quantity): 
        """
        Precondition: id:int and quantity: int  \n
        Postcondition: return True if the quantity given a valid id is less or equal\n 
                       compared the quantity of the position of the second column or False in otherwise cases\n 

        """

        id = int(id)
        quantity = int(quantity)   
        quantity_df = self.__db_ord[self.__value_column][id].astype(int, copy=True)
        return  quantity_df >= quantity

    def key_column(self):
        """
        Precondition: true \n
        Postcondition: return the name of key column in the database in the 0 column

        """
        return self.__key_column   

    def value_column(self):
        """
        Precondition: true \n
        Postcondition: return the name of value column in the database in the 0 column

        """
        return self.__value_column     
        

    def __binary_search(self, element):
        """
        Precondition: element:str and a sorted array of search \n
        Postcondition: return True if the element appeared in the key column of the sorted database

        """
        upper = (self.__db_ord[self.__key_column]).size - 1
        lower = 0
        index = -1

        while(lower <= upper ):
            mid = (lower + upper) // 2
            
            if((self.__db_ord[self.__key_column])[mid] > element):
                upper = mid - 1
            elif((self.__db_ord[self.__key_column])[mid] < element):
                lower = mid + 1    
            else:
                index = mid
                lower = upper + 1
                

        return index        

                    
    def is_available(self, item):
        """
        Precondition: item:str and a sorted array of search \n
        Postcondition: return a tuple t = (bool, int) that the first element of t represent if the item exist\n 
                            in the key column and the second element of t represent\n 
                            the id in which the item are located or -1 if not

        """
        index = self.__binary_search(item)
        
        if(index != -1 and self.__db_ord[self.__value_column][index] > 0):
            return (True, index) 
        else:
            return (False, index)

    def extract_by_id(self, id, quantity):
        """
        Precondition: id:nat and valid quantity \n
        Postcondition: update the database only remove the quantity of the id given

        """
        self.__db_ord.at[id , self.__value_column] -= quantity

    def extract_item(self, item, quantity):
        item_info = self.is_available(item)
        """
        Precondition: item:str and valid quantity \n
        Postcondition: update the database only remove the quantity of the id given different to extract_by_id because\n
                       this method search if the item is avaible in the key column of the database

        """

        if(item_info[0] == True and quantity <= self.__db_ord[self.__value_column][item_info[1]]):
            self.__db_ord.at[item_info[1] , self.__value_column] -= quantity
        else:
            raise Exception("Error, item not avaible or quantity out of range")   

    def available_items(self): 
        """
        Precondition: true \n
        Postcondition: show the database whichs rows in the value column is greater than 0

        """
        return self.__db_ord.loc[self.__db_ord[self.__value_column] > 0] 

    def display_db(self):
        """
        Precondition: true \n
        Postcondition: shows the complete database

        """
        display(self.__db_ord)    

        
