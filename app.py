import streamlit as st
import re
import sqlite3
import pandas as pd
import resume
from resume import emaill
st.set_page_config(page_title="CareerCrafter", page_icon="fevicon.jpg", layout="centered", initial_sidebar_state="auto", menu_items=None)
def set_bg_hack_url():       
    st.markdown(
          f"""
          <style>
          .stApp {{
              background: url("https://cdn.pixabay.com/photo/2016/04/15/04/02/water-1330252_1280.jpg");
              background-size: cover
          }}
          </style>
          """,
          unsafe_allow_html=True
      )
set_bg_hack_url()

conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(User TEXT,FirstName TEXT,LastName TEXT,Mobile TEXT,City TEXT,Email TEXT,password TEXT,Cpassword TEXT)')
def add_userdata(User,FirstName,LastName,Mobile,City,Email,password,Cpassword):
    c.execute('INSERT INTO userstable(User,FirstName,LastName,Mobile,City,Email,password,Cpassword) VALUES (?,?,?,?,?,?,?,?)',(User,FirstName,LastName,Mobile,City,Email,password,Cpassword))
    conn.commit()
def login_user(User,Email,password):
    c.execute('SELECT * FROM userstable WHERE User=? AND Email =? AND password = ?',(User,Email,password))
    data = c.fetchall()
    return data
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
def delete_user(Email):
    c.execute("DELETE FROM userstable WHERE Email="+"'"+Email+"'")
    conn.commit()
def create_job():
    c.execute('CREATE TABLE IF NOT EXISTS userstable1(Email TEXT,JT TEXT,JR TEXT,JP TEXT,JL TEXT)')
def add_job(Email,JT,JR,JP,JL):
    c.execute('INSERT INTO userstable1(Email,JT,JR,JP,JL) VALUES (?,?,?,?,?)',(Email,JT,JR,JP,JL))
    conn.commit()
def view_all_job(Email):
	c.execute("SELECT * FROM userstable1 WHERE Email=?", (Email,))
	data = c.fetchall()
	return data
def delete_job(JT):
    c.execute("DELETE FROM userstable1 WHERE JT="+"'"+JT+"'")
    conn.commit()
def update_pass(Email,Password):
    c=conn.cursor()
    c.execute('UPDATE userstable SET password="'+Password+'",Cpassword="'+Password+'" WHERE Email=="'+Email+'";')
    conn.commit()
def search_job(sj):
    c.execute("SELECT * FROM userstable1 WHERE JR=?", (sj,))
    data = c.fetchall()
    return data
def check_prof():
    c.execute("SELECT * FROM userstable WHERE User=?", ("User",))
    data = c.fetchall()
    return data

st.image("logo.png")
menu  = ["Home","Login","SignUp","Contact US"]
choice = st.sidebar.selectbox("Menu",menu)

if choice=="Home":
    st.markdown(
        """
        <p align="justify">
        CareerCrafter, the established career mentor of the new era, is a full-fledged career solution provider based in Kerala with years of satisfaction nationally and internationally. Understanding the most surging needs for directing the new generation students to a desirable career in a world of sweeping changes, we have adopted an exemplary mission of leading the students into a bright future by giving them proper direction, bolstering their confidence and instilling the power of self-esteem in them. To reinvigorate their entity and make them prepared for the competitive world We adopt various methods of aptitude tests and intensive counselling programmes. By means of exclusive career mentoring and career counselling manners Career Crafter takes up the most demanding responsibility of each student’s educational development and his career planning from the very outset with a special focus on comprehensive achievement."
        </p>
        """
        ,unsafe_allow_html=True)
