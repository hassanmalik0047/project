import streamlit as st

# Set page configuration
st.set_page_config(page_title="Portfolio", page_icon=":briefcase:", layout="wide")


# Home Section
def Home():
    st.title("Welcome to My Portfolio!")
    st.image("hassan.jpeg", width=200)
    st.header("Hassan Malik")
    st.subheader("Data Analyst | Data Scientist | Python | Web Scraping | C++")
    st.write(
        """ 
My name is Hassan Malik and i am currently pursuing a Bachelor's degree at the University of Central Punjab in Data Science. I am passionate about data science, programming, and C++. I have experience in Python programming, data manipulation, and data analysis and web scraping. I have completed multiple high-quality projects that have helped me to grow as professional. I have also experience in MySQL for managing databases. I am always eager to learn new technologies and improve my skills. I am looking for opportunities to work on challenging projects and grow as a professional.
"""
    )
    
    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }

        .instagram { background-color: #E1306C; }
        </style>
        <div class="social-buttons">
            <a href="https://www.instagram.com/hassanhayat68?igsh=YXY4M3ZwdmNzMzVs" target="_blank" class="instagram">Instagram</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# About Me Section
def About_section():
    st.header("About Me")
    st.write(
        """
        I am a Data Analyst and Data Scientist with a passion for data analysis, data visualization, and web scraping. I have gained experience by doing multiple projects. I have a strong hold on communication skills and problem-solving skills. I am always eager to learn new technologies and improve my skills. My doing projectsin team has helped me to improve my teamwork skills. Completing multiple projects have helped me to gain valuable lessons in field of information technology. I am looking for opportunities to work on challenging projects and grow as a professional.
        """
    )
    st.write("## Education")
    st.write("- Bachelor's in Data Science, University of Central Punjab (2022 - 2026)")
    st.write("- Intermediate in Computer Science, Punjab College (2022)")
    st.write("- Matriculation in Computer Science, Lahore Grammar School (2020)")
    
    st.write("## Expertise")
    st.write("- Backend Development (Python, C++)")
    st.write("- Data Analysis (Pandas, NumPy, MySQL)")
    st.write("- Data Visualization (Matplotlib, Seaborn)")
    st.write("- Web Scraping (Beautiful Soup, Scrapy)")
    
    st.write("## Languages")
    st.write("- English")
    st.write("- Urdu")
    st.write("- Hindi")
    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }

        .instagram { background-color: #E1306C; }
        
        </style>
        <div class="social-buttons">
            <a href="https://www.instagram.com/hassanhayat68?igsh=YXY4M3ZwdmNzMzVs" target="_blank" class="instagram">Instagram</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

def Project_section():
    # Define project details
    data = [
        {
            "title": "Web Scraping Odoo Portal",
            "description": "Web scraping project to extract data from Odoo portal.",
            "image": "odoo.jpeg", 
            "details": """
            **Process:**
            - Scraped useful information from the Odoo portal using Beautiful Soup.
            - Extracting information of teachers through multiple links.
            - Extracted useful and meaningul info of staff members and also extract their research interest.
 
            
            **Technologies:** Python, Beautiful Soup
            """
            
        },
        {
            "title": "School Management System",
            "description": "School management system to manage students, teachers.",
            "image": "school.jpeg",  
            "details": """
                **Process:**
                -  Created a main menu where user can select to manage,edit, delete info of students, teachers. 
                - Implemented a feature to add new and delete students and teachers.
                - Implemented a feature to delete students and teachers.
                - Implemented a feature to submit the fee of students.
                - Implemented a feature to view the fee of students.
                - Implemented a feature to submit the salary of teachers.
                
                **Technologies:** Python, Pandas, Numoy, VS code
            """
        },
        {
            "title": "Sales Dashboard using knime", 
            "description": "Sales dashboard to visualize the sales data.",
            "image": "knime.jpeg",  
            "details": """
            **Process:**
            - Performed multiple data cleaning operations on the data.
            - Implemented multiple widgets for data handling.
            - Implemented mutliple widgets of data visualization.
            - Created component to combine data visualization.
            **Technologies:** knime
            """
        },
    ]

    if "working_project" not in st.session_state:
        st.session_state.working_project = None

    if st.session_state.working_project is None:
        st.title("Projects")

        cols = st.columns(3)

        with cols[0]:
            st.image(data[0]["image"], width=250, caption="Scraping Odoo Portal")
            st.subheader(data[0]["title"])
            st.write(data[0]["description"])
            if st.button("View Details", key="view_0"):
                st.session_state.working_project = 0

        with cols[1]:
            st.image(data[1]["image"], width=350, caption="School Management System")
            st.subheader(data[1]["title"])
            st.write(data[1]["description"])
            if st.button("View Details", key="view_1"):
                st.session_state.working_project = 1

        with cols[2]:
            st.image(data[2]["image"], width=350, caption="Dashboard using knime")
            st.subheader(data[2]["title"])
            st.write(data[2]["description"])
            if st.button("View Details", key="view_2"):
                st.session_state.working_project = 2

    else:
        project_index = st.session_state.working_project
        project = data[project_index]

        st.title(project["title"])
        st.image(project["image"], width=350)
        st.write(project["details"])
        if st.button("Back to Projects"):
            st.session_state.working_project = None



def Certification():
    st.header("Certificates")
    
    certificate = [
        {
            "title": "Python",
            "issuer": "Udemy"
        },
        {
            "title": "C++",
            "issuer": "Udemy"
        },
        {
            "title": "MS Excel Certification",
            "issuer": "Coursera"
        },
        {
            "title": "Communication Skills",
            "issuer": "Coursera"
        }
    ]
    
    for certi in certificate:
        st.write(f"### {certi['title']}")
        st.write(f"**Issuer:** {certi['issuer']}")

    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    # Social Button
    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }

        .instagram { background-color: #E1306C; }
        </style>
        <div class="social-buttons">
            <a href="https://www.instagram.com/hassanhayat68?igsh=YXY4M3ZwdmNzMzVs" target="_blank" class="instagram">Instagram</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
# Skills Section
def skills():
    st.header("Technical Skills")
    skills_data = {
        "Python": 80,
        "MySQL": 70,
        "Data Analytics": 75,
        "Web Scraping": 80,
        "C++": 80
    }
    
    for skill, level in skills_data.items():
        st.write(f"{skill}")
        st.progress(level / 100)
    
    st.write("-------------")
    st.subheader("Soft Skills")
    st.write("- Communication skills")
    st.write("- Problem Solving")
    st.write("- Teamwork")
    st.write("- Time Management")
    st.write("- Analytical Thinking")

    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }
        .instagram { background-color: #E1306C; }
        </style>
        <div class="social-buttons">
            <a href="https://www.instagram.com/hassanhayat68?igsh=YXY4M3ZwdmNzMzVs" target="_blank" class="instagram">Instagram</a>

        </div>
        """,
        unsafe_allow_html=True,
    )

# Contact Section
def contact():
    st.markdown("""
    <style>
        .contact {
            background-color: #f0f0f5;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)
# User needs to fill the form 
# to contatct the owner of the portfolio
    st.header("Contact Me")
    with st.form("Contact Form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for reaching out!")

    st.markdown('</section>', unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    # Social Button
    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }
        .instagram { background-color: #E1306C; }
        </style>
        <div class="social-buttons">
            <a href="https://www.instagram.com/hassanhayat68?igsh=YXY4M3ZwdmNzMzVs" target="_blank" class="instagram">Instagram</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
# main function to run the app
def main():
    tabs = st.tabs(["Home", "About Me", "Projects", "Certificates", "Skills", "Contact"])
    with tabs[0]:
        Home()
    with tabs[1]:
        About_section()
    with tabs[2]:
        Project_section()
    with tabs[3]:
        Certification()
    with tabs[4]:
        skills()
    with tabs[5]:
        contact()

# Run the main function
if __name__ == "__main__":
    main()

