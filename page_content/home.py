import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>He Yongyan</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        <a href="heyongyanabc@163.com">heyongyanabc@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
    """
    ### About Me  
    I am a recent MSc in Marketing graduate from The Chinese University of Hong Kong, with a strong foundation in integrated marketing, brand strategy, and data-driven decision-making.

    During my internships at Xiaohongshu, Didi Chuxing, and SAIC, I led data-backed content strategies, planned high-impact campaigns, and collaborated with cross-functional teams to optimize brand performance. My experience spans consumer insights, performance marketing, and operational expansion—serving brands like Olay, Mentholatum, and Agoda.

    I'm passionate about combining creativity with analytics. Whether it's crafting compelling narratives for Gen Z audiences, using SQL and Python to guide marketing strategy, or leveraging AIGC tools like ChatGPT and Coze for content ideation and automation—I thrive at the intersection of marketing and tech.

    A proactive, adaptable team player fluent in Cantonese, English, and beginner Korean, I’m eager to bring fresh thinking and executional rigor to fast-paced, innovation-driven teams.
    """
    )

    st.markdown(
    """
    ### Skills  
    - Marketing & Strategy: Brand Positioning, Campaign Planning, Consumer Insights  
    - Content Creation: Copywriting, Community Operations, Event Planning, PR  
    - Data Analysis: Python, SQL, SPSS (Scraping, Analysis, Visualization)  
    - Tools & Platforms: MS Office, Moqups, Capcut, PR  
    - AIGC Applications: ChatGPT, Tongyi Tingwu (Audio), Jiemeng (Image), Coze (Workflow)  
    - Language Skills: Cantonese (Native), English (Fluent, IELTS 7), Korean (Beginner)  
    - Communication: Cross-team Collaboration, Strategic Reporting, KOL Coordination  
    """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 