if choice=="Login":
    menu2 = ["User","Admin","Company"]
    choice2 = st.sidebar.selectbox("Select Role",menu2)
    Usr=choice2
    Email = st.sidebar.text_input("Email")
    Password = st.sidebar.text_input("Password",type="password")
    b1=st.sidebar.checkbox("Login")
    if b1:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, Email):
            create_usertable()
            result = login_user(Usr,Email,Password)
            if result:
                st.success("Logged In as {}".format(Email))
                if Usr=="User":
                    menu3 = ["Profile","Build Resume","Courses","Search Job","Give Test","Ask Question","Q&A"]
                    choice3 = st.selectbox("Select",menu3)
                    if choice3=="Profile":
                        username=st.text_input("Enter Username")
                        newpassword=st.text_input("Enter New password")
                        if st.button("Change"):
                            update_pass(Email,newpassword)
                            st.text("Password Change")
                            
                    if choice3=="Build Resume":
                        menuN = ["1","2","3","4","5","6","7","8","9","10"]
                        Name=st.text_input("Your Full Name")
                        Title=st.text_input("Title For Profile")
                        Contact=st.text_input("Adress Full with No and Email")
                        choiceP = st.selectbox("No Project",menuN)
                        ProjectOneTitle=[]
                        ProjectOneDesc=[]
                        for i in range(int(choiceP)):
                            ProjectOneTitle.append(st.text_input("Project Title"+str(i)))
                            ProjectOneDesc.append(st.text_input("Prjoject Description"+str(i)))
                        choiceC = st.selectbox("No of Experiance",menuN)
                        WorkOneTitle=[]
                        WorkOneTime=[]
                        Workduration=[]
                        WorkOneDesc=[]
                        for j in range(int(choiceC)):
                            WorkOneTitle.append(st.text_input("Experiance Company Name"+str(j)))
                            WorkOneTime.append(st.text_input("DurationStart-End"+str(j)))
                            Workduration.append(st.text_input("NoYear-Month"+str(j)))
                            WorkOneDesc.append(st.text_input("Work Description"+str(j)))
                        choiceE = st.selectbox("No of Education",menuN)
                        EduOneTitle=[]
                        EduOneTime=[]
                        EduOneDesc=[]
                        Specification=[]
                        for k in range(int(choiceE)):
                            EduOneTitle.append(st.text_input("Education"+str(k)))
                            Specification.append(st.text_input("Specilization"+str(k)))
                            EduOneTime.append(st.text_input("Duration Start-End"+str(k)))
                            EduOneDesc.append(st.text_input("School/Univercity"+str(k)))
                        choiceS = st.selectbox("No of Skill",menuN)
                        SkillsDesc=[]
                        for m in range(int(choiceS)):
                            SkillsDesc.append(st.text_input("Skill Description"+str(m)))
                        choiceEX = st.selectbox("No of ExtraCurriculum",menuN)
                        ExtrasDesc=[]
                        TechSkillDesc=[]
                        for n in range(int(choiceT)):
                            TechSkillDesc.append(st.text_input("TechSkill Description"+str(n)))
                        choiceEX = st.selectbox("No of ExtraCurriculum",menuN)
                        ExtrasDesc=[]
                        for l in range(int(choiceEX)):
                            ExtrasDesc.append(st.text_input("Extra Curriculum"+str(l)))
                        if st.button("Build"):
                            resume.res(Name,Title,Contact,ProjectOneTitle,ProjectOneDesc,
                                       WorkOneTitle,WorkOneTime,WorkOneDesc,Workduration,
                                       EduOneTitle,EduOneTime,EduOneDesc,Specification,
                                       SkillsDesc,ExtrasDesc)
                            st.image("resumeexample.png")
                            #st.text(ProjectOneTitle)
                            
                    if choice3=="Courses":
                        video1 = """
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL9ooVrP1hQOE4KoZLUP4LgBwFH2IJCQs6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        """
                        st.markdown(video1,unsafe_allow_html=True)
                        video2 = """
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/LGTbdjoEBVM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        """
                        st.markdown(video2,unsafe_allow_html=True)
                        video3 = """
                        <h1>Other Online Courses</h1>
                        <a href="https://www.udemy.com/course/master-object-oriented-programming-concepts/">Master Object Oriented Programming Concepts</a>
                        <br>
                        <a href="https://www.udemy.com/course/complete-microsoft-sql-server-beginner-expert/">Microsoft SQL Crash Course for Absolute Beginners</a>
                        """
                        st.markdown(video3,unsafe_allow_html=True)
                     
                        
                    if choice3=="Search Job":
                        st.write("Search Job")
                        sj=st.text_input("Job Requirement")
                        if st.button("Search"):
                            user_result = search_job(sj)
                            clean_db = pd.DataFrame(user_result,columns=["Email","Job Title","Job Requirement","No of Position","Job Location"])
                            st.dataframe(clean_db)
                        apj=st.text_input("CompanyEmail")
                        if st.button("Apply"):
                            emaill(apj)
                            st.success("Resume Email Success")
                    if choice3=="Give Test":
                        menuT = ["OOPS","SQL"]
                        choiceT = st.selectbox("Select",menuT)
                        if choiceT=="OOPS":
                            q1=st.radio("1.Which of the following language was developed as the first purely object programming language?", 
                                     ("A.SmallTalk",
                                      "B.C++",
                                      "C.Kotlin",
                                      "D.Java"))
                            
                            q2=st.radio("2.Who developed object-oriented programming?", 
                                     ("A.Adele Goldberg",
                                      "B.Dennis Ritchie",
                                      "C.Alan Kay",
                                      "D.Andrea Ferro"))
                            
                            q3=st.radio("3.Which of the following is not an OOPS concept?", 
                                     ("A.Encapsulation",
                                      "B.Polymorphism",
                                      "C.Exception",
                                      "D.Abstraction"))
                            
                            q4=st.radio("4.Which feature of OOPS described the reusability of code?", 
                                     ("A.Abstraction",
                                      "B.Encapsulation",
                                      "C.Polymorphism",
                                      "D.Inheritance",))
                            
                            q5=st.radio("5.Which of the following language supports polymorphism but not the classes?", 
                                     ("A.C++ programming language",
                                     "B.Java programming language",
                                     "C.Ada programming language",
                                     "D.C# programming language"))
                            
                            if st.button("Submit"):
                                qqs=[q1,q2,q3,q4,q5]
                                Anss=["A.SmallTalk",
                                      "C.Alan Kay",
                                      "C.Exception",
                                      "A.Abstraction",
                                      "D.C# programming language"]
                                an=0
                                for i in range(5):
                                    if qqs[i]==Anss[i]:
                                        an=an+1
                                    else:
                                        an=an
                                st.success("You got "+str(an)+""+"/5"+"\nWrite Answer is B,C,D,A, and D")
                        
                        if choiceT=="SQL":
                            q1=st.radio("1.What is the full form of SQL?", 
                                     ("A.Structured Query List",
                                      "B.Structure Query Language",
                                      "C.Sample Query Language",
                                      "D.None of these"))
                            
                            q2=st.radio("2.Which of the following is not a valid SQL type?", 
                                     ("A.FLOAT",
                                      "B.NUMERIC",
                                      "C.DECIMAL",
                                      "D.CHARACTER"))
                            
                            q3=st.radio("3.Which of the following is not a DDL command?", 
                                     ("A.TRUNCATE",
                                      "B.ALTER",
                                      "C.CREAT",
                                      "D.UPDATE"))
                            
                            q4=st.radio("4.Which of the following are TCL commands?", 
                                     ("A.COMMIT and ROLLBACK",
                                      "B.UPDATE and TRUNCATE",
                                      "C.SELECT and INSERT",
                                      "D.GRANT and REVOKE",))
                            
                            q5=st.radio("5.Which statement is used to delete all rows in a table without having the action logged?", 
                                     ("A.DELETE",
                                     "B.REMOVE",
                                     "C.DROP",
                                     "D.TRUNCATE"))
                            
                            if st.button("Submit"):
                                qqs=[q1,q2,q3,q4,q5]
                                Anss=["A.Structured Query List",
                                      "C.DECIMAL",
                                      "C.CREAT",
                                      "D.GRANT and REVOKE",
                                      "C.DROP"]
                                an=0
                                for i in range(5):
                                    if qqs[i]==Anss[i]:
                                        an=an+1
                                    else:
                                        an=an
                                st.success("You got "+str(an)+""+"/5"+"\nWrite Answer is A,C,C,D, and C")
                            
                            
                    if choice3=="Ask Question":
                        st.text_input("Type Question")
                        if st.button('Ask'):
                            st.success("Posted")
                    if choice3=="Q&A":
                        menuQ = ["SQL","OOPS","Front end Devloper","Full Stack Devloper"]
                        choiceQ = st.selectbox("Select",menuQ)
                        if choiceQ=="SQL":
                            st.markdown(
                                """
                                <p align="justify">
                                <n>1. What is Database?</b>
                                </p>
                                <p align="justify">
                                A database is an organized collection of data, stored and retrieved digitally from a
                                remote or local computer system. Databases can be vast and complex, and such
                                databases are developed using fixed design and modeling approaches.
                                </p>
                                <b>2. What is DBMS?</b>
                                <p align="justify">
                                DBMS stands for Database Management System. DBMS is a system software
                                responsible for the creation, retrieval, updation, and management of the database. It
                                ensures that our data is consistent, organized, and is easily accessible by serving as
                                an interface between the database and its end-users or application so􀈅ware.
                                </p>
                                """
                                ,unsafe_allow_html=True)
                        if choiceQ=="OOPS":
                            st.markdown(
                                """
                                <p align="justify">
                                <b>1. What is meant by the term OOPs?</b>
                                </p>
                                <p align="justify">
                                OOPs refers to Object-Oriented Programming. It is the programming paradigm that is
                                defined using objects. Objects can be considered as real-world instances of entities
                                like class, that have some characteristics and behaviors.
                                </p>
                                <p align="justify">
                                <b>2. What is the need for OOPs?</b>
                                </p>
                                There are many reasons why OOPs is mostly preferred, but the most important
                                among them are:
                                OOPs helps users to understand the software easily, although they don’t know
                                the actual implementation.
                                With OOPs, the readability, understandability, and maintainability of the code
                                increase multifold.
                                Even very big so􀈅ware can be easily written and managed easily using OOPs.
                                </p>
                                """
                                ,unsafe_allow_html=True)
                        if choiceQ=="Front end Devloper":
                            st.markdown(
                                """
                                <p align="justify">
                                <b>1.What skills does a front-end developer need?</b>
                                </p>
                                <p align="justify">
                                Frontend developers utilize different web technologies to change coded data into
                                user-friendly interfaces. Many among these are Cascading Style Sheets (CSS),
                                JavaScript, HyperText Markup Language (HTML), etc. Mentioned below are brief
                                explanations of these technologies that frontend developers must be acquainted
                                with HTML,CSS, Java Script etc.
                                </p>
                                <b>2.Define HTML meta tags.?</b>
                                <p align="justify">
                                Meta tags are passed as pairs of name/value.
                                Meta tags can include data about encoding, document title, character
                                description, etc,
                                Meta tags fit inside the HTML page’s head tag.
                                Meta tags are not displayed on the page but it is to be shown on the browser.
                                </p>
                                """
                                ,unsafe_allow_html=True)
                        if choiceQ=="Full Stack Devloper":
                            st.markdown(
                                """
                                <p align="justify">
                                <b>1.Which language is the most preferred by full-stack developers?</b>
                                </p>
                                <p align="justify">
                                Full Stack Developers utilize several programming languages. Ideally, a candidate
                                should be fluent in several languages, preferably some for designing the front end
                                and others for fixing the back end. Since Full Stack developers work with a variety of
                                technologies and applications, they must be proficient in at least two to three of the
                                most popular languages such as Java, Python, Ruby, PHP, C++, etc.
                                </p>
                                <b>2. What is Callback Hell?</b>
                                <p align="justify">
                                Callback Hell, or Pyramid of Doom, is a common anti-pattern seen in asynchronous
                                programming code (multiple functions running at the same time). This slang term
                                describes a large number of nested "if" statements or functions. In simple terms,
                                Callback hell is a situation where you have multiple asynchronous functions. Those
                                functions depend on one another, so it could get quite messy with so many callback
                                functions nested in so many layers. The use of callback functions leaves you with
                                code that is difficult to read and maintain, and looks like a pyramid as shown below:
                                This also makes it more difficult to identify the flow of the application, which is the
                                main obstacle to debugging, which is the reason for the famous name of this
                                problem: Callback Hell.
                                </p>
                                """
                                ,unsafe_allow_html=True)
                if Usr=="Admin":
                    
                    Email1=st.text_input("Delete Email")
                    if st.button('Delete'):
                        delete_user(Email1)
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["User","FirstName","LastName","Mobile","City","Email","password","Cpassword"])
                    st.dataframe(clean_db)
                    
                if Usr=="Company":
                    menu3 = ["Add Post","Check Profiles","Ask Question"]
                    choice3 = st.selectbox("Select",menu3)
                    if choice3=="Add Post":
                        jt=st.text_input("Job Title")
                        jr=st.text_input("Job Requirement")
                        jp=st.text_input("No of Position")
                        jl=st.text_input("Job Location")
                        if st.button("OK"):
                            create_job()
                            add_job(Email,jt,jr,jp,jl)
                            st.success("Post Added")
                        jt1=st.text_input("Delete Job Title")
                        if st.button('Delete Job'):
                            delete_job(jt1)
                        user_result = view_all_job(Email)
                        clean_db = pd.DataFrame(user_result,columns=["Email","Job Title","Job Requirement","No of Position","Job Location"])
                        st.dataframe(clean_db)
                    if choice3=="Check Profiles":
                        user_result = check_prof()
                        clean_db = pd.DataFrame(user_result,columns=["User","FirstName","LastName","Mobile","City","Email","password","Cpassword"])
                        clean_db=clean_db.drop(['password','Cpassword'], axis=1)
                        st.dataframe(clean_db)
                    if choice3=="Ask Question":
                        st.text_input("Type Question")
                        if st.button('Ask'):
                            st.success("Posted")

            else:
                st.warning("Incorrect Email/Password")                
        else:
            st.warning("Not Valid Email")
                
                             
                
