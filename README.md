# qmind-product-template

## How to run locally
First, ensure you have access to a linux shell (Mac users can use Terminal). You will also need to have pip, python, and npm installed.

1. Clone this repository to your device
2. Install the necessary Python modules by navigating to `backend` and using the command `pip install -r requirements.txt`. It may be a good idea to use a [virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments), and activate it with `source <venv>/bin/activate`.
3. Start the Django server with `python manage.py runserver`.
4. In a new window, install the frontend libraries by navigating to `frontend` and using the command `npm install`.
5. Start the frontend server with `npm start`.

Navigate to `localhost:3000/` in your browser to view the app homepage. Select either of the sample projects to see what a computer vision project or dashboard project would look like (main difference lies in the "demo" tab).

If you wish to use the Django admin panel, you will first need to, again, navigate to the `backend` folder, run the command `python manage.py createsuperuser` and follow the instructions on the screen. Then, with the Django server running in the background, you can view the admin panel by navigating to `localhost:8000/admin` in your browser and logging in with your newly created credentials. This is where you can see your Django apps and their respective models (as well as their instantiations). 

## Customizing your project
If you are creating a computer vision project, please only edit the files within the `frontend/src/SampleCV` folder. Likewise, if you are creating a dashboard project, please only edit the files within the `frontend/src/SampleDashboard` folder.

First and foremost, you will want to change the name of the folder to be that of your project. Then, open the index.js file within your folder and change the component name towards the top and at the bottom of the code. Additionally, you will need to set the value of the `projectName` variable at the top of the code. Open the index.scss file and use the same projectName value at the top there as well.

You are welcome to customize your project page as much as you wish (however, please request permission before installing additional libraries!). Each "accordion" section is currently filled with placeholder data, so you will want to replace all of this with info related to your project. This includes uploading and importing headshots of your team for the "team members" tab. You may add/remove/edit accordion tabs however you'd like.

A sample chart from the Recharts library has been provided (in the "demo" tab for dashboard projects and in the "our model" tab for computer vision projects) along with a sample dataset, but you may choose to remove these if they are not needed. You can read about customization options on the Recharts website.

You will also see an example of an API call to our backend in the code, should you wish to utilize it.
