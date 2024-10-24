import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
df[['manufacturer', 'model_name']] = df['model'].str.split(' ', n=1, expand=True)
df = df.drop(columns=['model'])
#We need at least one st.heaader with text
header = st.header("Joseph's Analysis")

#Atleast one histogram
#At least one checkbox
conditions = df['condition'].unique()
selected_conditions = []
st.title("Select Conditions")
for condition in conditions:
    if st.checkbox(condition, value=True):
        selected_conditions.append(condition)

filtered_df = df[df['condition'].isin(selected_conditions)]
        
fig1 = px.histogram(filtered_df , x = 'price' , y = 'manufacturer' , color = 'condition' ,
                   title= 'Average Price by Condition and Manufacturer',
                    labels = {'price': 'Price ($)' , 'manufacturer': 'Manufacturer'} ,
                     nbins = 10 )
st.title('Car Price by Condition Histogram')
st.write("This histogram shows the distribution of car prices by manufacturer based on the condition of the car")
st.plotly_chart(fig1)

#Aty least one scatter plot
mileage_vals = df['odometer'].unique()
selected_miles = []

#for odometer in mileage_vals:
   #if st.checkbox(odometer , value=True):
        #selected_miles.append(odometer)

filtered_miles_df = df[df['odometer'] != 0]

#df['odometer'] = df['odometer'].astype(int)

avg_price_by_miles = filtered_miles_df.groupby('odometer' , as_index=False)['price'].mean()

fig2 = px.scatter(
    df , 
    x = 'odometer' , 
    y = 'price' , 
    title= 'Average Car Price by Mileage' , 
    labels = {'odometer': 'Mileage' , 'price': 'Average Price ($)'} , 
    text= 'price'
)
st.title('Average Car Price by Mileage')
st.write("This scatter plot shows the average price of cars based on the selected mileage).")
st.plotly_chart(fig2)