if choice=="SignUp":
    menu3 = ["User","Admin","Company"]
    choice3 = st.selectbox("Select Role",menu3)
    Usr=choice3
    if Usr=="Company":
        Fname = st.text_input("Company Name")
        Lname = st.text_input("Company Type")
        Mname = st.text_input("Mobile Number")
        Email = st.text_input("Email")
        City = st.text_input("City")
        Password = st.text_input("Password",type="password")
        CPassword = st.text_input("Confirm Password",type="password")
        b2=st.button("SignUp")
        if b2:
            pattern=re.compile("(0|91)?[7-9][0-9]{9}")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if Password==CPassword:
                if (pattern.match(Mname)):
                    if re.fullmatch(regex, Email):
                        create_usertable()
                        add_userdata(Usr,Fname,Lname,Mname,City,Email,Password,CPassword)
                        st.success("SignUp Success")
                        st.info("Go to Logic Section for Login")
                    else:
                        st.warning("Not Valid Email")         
                else:
                    st.warning("Not Valid Mobile Number")
            else:
                st.warning("Pass Does Not Match")
    else:    
        Fname = st.text_input("First Name")
        Lname = st.text_input("Last Name")
        Mname = st.text_input("Mobile Number")
        Email = st.text_input("Email")
        City = st.text_input("City")
        Status = st.radio("Select Gender: ",('Male', 'Female'))
        Password = st.text_input("Password",type="password")
        CPassword = st.text_input("Confirm Password",type="password")
        b2=st.button("SignUp")
        if b2:
            pattern=re.compile("(0|91)?[7-9][0-9]{9}")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if Password==CPassword:
                if (pattern.match(Mname)):
                    if re.fullmatch(regex, Email):
                        create_usertable()
                        add_userdata(Usr,Fname,Lname,Mname,City,Email,Password,CPassword)
                        st.success("SignUp Success")
                        st.info("Go to Logic Section for Login")
                    else:
                        st.warning("Not Valid Email")         
                else:
                    st.warning("Not Valid Mobile Number")
            else:
                st.warning("Pass Does Not Match")


if choice=="Contact US":
    st.subheader("Contact US Section\n\n\n")
    