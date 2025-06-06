import warnings
import streamlit as st
import os # 确保 os 已导入，如果下面的 print 语句需要

warnings.simplefilter(action="ignore", category=FutureWarning)

# 这是第一个 Streamlit 命令
st.set_page_config(page_title="personalsite", layout="wide")

# --- 现在可以在这里放置 st.write() 调试语句 ---
st.write(f"主脚本的当前工作目录 (CWD): {os.getcwd()}")
st.write(f"主脚本CWD下的文件/文件夹: {os.listdir('.')}")
# ... 其他 st.write() 调试信息 ...
# 或者，如果您使用了 print() 进行调试，它们可以放在 set_page_config 前后都没关系
print(f"主脚本的当前工作目录 (CWD): {os.getcwd()}")
# --- 调试代码结束 ---

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Load custom CSS
        load_css()

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.radio(
            "Navigation", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")

        app["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app
app.add_app("Home Page", home_page)
app.add_app("Education Page", education_page)
app.add_app("Experience Page", experience_page)
app.add_app("Resume Page", resume_page)
app.add_app("Contact Page", contact_page)

# Run the app
app.run()
