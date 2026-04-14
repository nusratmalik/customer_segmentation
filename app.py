import streamlit as st
import pickle
import numpy as np
kmeans= pickle.load(open("k_means.pickle", 'rb'))

cluster_descriptions = {
    0: "Cluster 0: Customers with medium annual income and medium annual spend",
    1: "Cluster 1: Customers with high annual income and high annual spend",
    2: "Cluster 2: Customers with low annual income and high annual spend",
    3: "Cluster 3: Customers high annual income but low annual spend ",
    4: "Cluster 4: Customers with low annual income and low annual spend"
}

#streamlit App
st.title("Mall Customer Segmentation")
st.write("Predict the customer segment based on user inputs.")

 #user inputs

annual_income= st.slider("Enter Annual Income in $", 0, 200, 1)
spending_score=st.slider("Spending Score", 0, 100, 50)

 #predict cluster

if st.button("Predict Cluster"):

    user_data =np.array([[annual_income, spending_score]])
    predicted_cluster= kmeans.predict(user_data)[0]


    st.subheader (f"The Customer belongs to Cluster {predicted_cluster}")
    st.write(cluster_descriptions.get(predicted_cluster,"Cluster description not available"))