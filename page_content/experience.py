import streamlit as st
import base64
import os
from components.interactive import display_interactive_chart  # 保留你原有导入

def experience_page():
    st.markdown("## Professional Experience")

    st.markdown("""
    ### Business Planning Intern, Department of Commerce  
    **RedNote (Xiaohongshu)** | *May 2023 – Aug 2023, Guangzhou*  

    - Created industry playbooks and analyzed backend search data to extract consumer insights across categories like oral care and skincare, supporting advertising optimization.  
    - Proposed tailored ad strategies (e.g., Splash Ads, Feed Ads) based on campaign data, improving merchant exposure and product virality.  
    - Tracked brand and competitor performance, supported 618 Festival promotions for brands such as Olay, Mentholatum, and Haleon with actionable strategic insights.  
    """)

    st.markdown("""
    ### Data Operations Intern, Two-wheeler Division  
    **Didi Chuxing** | *Nov 2022 – Feb 2023, Guangzhou*  

    - Built launch logic and maintained rollout data for electric vehicle expansion across 120+ cities in four southern regions.  
    - Supported headquarters in supervising city managers, monitoring progress on product launches and government coordination.  
    - Allocated resources like cycling cards and organized offline events to boost brand awareness and user engagement.  
    """)

    st.markdown("""
    ### Marketing Intern, RV and New Retail Division  
    **SAIC Chase** | *Jul 2022 – Oct 2022, Shanghai*  

    - Planned and executed the “Cool Between Mountains and Seas” campaign using real RV owner stories, generating 18,000 visits and 3,310 new users.  
    - Designed loyalty program and internal campaigns for RV owners, resulting in 300 inquiries and 12 deals within the first month.  
    - Promoted outdoor lifestyle content to enhance brand relevance and spark social sharing within travel communities.  
    """)

    st.markdown("---")