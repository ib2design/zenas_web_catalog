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

#put the data into a dataframe
df = pandas.DataFrame(my_catalog)

#write dataframe to page for validation
streamlit.write(df)

#put first column into a list
color_list = df[0].values.tolist()

#pick list to pick the color
option = streamlit.selectbox('Pick a Sweatsuit color or style:', list(color_list))

#image caption
product_caption = ('Our warm, comfortable, ' + option + ' sweatsuit!')


