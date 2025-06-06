import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="HE Yongyan.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("HE, Yongyan | Claudia")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** heyongyanclaudia@gmail.com  
    - **Phone:** 18127967539  
    - **LinkedIn:** [linkedin.com/in/yongyan-he-claudia](https://linkedin.com/in/yongyan-he-claudia)
    """)

    st.header("Professional Summary")
    st.markdown("""
    Aspiring marketing and data strategy professional with experience across brand planning, data operations, and campaign execution.  
    Proven ability to translate consumer insights and platform data into actionable strategies, with internship experience at Xiaohongshu, Didi, and SAIC.  
    Strong academic background from QS Top 50 The Chinese University of Hong Kong, with hands-on project leadership in brand transformation and user growth.  
    Proficient in marketing tools, data analysis, and AI-based content generation, eager to contribute to dynamic teams driving digital innovation.
    """)

    st.header("Professional Experience")
    st.markdown("""
    ### Business Planning Intern, Department of Commerce  
    **RedNote (Xiaohongshu)** | *May 2023 – Aug 2023, Guangzhou*  
    - Created industry playbooks and analyzed backend search data to extract consumer insights across categories like oral care and skincare.  
    - Proposed tailored ad strategies (e.g., Splash Ads, Feed Ads) based on campaign data, improving merchant exposure and product virality.  
    - Tracked brand and competitor performance, supported 618 Festival promotions for brands such as Olay, Mentholatum, and Haleon.  

    ### Data Operations Intern, Two-wheeler Division  
    **Didi Chuxing** | *Nov 2022 – Feb 2023, Guangzhou*  
    - Built launch logic and maintained rollout data for electric vehicle expansion across 120+ cities.  
    - Supported city teams and HQ in tracking launch progress and managing operational goals.  
    - Allocated ride cards and hosted city events to improve user engagement and brand awareness.  

    ### Marketing Intern, RV and New Retail Division  
    **SAIC Chase** | *Jul 2022 – Oct 2022, Shanghai*  
    - Launched the “Cool Between Mountains and Seas” RV lifestyle campaign, generating 18,000 mini-program visits and 3,310 new users.  
    - Created loyalty programs and internal events for RV owners, resulting in 300 leads and 12 sales in the first month.  
    """)

    st.header("Education")
    st.markdown("""
    **MSc in Marketing**  
    - The Chinese University of Hong Kong (QS Top 50)  
    - *Aug 2024 – Nov 2025*

    **BBA in Tourism Management**  
    - Sun Yat-sen University (985)  
    - *Sep 2020 – Jun 2024*
    """)

    st.header("Skills")
    st.markdown("""
    - **Content & Campaigns:** Copywriting, Event Planning, Community Operations, PR, Video/Image Editing  
    - **Data Analysis Tools:** Python, SQL, SPSS, Excel, Moqups  
    - **Languages:** Cantonese (Native), English (Fluent, IELTS 7), Korean (Beginner)  
    - **AIGC Tools:** ChatGPT, Tongyi Tingwu, Cursor, Coze, Jiemeng  
    - **Design Tools:** CapCut, Premiere Pro  
    """)

    st.header("Projects")
    st.markdown("""
    ### Agoda Rebranding IMC Plan  
    - Conducted market analysis and SWOT research on brand trust crisis in China.  
    - Created KOL-driven campaigns using Douyin and Xiaohongshu, using a "Then vs. Now" narrative to rebuild trust.  
    - Applied AI-generated ad visuals and ran A/B tests to optimize CTR and sentiment metrics.

    ### EDUA Career Advantage Program (Team Lead)  
    - Designed and launched workshops such as “Hogwarts Career Lab” to explore innovative employment formats.  
    - Delivered cold-start user acquisition (70+ users in 2 weeks), achieving 50%+ consultation conversion and 15% deal rate.  
    - Led team operations and wrote content strategies for marketing events and brand exposure.
    """)

    st.header("Languages")
    st.markdown("""
    - **Cantonese:** Native  
    - **English:** Fluent (IELTS 7)  
    - **Korean:** Beginner  
    """)

    st.header("Interests")
    st.markdown("""
    - Branding & Consumer Psychology  
    - Data-Driven Campaign Strategy  
    - Outdoor Travel & Lifestyle Communities  
    """)

    st.markdown("---") 