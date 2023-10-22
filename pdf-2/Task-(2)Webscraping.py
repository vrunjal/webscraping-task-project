# # Import request from lib if you have not install then install from cmd Pip install request
# import requests              #This is used for making HTTP requests in python
# #from bs4 import BeautifulSoup4 (you have to install pip install beautifulsoup4)
# from bs4 import BeautifulSoup    #This is used for extract data of HTML/XML ,searching and filtering ,Data extrrection in web scraping.
# # download mysql connectorand import connector
# import mysql.connector         #This will useful sql connection with MySQL database   
# #DB configure


# # Below is a database connection code
# databaseValue = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="admin123",
#   database="vrunjal"
# )

# # By this you can perform SELECT,UPDATE,INSERT,DELETE,ALTER queries
# cursor = databaseValue.cursor()

# # Create TABLE query
# create_table_query = "CREATE TABLE IF NOT EXISTS color (name VARCHAR(70) NOT NULL,color VARCHAR(70) NOT NULL)"
# # This will execute SELECT query
# cursor.execute(create_table_query)

# print(cursor)
# #URL for color code
# URL_path="https://teamcolorcodes.com/ncaa-color-codes/aac/"

# # HTTP get request to specify URL path used for fetching data from web server.
# data=requests.get(URL_path)

# soup=BeautifulSoup(data.content,"html.parser")
# data_element=soup.find_all(class_="colorbox")
# print(data_element)
# for data in data_element:
#     try:
#         name=data.div.text
#         color=data.div['style'].split(':')[1].strip()
#         insert_query = "INSERT INTO color(name,color)VALUES (%s, %s)"
#         cursor.execute(insert_query,(name,color))
#         databaseValue.commit()
#     except:
#         print("nothing to commit")
# databaseValue.close()


# Import request from lib if you have not install then install from cmd Pip install request
import requests
#from bs4 import BeautifulSoup (you have to download Beautifulsoup)
from bs4 import BeautifulSoup
# download mysql connectorand import connector
import mysql.connector
#DB configure

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin123',
    'database': 'webdataschema1'
}

data_DB= mysql.connector.connect(**db_config)
cursor = data_DB.cursor()

create_table_query = "CREATE TABLE color (name VARCHAR(255) NOT NULL,color VARCHAR(255) NOT NULL)"
cursor.execute(create_table_query)
print(cursor)
#URL for color code
URL_path="https://teamcolorcodes.com/ncaa-color-codes/acc-color-codes/"

data=requests.get(URL_path)
soup=BeautifulSoup(data.content,"html.parser")
data_element=soup.find_all("a",class_="team-button")
print(data_element)
for data_ in data_element:
    
    name=data_.text
    print(f"\n\n\n\n\n\n{name}\n\n\n\n\n\n")
    color=data_.get('style')
    print(f"\n\n\n\n\n\n{color}\n\n\n\n\n\n")
    insert_query = "INSERT INTO color(name,color)VALUES (%s, %s)"
    cursor.execute(insert_query,(name,color))
    data_DB.commit()
data_DB.close()