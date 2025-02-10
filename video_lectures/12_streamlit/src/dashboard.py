import streamlit as st
from kpis import approved_percentage, total_application, number_approved, provider_kpis
from read_data import read_data
from charts import approved_by_area_bar

df = read_data()

def layout():
    st.markdown("# YH dashboard 2024 aplications")
    st.markdown(
        "This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard."
    )
    st.markdown("## KPIs in Sweden")

    labels = ("total applications", "number approved", "approved percentage")
    
    #st.metric(label=labels[0], value=total_application)
    # don't want to write this out 3 times so create a loop

    cols = st.columns(3)
    kpis = (total_application, number_approved, approved_percentage)
    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)

    st.markdown("## Approved by area")
    approved_by_area_bar()

    st.markdown("## Simple statistics on a given provider")
    st.markdown("Search for an educational provider")

    provider = st.selectbox(
        "Choose educational provider", df["Utbildningsanordnare administrativ enhet"].unique()
    )
    
    provider_application, provider_approved = provider_kpis(provider)
    st.markdown(f"This educational {provider} has applied fro {provider_application} educations and gotten {provider_approved} educations approved")
    

    st.markdown("## raw data")
    st.dataframe(df)

if __name__ == "__main__":
    layout()
