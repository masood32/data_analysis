import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns



def main():
    st.title("This is app for ecomm I am creating")
    st.sidebar.title("You can upload your file here")
    upload_file = st.sidebar.file_uploader("Upload your file here", type = ["csv", "xlsx"])
    if upload_file is not None:
        try:
            if upload_file.name.endswith(".csv"):
                data = pd.read_csv(upload_file)
            else:
                data= pd.read_excel(upload_file)
            st.sidebar.success("file uploaded successfully")
            st.subheader("I am going to show you some data details")
            st.dataframe(data.head())
            st.subheader("I am going to show you some more data details")
            st.write("shape of data", data.shape)
            st.write("the column name inside the data is: ", data.columns)
            st.write("missing values into columns", data.isnull().sum())

            st.subheader("I will show you some bit of stats")

            st.write(data.describe())
            st.write("count of the data", data.count())
            st.write("mean of the data", data.mean())
            st.write("median of the data", data.median())
            st.write("mode of the data", data.mode().iloc[0])
            st.write("standard deviation of the data", data.std())

                        


        except Exception as e:
            print(e)



                                                    




if __name__ == "__main__":
    main()

