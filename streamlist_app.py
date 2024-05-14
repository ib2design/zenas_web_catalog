import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Atheleisure Catalog')

#connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#run a snowflake query and put it all in a var called my_catalog
my_cur.execute ("SELECT  color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

my_data_row = my_cur.fetchone()

streamlit.text ("Hellow from Snowflake:")
streamlit.text(my_data_row)
