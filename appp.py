import pandas as pd
import numpy as np
import streamlit as st
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


# data importing 
data = pd.read_xlsx("Product.xlsx")
df = data.pivot_table(index="Facilities", columns="Email", values="Rating").fillna(0)
df_matrix = csr_matrix(df.values) # converting the table to an array matrix
model_knn = NearestNeighbors(metric="cosine", algorithm="brute")
model_knn.fit(df_matrix)

def recom_system(distances, indices, index):
    pro = None
    rec = []
    for i in range(0, len(distances.flatten())):
        if i == 0:
            pro = df.index[index].values[0]
        else:
            rec.append(df.index[indices.flatten()[i]])
    return pro, rec



def main():
    st.title("Product Recommendation System")
    st.write("Banking Products")
    if st.checkbox("Registered Users"):
        st.write(data[["Email","Facilities","Rating"]].head())
    user = st.text_input("Enter your mail")
    if st.button("Enter"):
        if user in list(data["Email"].unique()):
            st.write(f"Welcome back! {user[:9].upper()}")
            index = data[data["Email"]==user].index.values
            # print(index)
            distances, indices = model_knn.kneighbors(df.iloc[index,:].values.reshape(1,-1), n_neighbors=6)
            product, rec = recom_system(distances, indices, index)
            st.write(f"your current product : ' __{product}__ '")
            st.write("#### Products you may like ")
            col1, col2, col3, col4, col5  = st.columns(5)
            with col1:
                st.write(f"__{rec[0]}__")
                st.image("https://i.gifer.com/JVX7.gif")
            with col2:
                st.write(f"__{rec[1]}__")
                st.image("https://i.gifer.com/JVX7.gif")
            with col3:
                st.write(f"__{rec[2]}__")
                st.image("https://i.gifer.com/JVX7.gif")
            with col4:
                st.write(f"__{rec[3]}__")
                st.image("https://i.gifer.com/JVX7.gif")
            with col5:
                st.write(f"__{rec[4]}__")
                st.image("https://i.gifer.com/JVX7.gif")
            st.button("home")
        else:
            st.error("User not Registered")
            st.write("create a new account or use registered email")
    # st.markdown("##### Create a Account")
    else:
        if "button_clicked" not in st.session_state:
            st.session_state.button_clicked = False
        if (st.button("Create Account") or st.session_state.button_clicked):

            user_mail = st.text_input("Your Email")
            # st.session_state
            if (st.button("Sign up!") or st.session_state.button_clicked):
                st.success("Successful")
                st.subheader("Welcome new user!")
                st.write("Welcome to our Bank")
                select = st.multiselect("Products Available", list(data["Facilities"].unique()))
                # st.write("your selected product: ",select)
                st.write("#### Some popular products ")
                rec2 = list(data.loc[data["Rating"]>4.9, "Facilities"].unique())[:6]
                print(rec2)
                col1, col2, col3, col4, col5  = st.columns(5)
                with col1:
                    st.write(f"__{rec2[0]}__")
                    st.image("https://i.gifer.com/9uff.gif")
                with col2:
                    st.write(f"__{rec2[1]}__")
                    st.image("https://i.gifer.com/9uff.gif")
                with col3:
                    st.write(f"__{rec2[2]}__")
                    st.image("https://i.gifer.com/9uff.gif")
                with col4:
                    st.write(f"__{rec2[3]}__")
                    st.image("https://i.gifer.com/9uff.gif")
                with col5:
                    st.write(f"__{rec2[4]}__")
                    st.image("https://i.gifer.com/9uff.gif")
                st.balloons()
                st.button("home", on_click=home)


    st.write("## Thank you for Visiting \nProject by Suyog J")
    st.markdown("<h1 style='text-align: right; color: #d7e3fc; font-size: small;'><a href='https://github.com/suyog56'>Looking for Source Code?</a></h1>", 
    unsafe_allow_html=True)

if __name__ == "__main__":
    main()