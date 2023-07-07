import streamlit as st
import plotly.graph_objects as go


def gauge_chart(value, title):
    if value <= 30:
        color = "red"
    elif value <= 70:
        color = "yellow"
    else:
        color = "green"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': 'white'},
                {'range': [30, 70], 'color': 'white'},
                {'range': [70, 100], 'color': 'white'}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 80
            }
        }
    ))

    return fig


# Streamlit uygulama başlatma
st.title("Revit Model Sağlık Kontrolü")
st.markdown("Bu örnekte Revit modelinin sağlık kontrolü sonuçlarını Gauge (ölçek) grafiği kullanarak gösteriyoruz.")

# Rastgele bir değer oluşturma
revit_puan = 65

# Gauge grafiğini oluşturma ve gösterme
fig = gauge_chart(revit_puan, "Revit Model Puanı")
st.plotly_chart(fig)
