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
menu  = ["Home","Login","SignUp","Career Solution","Contact US"]
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
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/ugagVOu74CA?si=UOJeR86wrpJ3T3RG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        """
                        st.markdown(video1,unsafe_allow_html=True)
                        video2 = """
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/qYhrd2Lhq0g?si=smkpIZaOJ_nGQfgX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        """
                        st.markdown(video2,unsafe_allow_html=True)
                        video3 = """
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/HyU4vkZ2NB8?si=jV78VXyBMX0z0bLn" title="YouTube video player" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        """
                        st.markdown(video3,unsafe_allow_html=True)
                        video4 = """
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/1SnPKhCdlsU?si=349qOpFgJ_iDH2eP" title="YouTube video player" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        """
                        st.markdown(video4,unsafe_allow_html=True)
                        video5 = """
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/yX40xebDK68?si=nBnzhOH20Zvy1-F4" title="YouTube video player" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
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
                        menuT = ["Java","SQL","Logical Reasoning"]
                        choiceT = st.selectbox("Select",menuT)
                        if choiceT=="Java":
                                q1=st.radio("1.Which is a valid keyword in java?",
                                            ("A.interface",
                                             "B.string",
                                             "C.Float",
                                             "D.unsigned"))
                                q2=st.radio("2.Number of primitive data types in Java are?",
                                            ("A.6",
                                             "B.7",
                                             "C.8",
                                             "D.9"))
                                q3=st.radio("3.When an array is passed to a method, what does the method receive?",
                                            ("A.The referrence of the array",
                                             "B.A copy of the array",
                                             "C.Length of the array",
                                             "D.Copy of first element"))
                                q4=st.radio("4.In which of the following is toString() method defined?",
                                            ("A.java.lang.Object",
                                             "B.java.lang.String",
                                             "C.java.lang.util",
                                             "D.None"))
                                q5=st.radio("5.Find the output of the following code.int ++a = 100;System.out.println(++a);",
                                            ("A.101",
                                             "B.Compile error",
                                             "C.100",
                                             "D.None"))
                                
                                if st.button("Submit"):
                                    qqs=[q1,q2,q3,q4,q5]
                                    Anss=["B.string",
                                          "C.8",
                                          "A.The referrence of the array",
                                          "A.java.lang.Object",
                                          "B.Compile error"]
                                    an=0
                                    for i in range(5):
                                        if qqs[i]==Anss[i]:
                                            an=an+1
                                        else:
                                            an=an
                                    st.success("You got "+str(an)+""+"/5"+"\nRight Answer is B,C,A,A, and B")
                                    
                                    
                                    
                        if choiceT=="SQL":
                                  q1=st.radio("1.What command is used to create a new table in SQL?",
                                                    ("A.CREATE TABLE",
                                                     "B.BUILD TABLE",
                                                     "C.GENERATE TABLE",
                                                     "D.NONE OF ABOVE"))
                                  q2=st.radio("2.Which of the following commands is used to delete all rows and free up space from a table?",
                                                    ("A.TRUNCATE",
                                                     "B.DROP",
                                                     "C.DELETE",
                                                     "D.ALTER"))
                                  q3=st.radio("3.Which of the following is the full form of DDL?",
                                                    ("A.Data Definition Language",
                                                     "B.Data Derivation Language",
                                                     "C.Dynamic Data Language",
                                                     "D.Detailed Data Language"))
                                  q4=st.radio("4._______ clause creates temporary relation for the query on which it is defined",
                                              ("A.WITH",
                                               "B.FROM",
                                               "C.WHERE",
                                               "D.SELECT"))
                                  q5=st.radio("5.What is the difference between a PRIMARY KEY and a UNIQUE KEY?",
                                              ("A.Primary key can store null value, whereas a unique key cannot store null value",
                                               "B.We can have only one primary key in a table while we can have multiple unique keys",
                                               "C.Primary key cannot be a date variable whereas unique key can be",
                                               "D.None of these"))
                                  
                                  if st.button("Submit"):
                                      qqs=[q1,q2,q3,q4,q5]
                                      Anss=["A.CREATE TABLE",
                                            "C.DELETE",
                                            "A.Data Definition Language",
                                            "A.WITH",
                                            "B.We can have only one primary key in a table while we can have multiple unique keys"]
                                      
                                      an=0
                                      for i in range(5):
                                          if qqs[i]==Anss[i]:
                                              an=an+1
                                          else:
                                              an=an
                                      st.success("You got "+str(an)+""+"/5"+"\nRight Answer is A,C,A,A, and B")
                                      
                                      
                        if choiceT=="Logical Reasoning":
                                q1=st.radio("1.Which of the following propositions is tautology?",
                                            ("A.(p v q)→q",
                                             "B.p v (q→p)",
                                             "C.p v (p→q)",
                                             "D.Both (b) & (c)"))
                                q2=st.radio("2.What is the next number in the sequence?"
                                            "1, 4, 9, 16, ?",
                                            ("A) 25",
                                             "B) 36",
                                             "C) 49",
                                             "D) 64"))
                                q3=st.radio("3.The shadow of a pole 6 metre high is 15 metre long and at the same time the shadow of a tree is 25 metre long. What is the height of the tree?",
                                            ("A.21 m",
                                             "B.10 m",
                                             "C.35 m",
                                             "D.None of the above"))
                                q4=st.radio("4.The length of shadow of a tree is 16 m when the angle of elevation of the sun is 60°. What is the height of the tree?",
                                            ("A.8 m",
                                             "B.16 m",
                                             "C.32 m",
                                             "D.64 m"))
                                q5=st.radio("5.If in a race of 80m, A covers the distance in 20 seconds and B in 25 seconds, then A beats B by:",
                                            ("A) 20 m",
                                             "B) 16 m",
                                             "C) 11 m",
                                             "D) 10 m"))
                                
                                if st.button("Submit"):
                                    qqs=[q1,q2,q3,q4,q5]
                                    Anss=["C.p v (p→q)",
                                          "A.25",
                                          "C.35 m",
                                          "C.32 m",
                                          "A.20 m"]
                                    
                                    an=0
                                    for i in range(5):
                                        if qqs[i]==Anss[i]:
                                            an=an+1
                                        else:
                                            an=an
                                    st.success("You got "+str(an)+""+"/5"+"\nRight Answer is C,A,C,C, and A")
                                    
                                    
                            
                            
                    if choice3=="Ask Question":
                        st.text_input("Type Question")
                        if st.button('Ask'):
                            st.success("Posted")
                     if choice3=="Q&A":
                       menuQ = ["SQL","Python","OOPS","IOT"]
                       choiceQ = st.selectbox("Select",menuQ)
                       if choiceQ=="SQL":
                           st.markdown(
                               """
                               <p align="justify">
                               <b>1. What is Database?</b>
                               </p>
                               <p align="justify">
                               A database is a structured collection of data that is organized and stored electronically
                               in a computer system. It is designed to efficiently manage, store, retrieve, and
                               manipulate data according to predefined criteria and requirements. Databases are fundamental
                               components of information systems and are widely used in various applications, ranging from
                               simple personal data management to large-scale enterprise systems.
                               </p>
                               <b>2. What is the purpose of a primary key in a database table?</b>
                               </p>
                               <p align="justify">
                               The primary key uniquely identifies each record in the table and ensures data integrity
                               by preventing duplicate or null values in the key columns.
                               </p>
                               <b>3. What does the 'select' statement do?</b>
                               </p>
                               <p align="justify">
                               The SELECT statement retrieves data from one or more tables in a database based on 
                               specified criteria and returns the result set of rows that match the criteria.
                               </p>
                               <b>4. What is the purpose of the SQL 'JOIN' keyword?</b>
                               </p>
                               <p align="justify">
                               The JOIN keyword is used to combine rows from two or more tables based on a related
                               column between them, allowing data from different tables to be retrieved together
                               in a single result set.
                               </p>
                               <b>5. What does the SQL 'GROUP BY' clause do?</b>
                               </p>
                               <p align="justify">
                               The GROUP BY clause is used to group rows that have the same values into summary
                               rows, typically to perform aggregate functions like 'SUM', 'COUNT', 'AVG', etc.,
                               on each group.
                               """
                              ,unsafe_allow_html=True)
                           
                       if choiceQ=="Python":
                             st.markdown(
                                 """
                                 <p align="justify">
                                 <b>1. What is Python?</b>
                                 </p>
                                 <p align="justify">
                                 Python is an interpreted scripting language that is known for its power,
                                 interactivity, and object-oriented nature. It utilizes English keywords extensively
                                 and has a simpler syntax compared to many other programming languages.
                                 </p>
                                 <b>2. What is pep 8?
                                 </p>
                                 <p align="justify">
                                 PEP in Python stands for Python Enhancement Proposal. It comprises a collection
                                 of guidelines that outline the optimal approach for crafting and structuring Python
                                 code to ensure the utmost clarity and legibility.
                                 </p>
                                 <b>3.What is a dictionary in Python?
                                 </p>
                                 <p align="justify">
                                 Python supports various data types, including dictionaries. A dictionary in Python
                                 is a collection of elements that are stored as key-value pairs. It is an unordered
                                 data structure, and the indexing is done based on the keys assigned to each element.
                                 Let’s consider an example: we have a dictionary named ‘dict’ with two keys, ‘Country’
                                 and ‘Capital’, which have corresponding values ‘India’ and ‘New Delhi’, respectively.
                                 """
                                 ,unsafe_allow_html=True)
                         
             
                       if choiceQ=="OOPS":
                             st.markdown(
                                 """
                                 <p align="justify">
                                 <b>1.  What is Object Oriented Programming (OOPs)?</b>
                                 </p>
                                 <p align="justify">
                                 Object Oriented Programming (also known as OOPs) is a programming paradigm where the complete
                                 software operates as a bunch of objects talking to each other. An object is a collection of
                                 data and the methods which operate on that data. 
                                 </p>
                                 <b>2. What is a Class?
                                 </p>
                                 <p align="justify">
                                 A class is a building block of Object Oriented Programs. It is a user-defined data type that
                                 contains the data members and member functions that operate on the data members. It is like a
                                 blueprint or template of objects having common properties and methods.
                                 </p>
                                 <b>3.  What is the difference between overloading and overriding?
                                 </p>
                                 <p align="justify">
                                 A compile-time polymorphism feature called overloading allows an entity to have numerous
                                 implementations of the same name. Method overloading and operator overloading are two examples.
                                 
                                 Overriding is a form of runtime polymorphism where an entity with the same name but a different
                                 implementation is executed. It is implemented with the help of virtual functions.
                                 </p>
                                 <b>4.  What different types of inheritance are there?
                                 </p>
                                 <p align="justify">
                                 Inheritance can be classified into 5 types which are as follows:\n
                                    1. <b>Single Inheritance</b>: Child class derived directly from the base class.\n
                                    2. <b>Multiple Inheritance</b>: Child class derived from multiple base classes.\n
                                    3. <b>Multilevel Inheritance</b>: Child class derived from the class which is also derived from another base class.\n
                                    4. <b>Hierarchical Inheritance</b>: Multiple child classes derived from a single base class.\n
                                    5. <b>Hybrid Inheritance</b>: Inheritance consisting of multiple inheritance types of the above specified.
                                 </p>
                                 <b>5. What is Inheritance?
                                 </p>
                                 <p align="justify">
                                 Inheritance is one of the major features of object-oriented programming, by which an entity inherits
                                 some characteristics and behaviors of some other entity and makes them their own. Inheritance helps to
                                 improve and facilitate code reuse.
                                 The various types of inheritance include:\n
                                 Single Inheritance\n
                                 Multiple Inheritance\n
                                 Multilevel Inheritance\n
                                 Hierarchical Inheritance\n
                                 Hybrid Inheritance
                                 """
                                 ,unsafe_allow_html=True) 

                       if choiceQ=="IOT":
                             st.markdown(
                                 """
                                 <p align="justify">
                                 <b>1. What is IoT?
                                 </p>
                                 <p align="justify">
                                 IoT refers to the internet of things. It is a system of interrelated physical devices that are each
                                 assigned a unique identifier. IoT extends internet connectivity beyond traditional platforms, such
                                 as PCs, laptops and mobile phones.
                                 </p>
                                 <b>2.  What is meant by a smart city in IoT?
                                 </p>
                                 <p align="justify">
                                 A smart city is an urban area that uses IoT technologies to connect city services and enhance their
                                 delivery. Smart cities can help reduce crime, optimize public transportation, improve air quality,
                                 streamline traffic flow, lower energy use, manage infrastructure, reduce health risks, simplify parking,
                                 manage utilities and improve a variety of other processes. Using sensor-driven data collection, the
                                 smart city can orchestrate and automate a wide range of services, while reducing costs and making those
                                 services easier to access for more people.
                                 </p>
                                 <b>3. What are the main components of the IoT architecture?
                                 </p>
                                 <p align="justify">
                                 The IoT architecture consists of the following components:\n
                                 * <b>Smart devices</b>: Include embedded systems for carrying out tasks such as collecting and transmitting
                                 data or responding to commands from external control and management systems.
                                 * <b>Data processing platforms</b>: Include the hardware and software necessary to process and analyze the
                                 data coming in over the network from the IoT devices.
                                 * <b>Storage platforms</b>: Manage and store the data and interface with the data processing platform to
                                 support its operations.
                                 * <b>Network infrastructure</b>: Facilitates communications between the devices and the data processing and
                                 storage platforms.
                                 * <b>UI</b>: Enables individuals to connect directly to IoT devices to configure and manage them, as well
                                 as verify their status and troubleshoot them.
                                 </p>
                                 <b>4. Explain the meaning of Arduino.
                                 </p>
                                 <p align="justify">
                                 Arduino is an open-source platform for building electronics projects using easy-to-use hardware and software.
                                 A microcontroller is the common feature of all Arduino boards. The microcontrollers on board are capable of 
                                 reading inputs (e.g., light on a sensor, an object near a sensor) and converting them to outputs
                                 (drive a motor, ring an alarm, turn on an LED, display information on an LCD). It is possible to connect multiple
                                 devices and exchange data in real-time between them. It is also possible to monitor them remotely using a simple
                                 interface.
                                 </p>
                                 <b>5. What do you mean by Raspberry Pi?
                                 </p>
                                 <p align="justify">
                                 Raspberry Pi is a card-sized computer with features like General Purpose Input Output (GPIO) pins, WiFi,
                                 and Bluetooth that allow it to communicate, control, and connect to other external devices. Combining IoT
                                 applications with Raspberry Pi helps businesses embrace technology more effectively.
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
                
