import streamlit as st
import os
import sys
import json
import datetime

with st.container():
    st.title("Tagesschau News App")

    today = datetime.date.today().strftime("%Y-%m-%d")
    st.write(f"Heutiges Datum: {today}")

    # Korrigierter Pfad: Absoluter Pfad mit os.path.join
    ordner = os.path.join(os.getcwd(), "Output", today)
    dateiname = "tagesschau_NVDA.json"
    pfad = os.path.join(ordner, dateiname)

    if os.path.exists(pfad):
        with open(pfad, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Sortierte Anzeige der News nach Datum (absteigend)
            def get_date(item):
                return item.get("date", "")

            st.subheader("Company Specific News")
            company_news = sorted(data.get("company_specific", []), key=get_date, reverse=True)
            for news in company_news:
                st.markdown(f"**{news.get('title', '')}**  \n{news.get('date', '')}")
                st.write(news.get('firstSentence', ''))
                st.markdown(f"[Weiterlesen]({news.get('shareURL', '#')})")
                st.write("---")

            st.subheader("Sector/Industry News")
            sector_news = sorted(data.get("sector_industry", []), key=get_date, reverse=True)
            for news in sector_news:
                st.markdown(f"**{news.get('title', '')}**  \n{news.get('date', '')}")
                st.write(news.get('firstSentence', ''))
                st.markdown(f"[Weiterlesen]({news.get('shareURL', '#')})")
                st.write("---")
    else:
        st.warning(f"Datei nicht gefunden: {pfad}")
