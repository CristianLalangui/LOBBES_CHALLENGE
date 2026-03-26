# Lobbes Automation Integation 

## 📐 Architecture 

**The Project's arquitecture has the following arquitecture :**



**Components**

**1- Lobbes CRM** 

> Creates, Tasks and Logs<br>
> Stores responses of different forms<br>
> Changes the status of different tasks




**2- N8N Workflow** 

>  Has the necsary nodes to make the worflow functional <br>
>  Acts as a communication bridge between the backend and the CRM.”<br>
>  Has the logic of all the workflow, and decides which Apis calls,




**3- Backend Service** 

>  Contains the logic of emails and forms, <br>
>  Stores the tasks creted in the CRM , and the responses of the forms <br>
>  Manages the logic of the different endpoints of each API  



**4- Forms** 

>  Contains the questions  of the form <br>
>  Send the responses to the backend service

## 🔄 Workflow Logic

<u>**1. Task Initialization**<u>



Tasks are created in Lobees CRM, in order to do that we must first have some leads,
We have one parent task **Send forms** and three child tasks **Send form 1**, **Send form 2**, **Send form 3**,
each task will be ligated to a form,
n8n retrieves tasks filtered by lead email, and proceed to pass this tasks to backend service
Tasks are created in Django backend, with a id<br>
Status is reset via API, of all tasks filtered by email, in my case is **cristianalg740@gmail.com**
Once we have created the tasks we call again backend service to get tasks by Title and email, the title for 
the first task is **Send form 1**, when we get that task we procced to change the status to **In progress** 
and we will send the first form to the lead



2. Form 1 Flow

Once the lead submmits its responses of the first form, the responses will be saved in Django and n8n will recive a Json, with the information
received, but to send the second email whith the second form,  we must first filter by **interest**, if  ** interest == yes**  we change
the status of that task to **completed**, then we call backend service to get tasks stored  in our Django project, and we filter by email which
coninues being the same  and by Title, that in this case  the Title is **Send form 2**<br>after we get that task,   our backend will proceed to send the second form to the lead by email, and will change the status of the second Task, to ** In progress** 



3. Form 2 Flow
   
Once the lead submmits its responses of the second form, the responses will be saved in Django and n8n will recive a Json, with the information
received, but to send the third email with the third form, we must first filter by **proposed time**, if  ** proposed time  == yes**  we change
the status of that task to **completed**, then we call backend service to get tasks stored  in our Django project, and we filter by email which
coninues being the same  and by Title, that in this case  the Title is **Send form 3**<br>after we get task,   our backend will proceed to send the third form to the lead by email, and will change the status of the second Task, to ** Completed ** 


4. Form 3 Flow
 
Once the lead submmits its responses of the second form, the responses will be saved in Django and n8n will recive a Json, with the information
received, but to send the third email with the third form, we must first filter by **proposed time**, if  ** proposed time  == yes**  we change
the status of that task to **completed**, then we call backend service to get tasks stored  in our Django project, and we filter by email which
coninues being the same  and by Title, that in this case  the Title is **Send form 3**<br>after we get task,   our backend will proceed to send the third form to the lead by email, and will change the status of the second Task, to ** Completed ** 



## 🔗 API Endpoints



## ⚡ System Exeution<br>

**Backend Service (Django)** <br>

In order to make this work , first clone the project and open the backendLobbes directory in your computer<br>
if you haven't done it yet, 

       git clone <url-repository>
Second, create a virtual environment 

           python -m venv venv

Third,  you have to activate the  environment created

        .\venv\Scripts\activate         
           
Then, install the necesary requirements written in requirements.txt

         pip install -r requirements.txt
After that migrate to create the necesary tables in SQLite

         python manage.py migrate
         
And finally run the backend service 

         python manage.py runserver
         
##  🤖  Automation

