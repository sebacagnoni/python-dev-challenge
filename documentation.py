
from bot import *
from api_handler import *
from database import *

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})
print("presione 0 para ver la documentacion")

db = DB(_PRODUCT_DF)



bot = Bot(db, discount_lst, geo)
geo = GeoAPI()

doc_bot_call = bot.call.__doc__
doc_bot_ipq = bot.inform_products_and_quantities.__doc__
doc_bot_vdc = bot.validate_discount_code.__doc__

doc_db_id_in_range = db.id_in_range.__doc__
doc_db_qu_in_range = db.quantity_in_range.__doc__
doc_db_kc = db.key_column.__doc__
doc_db_vc = db.value_column.__doc__
doc_db_ia = db.is_available.__doc__
doc_db_ebid = db.extract_by_id.__doc__
doc_db_eit = db.extract_item.__doc__
doc_db_ait = db.available_items.__doc__
doc_db_ddb = db.display_db.__doc__


doc_aph_ihip = geo.is_hot_in_pehuajo.__doc__
doc_aph_sll = geo.set_lat_long.__doc__

doc_bot_call_n = bot.call.__name__
doc_bot_ipq_n = bot.inform_products_and_quantities.__name__
doc_bot_vdc_n = bot.validate_discount_code.__name__

doc_db_id_in_range_n = db.id_in_range.__name__
doc_db_qu_in_range_n = db.quantity_in_range.__name__
doc_db_kc_n = db.key_column.__name__
doc_db_vc_n = db.value_column.__name__
doc_db_ia_n = db.is_available.__name__
doc_db_ebid_n = db.extract_by_id.__name__
doc_db_eit_n = db.extract_item.__name__
doc_db_ait_n = db.available_items.__name__
doc_db_ddb_n = db.display_db.__name__


doc_aph_ihip_n = geo.is_hot_in_pehuajo.__name__
doc_aph_sll_n = geo.set_lat_long.__name__


print(doc_bot_call_n)
print(doc_bot_call)

print(doc_bot_ipq_n)
print(doc_bot_ipq)

print(doc_bot_vdc_n)
print(doc_bot_vdc)

print(doc_db_id_in_range_n)
print(doc_db_id_in_range)

print(doc_db_qu_in_range_n)
print(doc_db_qu_in_range)

print(doc_db_kc_n)
print(doc_db_kc)

print(doc_db_vc_n)
print(doc_db_vc)

print(doc_db_ia_n)
print(doc_db_ia)

print(doc_db_ebid_n)
print(doc_db_ebid)

print(doc_db_eit_n)
print(doc_db_eit)

print(doc_db_ait_n)
print(doc_db_ait)

print(doc_db_ddb_n)
print(doc_db_ddb)


print(doc_aph_ihip_n)
print(doc_aph_ihip)

print(doc_aph_sll_n)
print(doc_aph_sll)