if choice=="Career Solution":
    crmenu  = ["Java","python",".net","Android","PHP"]
    choice = st.selectbox("Select Your Choise",crmenu)
    if choice=="Java":
      Status=st.radio("Select Course: ", ("Java Developer", "Database Administrator","Mobile Developer","Front-end Developer"))
      if Status=="Java Developer":
          st.text("A Java developer is a software engineering professional who develops and maintains")
          st.text ("programming.This may include writing and testing code, analysing software, ensuring")
          st.text (" applications comply with industry standards and presenting development reports to")
          st.text (" other departments in a company. ")
      if Status=="Database Administrator":
          st.text(" A database administrator oversees the maintenance and security procedures of")
          st.text(" an organisation's databases.Their duties include assessing and upgrading malware")
          st.text("protection programs to avoid potential security breaches, creating accounts for") 
          st.text("authorised individuals to access databases and organising databases so employees")
          st.text("can find important documents quickly and accurately. ")
      if Status=="Mobile Developer":
          st.text("They collaborate with back-end developers to formulate robust architectures for") 
          st.text("solutions.These professionals also work with computer engineers to promote ideas")
          st.text(" for unique applications.")
      if Status=="Front-end Developer":
          st.text(" They follow web design principles to render a company's website well across devices.")
          st.text("They design frameworks for user applications and improve them routinely to fulfil")
          st.text("the growing requirements of an organisation.These developers analyse the performance")
          st.text(" of websites, monitor site traffic variations, identify traffic issues and rectify")
          st.text("them.")
          
    if choice=="python":
      Status=st.radio("Select Course: ", ("Python Developer", "Data Analyst", "Data Scientist", "Cybersecurity Specialist"))
      if Status=="Python Developer":
          st.text("As a Python developer, you would be responsible for writing, testing, and debugging")
          st.text("code using Python.You would work on various projects such as web applications,")
          st.text("data analytics, scientific computing, and machine learning.To become a Python")
          st.text("developer, you should have a strong understanding of Python syntax and libraries")
          st.text("as well as proficiency in software development tools and methodologies.")
      if Status=="Data Analyst":
          st.text("Python is widely used in data analysis due to its powerful libraries such as NumPy,")
          st.text("Pandas, and Matplotlib.As a data analyst, you would use Python to collect, clean,")
          st.text("and analyze large amounts of data. Data analyst requires a strong understanding of")
          st.text("statistical concepts, as well as proficiency in data visualization and analysis tools.")
      if Status=="Data Scientist":
          st.text("A Data Scientist in a Python career is a professional who utilizes Python programming")
          st.text("skills and statistical knowledge to extract insights and make data-driven decisions.")
          st.text("It Perform data cleaning and preprocessing using Python, handling missing values,")
          st.text("outliers, and data inconsistencies.")
      if Status=="Cybersecurity Specialist":
          st.text("As a cybersecurity specialist, you would use Python to automate security tasks and")
          st.text("scripts, such as vulnerability scanning and penetration testing.You would work on")
          st.text("various projects such as network security, application security, and cloud security.")
          
          
    if choice==".net":
        Status=st.radio("Select Course: ", (".net Developer", "Full-stack Developer", "Back-end Developer", "Software Developer"))
        if Status==".net Developer":
            st.text("NET developer is an information technology professional who uses the . NET Microsoft")
            st.text("framework to design and maintain software and applications.They collaborate with")
            st.text("computer scientists, other web developers and clients to create a user-friendly,")
            st.text("scalable application.The .Net infrastructure features various tools, libraries,")
            st.text("and frameworks that help broaden the scope of this beneficial software")
            st.text("development platform.")
        if Status=="Full-stack Developer":
            st.text("Full Stack Developers build web applications for both the visible front end")
            st.text("that users see and the back end that powers the applications.Full Stack")
            st.text("Developers can work alone but often work on a team with Front End and")
            st.text("or Back End Developers as well as Designers.They should know the basic")
            st.text("front end web languages like HTML, CSS, and JavaScript as well as back")
            st.text("end technologies like server configuration, databases, SQL, and Python.")
            st.text("Each workplace will have its own process but understanding scrum,")
            st.text("whiteboarding, the software development lifecycle, and soft skills")
            st.text("like teamwork will be helpful.")
        if Status=="Back-end Developer":
            st.text("A back-end developer builds and maintains the mechanisms that process")
            st.text("data and perform actions on websites. They are responsible for a site's")
            st.text("structure, system, data, and logic.Back-end developers need to have a")
            st.text("passing familiarity with, if not command of, several technical languages")
            st.text("and programs.")
        if Status=="Software Developer":
            st.text("Software developers create the computer applications that allow users to")
            st.text("do specific tasks and the underlying systems that run the devices or")
            st.text("control networks. These workers must be able to give clear instructions")
            st.text("and explain problems that arise to other team members involved in development.")
            
            
    if choice=="Android":
        Status=st.radio("Select Course: ", ("Android App Developer", "Freelance Developer", "Mobile Lead Software Engineer"))
        if Status=="Android App Developer":
            st.text("An android developer is a software developer proficient in creating")
            st.text("software applications for mobile devices such as mobile phones and")
            st.text("tablets, which run on the Android operating system.The android")
            st.text("development process involves creating software code, implementing")
            st.text("backend services, and testing the application on mobile devices.")
        if Status=="Freelance Developer":
            st.text("Freelance Android developers work independently or on a contract")
            st.text("basis, developing applications for clients or working on their own")
            st.text("projects. This option offers flexibility and the opportunity to")
            st.text("work on a variety of projects.")
        if Status=="Mobile Lead Software Engineer":
            st.text("A Mobile Lead Software Engineer is a professional who specializes in")
            st.text("developing software applications specifically for mobile devices such")
            st.text("as smartphones and tablets.It can Leading the technical design and")
            st.text("architecture of mobile applications.Staying current with mobile")
            st.text("development trends, tools, and technologies.Managing the release process,")
            st.text("including deployment to app stores and ongoing maintenance updates.")
            
            
    if choice=="PHP":
        Status=st.radio("Select Course: ", ("Web Developer", "Graphic Designer", "php Developer"))
        if Status=="Web Developer":
            st.text(" PHP is commonly used in web development, so becoming a web developer")
            st.text("specializing in PHP can be a lucrative career path.You would work on")
            st.text("creating dynamic websites and web applications using PHP along with")
            st.text("other web technologies like HTML, CSS, and JavaScript.")
        if Status=="Graphic Designer":
            st.text("Graphic Designers are the ones who make digital visuals aesthetically")
            st.text("appealing. Another significant future scope of PHP is the Graphic")
            st.text("Designer job. Their task involves creating attractive graphics for")
            st.text("digital content. Adobe Dreamweaver is an excellent tool for web designing.")
        if Status=="php Developer":
            st.text("PHP developers develop programs, applications, and web sites using the")
            st.text("dynamic scripting language PHP.PHP is known for web development and")
            st.text("business applications. Depending on job function, PHP developers may")
            st.text("be classified as software developers or web developers.PHP developer")
            st.text("skills are abilities you can utilize as a web developer specializing")
            st.text("in using PHP to write code for server-side applications.")
        
      
    





                    
if choice=="Contact US":
    st.text("CONTACT INFO:")
    st.image("contact.png")
    st.subheader("9537452279")
    st.image("mailbox.png")
    st.subheader("careercraft@gmail.com")
                    


