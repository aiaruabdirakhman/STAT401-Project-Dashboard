import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="STAT401 Dashboard", layout="wide")

# Universal Color Palette
SPRING_COLOR_PALETTE = [
    "#E0F2E9", "#CCEBC5", "#99D8C9", "#66C2A5", 
    "#33B896", "#00A080", "#007F6A", "#005E51"
]

st.title("Earthquake Impact & Housing Policy Dashboard – Türkiye")

# --- Q1 ---
st.header("Q1 – Social vs Earthquake Housing Laws (Last Five Years)")
q1_pdf = pd.DataFrame({"year": [2022, 2023, 2024, 2025, 2026], "sosyal_konut": [2, 3, 1, 0, 1], "afet_konut": [3, 5, 3, 2, 2]})
fig_q1 = px.bar(q1_pdf, x="year", y=["sosyal_konut", "afet_konut"], barmode="group", 
                color_discrete_sequence=[SPRING_COLOR_PALETTE[2], SPRING_COLOR_PALETTE[1]])
st.plotly_chart(fig_q1, use_container_width=True)

# --- Q2 ---
st.header("Q2 – Ministry vs Presidential Language (2020–2026)")
q2_pdf = pd.DataFrame({"year": [2020, 2021, 2022, 2023, 2024, 2025, 2026], "ministry_refs": [7, 4, 6, 9, 8, 7, 2], "pres_refs": [10, 4, 6, 10, 9, 7, 2]})
fig_q2 = px.line(q2_pdf, x="year", y=["ministry_refs", "pres_refs"], markers=True, 
                 color_discrete_sequence=[SPRING_COLOR_PALETTE[2], SPRING_COLOR_PALETTE[1]])
st.plotly_chart(fig_q2, use_container_width=True)

# --- Q3 (Heatmap) ---
st.header("Q3 – Keyword Frequency Grid")
treemap_df = pd.DataFrame({"word": ["ilişkin", "bağı", "mahallesi", "ilçesine", "ilçesinde", "yürütólen", "inşaa", "dönüşüm", "kentsel", "diyarbakır", "toki", "durumuna", "akıbetine", "edilen", "deprem"], "count": [13, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2]})
z_data = [treemap_df['count'][i:i+5].tolist() for i in range(0, 15, 5)]
text_data = [treemap_df['word'][i:i+5].tolist() for i in range(0, 15, 5)]
fig_q3_heat = go.Figure(data=go.Heatmap(z=z_data, text=text_data, texttemplate="%{text}<br>%{z}", colorscale=[[0, SPRING_COLOR_PALETTE[0]], [1, SPRING_COLOR_PALETTE[4]]], showscale=False))
st.plotly_chart(fig_q3_heat, use_container_width=True)

# --- Q3 (Bar) ---
st.header("Q3 – Earthquake Questions by Ministry")
q3_min = pd.DataFrame({"ministry_name": ["Diğer", "Çevre, Şehircilik ve İklim Değişikliği Bakanlığı", "İçişleri Bakanlığı / AFAD", "Hazine ve Maliye Bakanlığı"], "total_eq_questions": [1181, 714, 323, 295], "unanswered_eq_questions": [279, 241, 136, 154]})
q3_min["answered_eq_questions"] = q3_min["total_eq_questions"] - q3_min["unanswered_eq_questions"]
q3_long = q3_min.melt(id_vars="ministry_name", value_vars=["answered_eq_questions", "unanswered_eq_questions"])
fig_q3_bar = px.bar(q3_long, x="ministry_name", y="value", color="variable", barmode="stack", color_discrete_sequence=[SPRING_COLOR_PALETTE[2], SPRING_COLOR_PALETTE[1]])
st.plotly_chart(fig_q3_bar, use_container_width=True)

# --- Q4 ---
st.header("Q4 – Composition of Motions by Province and Theme")

q4_pdf = pd.DataFrame({
    "province": ["İstanbul", "Ankara", "İzmir", "Adana", "Mersin", "Şanlıurfa", "Hatay", "Van"],
    "earthquake": [35, 22, 18, 20, 19, 24, 27, 21],
    "agriculture": [28, 19, 21, 17, 16, 14, 10, 11],
    "stray": [24, 15, 14, 13, 12, 8, 7, 6]
})

q4_long = q4_pdf.melt(
    id_vars="province",
    value_vars=["earthquake", "agriculture", "stray"]
)

fig_q4 = px.bar(
    q4_long,
    x="province",
    y="value",
    color="variable",
    barmode="stack",
    color_discrete_sequence=[
        SPRING_COLOR_PALETTE[2],
        SPRING_COLOR_PALETTE[1],
        SPRING_COLOR_PALETTE[3]
    ]
)

st.plotly_chart(fig_q4, use_container_width=True)

# --- Q5 ---
st.header("Q5 – Maximum Fines for Construction-Related Violations")

q5_pdf = pd.DataFrame({
    "year": [2020, 2022, 2023, 2024, 2026],
    "max_fine_tl": [250000, 500000, 750000, 1000000, 1500000],
    "law_no": [7244, 7410, 7456, 7534, 7579]
})

fig_q5 = px.bar(
    q5_pdf,
    x="year",
    y="max_fine_tl",
    color_discrete_sequence=[SPRING_COLOR_PALETTE[2]]
)

fig_q5.add_trace(
    go.Scatter(
        x=q5_pdf["year"],
        y=q5_pdf["max_fine_tl"],
        mode="lines+markers+text",
        text=q5_pdf["law_no"],
        line=dict(color=SPRING_COLOR_PALETTE[4]),
        marker=dict(color=SPRING_COLOR_PALETTE[4])
    )
)

st.plotly_chart(fig_q5, use_container_width=True)

# --- Q6 ---
st.header("Q6 – Disaster Fiscal Laws vs Laws with Write-off")

q6_pdf = pd.DataFrame({
    "year": [2021, 2022, 2023, 2024, 2025, 2026],
    "disaster_laws": [7, 7, 16, 6, 5, 1],
    "writeoff_laws": [1, 3, 5, 2, 2, 1]
})

q6_long = q6_pdf.melt(
    id_vars="year",
    value_vars=["disaster_laws", "writeoff_laws"]
)

fig_q6 = px.line(
    q6_long,
    x="year",
    y="value",
    color="variable",
    markers=True,
    color_discrete_sequence=[
        SPRING_COLOR_PALETTE[2],
        SPRING_COLOR_PALETTE[1]
    ]
)

st.plotly_chart(fig_q6, use_container_width=True)
