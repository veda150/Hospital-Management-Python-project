class Hospital:
  def doctor():
   print("welcome to 'GANDHI HOSPITAL' Hyderabad")
   print('Doctor Info')
   dname='Dr.Lingam '
   print('Doctor name is : ',dname)
   qualification='MBBS,RAD'
   print('Qualification : ',qualification)
   specialization='Radiology '
   print('Specialization :',specialization)
   experience='12 years'
   print('Having expirience :',experience)
class Doctor(Hospital):
  def patient():
    print('welcome to Gandhi hospitals')
    print('patient Info')
    pname='Shinchan'
    print('patient name :',pname)
    age=20
    print('age :',age)
    problem='CTS' 
    print('patient problem :',problem)
    gender='male'
    print('gender :',gender)

class Workers(Doctor,Hospital):
  def workers():
    print('welcome to Gandhi Hospital')
    print('workers Info:')
    wname='Ram'
    print('worker name :',wname)
    position='manager'
    print('position of worker :',position)
    salary=20000
    print('salary :',salary)
class coWorkers(Workers,Doctor,Hospital):
  def coworkers():
   print('welcome to Gandhi Hospitals')
   print('Cowerkers Info')
   cowname='Janani'
   print('name of coworker :',cowname)
   position='Asst.Manager'
   print('position :',position)
   salary=6000
   print('salary :',salary)

choices=[1,2,3,4]
#1=doctor,2=patient,3=worker,4=cowerker
print('Please Enter your choices Dear user  :',choices)
casevalue=int(input())
if(casevalue==1):
  d1=Hospital.doctor()
  print(d1)
elif(casevalue==2):
  d1=Doctor.patient()
  print(d1)
elif(casevalue==3):
  d1=Workers.workers() 
  print(d1)
elif(casevalue==4):
  d1=coWorkers.coworkers()
  print(d1)
else:
  print('run the existed code one more time and enter a valid choice')
print("Thank you ")
