def res(Name,Title,Contact,
        ProjectOneTitle,ProjectOneDesc,
        WorkOneTitle,WorkOneTime,WorkOneDesc,Workduration,
        EduOneTitle,EduOneTime,EduOneDesc,Specification,
        SkillsDesc,
        ExtrasDesc):
    # Text Variables
    Header = '>>>This resume was generated Team JobPortal'
    ProjectsHeader = 'PROJECTS/PUBLICATIONS'
    WorkHeader = 'EXPERIENCE'
    EduHeader = 'EDUCATION'
    SkillsHeader = 'Skills'
    ExtrasTitle = 'Extra Curriculum'
    # Setting style for bar graphs
    import matplotlib.pyplot as plt
    
    # set font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'STIXGeneral'
    
    fig, ax = plt.subplots(figsize=(8.5, 11))
    
    # Decorative Lines
    ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
    plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
    plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
    
    # set background color
    ax.set_facecolor('white')
    
    # remove axes
    plt.axis('off')
    
    # add text
    plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.6)
    plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
    plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
    plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='#ffffff')
    
    plt.annotate(ProjectsHeader, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
    for i in range(len(ProjectOneTitle)):
        plt.annotate(ProjectOneTitle[i], (.02,.830-i*.04), weight='bold', fontsize=10)
        plt.annotate(ProjectOneDesc[i], (.04,.810-i*.04), weight='regular', fontsize=9)
    
    
    plt.annotate(WorkHeader, (.02,.54), weight='bold', fontsize=10, color='#58C1B2')
    for i in range(len(WorkOneTitle)):
        plt.annotate(WorkOneTitle[i], (.02,.508-i*.04), weight='bold', fontsize=10)
        plt.annotate(WorkOneTime[i], (.25,.508-i*.04), weight='regular', fontsize=9, alpha=.6)
        plt.annotate(Workduration[i], (.50,.508-i*.04), weight='regular', fontsize=9, alpha=.6)
        plt.annotate(WorkOneDesc[i], (.04,.490-i*.04), weight='regular', fontsize=9)
    
    plt.annotate(EduHeader, (.02,.185), weight='bold', fontsize=10, color='#58C1B2')
    for i in range(len(EduOneTitle)):
        plt.annotate(EduOneTitle[i], (.02,.155-i*.08), weight='bold', fontsize=10)
        plt.annotate(Specification[i], (.02,.140-i*.08), weight='regular', fontsize=9)
        plt.annotate(EduOneDesc[i], (.02,.120-i*.08), weight='regular', fontsize=10)
        plt.annotate(EduOneTime[i], (.02,.100-i*.08), weight='regular', fontsize=9, alpha=.6)
    
    
    
    plt.annotate(SkillsHeader, (.7,.8), weight='bold', fontsize=10, color='#ffffff')
    for i in range(len(SkillsDesc)):
        plt.annotate(SkillsDesc[i], (.7,.78-i*.02), weight='regular', fontsize=10, color='#ffffff')
    
    plt.annotate(ExtrasTitle, (.7,.43), weight='bold', fontsize=10, color='#ffffff')
    for i in range(len(ExtrasDesc)):
        plt.annotate(ExtrasDesc[i], (.7,.41-i*.02), weight='regular', fontsize=10, color='#ffffff')
    
    plt.savefig('resumeexample.png', dpi=300, bbox_inches='tight')
def emaill(email):
    # Python code to illustrate Sending mail with attachments
    # from your Gmail account 
    # libraries to be imported
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders  
    fromaddr = "test@test.com"
    toaddr = email
       
    # instance of MIMEMultipart
    msg = MIMEMultipart()
      
    # storing the senders email address  
    msg['From'] = fromaddr
      
    # storing the receivers email address 
    msg['To'] = toaddr
      
    # storing the subject 
    msg['Subject'] = "Applied For Job"
      
    # string to store the body of the mail
    body = "Find Attachment For Resume"
      
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
      
    # open the file to be sent 
    filename = "resumeexample.png"
    attachment = open(filename, "rb")
      
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
      
    # To change the payload into encoded form
    p.set_payload((attachment).read())
      
    # encode into base64
    encoders.encode_base64(p)
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
      
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
      
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
      
    # start TLS for security
    s.starttls()
      
    # Authentication
    s.login(fromaddr, "12345")
      
    # Converts the Multipart msg into a string
    text = msg.as_string()
      
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
      
    # terminating the session
    s.quit()