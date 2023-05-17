from fastapi import FastAPI,HTTPException
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schema.models import Student, EmailClass
from core.db.mongo_db import Connection
from constants.agg_cons import agg_store

conn = Connection()

class Crud:
    def create(self,student: Student):
        conn.lib.insert_one(student.dict())
        return {"message": "Data inserted successfully"}

    def get_all_data(self):
        students =  conn.lib.find({})
        details = []
        for document in students:
            detail = {'name':document['name'],'registration_no':document['registration_no'],'course_id':document['course_id'],'course_name':document['course_name']}
            details.append(detail)
        return {"details":details}

    def update(self,id:int,student: Student):
        
        conn.lib.update_one({"registration_no": id}, {"$set": student.dict()})
        return {"message": "Student data updated successfully!"}

        
    def delete(self,id:int):
        conn.lib.delete_one({'registration_no':id})
        return {"message": "Student record deleted successfully"}
    
    def aggregate(self):
        a = conn.lib.aggregate(agg_store)
        a_list = list(a)
        return a_list[0]["totalprice"]
     
    

    def send_email(self,data: EmailClass):
        # Set up the email details
        sender_email = "this.is.priyanka30@gmail.com"
        sender_password = "xaqmxsruanrubwms"
        receiver_email = data.rec_email
    

    # Create a multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = data.subject
        
        body = self.aggregate()
        body=str(body)
    # Add the body to the email
        message.attach(MIMEText("Total course fee is: "+body, "plain"))

        try:
            # Create a secure connection to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Login to the sender's email account
            server.login(sender_email, sender_password)
            
            # Send the email
            server.send_message(message)

            # Close the connection
            server.quit()

            return {"message": "Email sent successfully"}
        
        except Exception as e:
            return {"message": str(e)}


    