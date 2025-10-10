import streamlit as st
import os
import json
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")

def show_NVDA_news():
    ordner = os.path.join(os.getcwd(), "Output", today)
    dateiname = "tagesschau_NVDA.json"
    pfad = os.path.join(ordner, dateiname)

    if os.path.exists(pfad):
        with open(pfad, 'r', encoding='utf-8') as file:
            data = json.load(file)

            def get_date(item):
                return item.get("date", "")

            st.subheader("Company Specific News")
            company_news = sorted(data.get("company_specific", []), key=get_date, reverse=True)
            for news in company_news:
                date_str = news.get("date", "").replace("T", " ").replace("Z", "")[:19]
                st.markdown(f"**{news.get('title', '')}**  \n{date_str}")
                st.write(news.get('firstSentence', ''))
                st.markdown(f"[Weiterlesen]({news.get('shareURL', '#')})")
                st.write("---")

            st.subheader("Sector/Industry News")
            sector_news = sorted(data.get("sector_industry", []), key=get_date, reverse=True)
            for news in sector_news:
                date_str = news.get("date", "").replace("T", " ").replace("Z", "")[:19]
                st.markdown(f"**{news.get('title', '')}**  \n{date_str}")
                st.write(news.get('firstSentence', ''))
                st.markdown(f"[Weiterlesen]({news.get('shareURL', '#')})")
                st.write("---")
    else:
        st.warning(f"Datei nicht gefunden: {pfad}")


def filter_by_otp(api_data, otp_value="meldung"):
    news_list = api_data.get("news", []) or api_data.get("items", [])
    filtered_news = [
        news for news in news_list
        if any(track.get("otp", "").lower() == otp_value.lower() for track in news.get("tracking", []))
    ]
    return {"news": filtered_news}


with st.container():
    st.title("Tagesschau News App")
    st.write(f"Heutiges Datum: {today}")

    ordner = os.path.join(os.getcwd(), "Output", today)
    dateiname = "tagesschau.json"
    pfad = os.path.join(ordner, dateiname)

    if os.path.exists(pfad):
        with open(pfad, 'r', encoding='utf-8') as file:
            data = json.load(file)
            filtered_data = filter_by_otp(data, otp_value="meldung")

            st.subheader("Letzte 5 Nachrichten von Tagesschau")
            news_list = filtered_data.get("news", [])
            latest_news = sorted(news_list, key=lambda x: x.get("date", ""), reverse=True)[:5]

            for news in latest_news:
                date_str = news.get("date", "").replace("T", " ").replace("Z", "")[:19]
                st.markdown(f"**{news.get('title', '')}**  \n{date_str}")
                col1, col2 = st.columns([3, 1])
                col1.write(news.get('firstSentence', ''))
                col2.markdown(f"[Weiterlesen]({news.get('shareURL', '#')})")
                st.write("---")
    else:
        st.warning(f"Datei nicht gefunden: {pfad}")
