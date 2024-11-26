import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Data Visualizer")
st.write("Upload a CSV file to visualize the data.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Read CSV
    data = pd.read_csv(uploaded_file)

    # Display DataFrame
    st.write("Data Preview:")
    st.dataframe(data)

    # Select columns
    numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
    if numeric_columns.empty:
        st.warning("No numeric columns to visualize.")
    else:
        chart_type = st.selectbox(
            "Select Chart Type", ["Line Chart", "Bar Chart", "Histogram"]
        )

        x_axis = st.selectbox("Select X-axis column", numeric_columns)
        y_axis = st.selectbox("Select Y-axis column", numeric_columns)

        if st.button("Generate Chart"):
            fig, ax = plt.subplots()
            if chart_type == "Line Chart":
                ax.plot(data[x_axis], data[y_axis], marker="o")
                ax.set_title("Line Chart")
            elif chart_type == "Bar Chart":
                ax.bar(data[x_axis], data[y_axis])
                ax.set_title("Bar Chart")
            elif chart_type == "Histogram":
                ax.hist(data[x_axis], bins=20, alpha=0.7, label=x_axis)
                ax.hist(data[y_axis], bins=20, alpha=0.7, label=y_axis)
                ax.legend()
                ax.set_title("Histogram")

            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            st.pyplot(fig)
