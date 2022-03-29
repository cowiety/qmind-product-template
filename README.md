# qmind-product-template

## How to run locally
First, ensure you have access to a linux shell (Mac users can use Terminal). You will also need to have pip, python, and npm installed.

1. Clone this repository to your device
2. You should use a virtual environment to keep the Python modules required for your project distinct from others on your device and avoid version issues. 
- On Mac/Linux, open your shell and navigate to a location outside of your project directory where you wish to install your Python modules
- Use the command `python3 -m venv <name_of_env>` to create your virtual environment directory
- Activate your virtual environment with the command `source <name_of_env>/bin/activate`
3. Once your virtul environment has been activated (you will need to reactivate it each time you open a new shell window), navigate to the `backend` project folder and use the command `pip install -r requirements.txt` to install the required Python modules for the project
4. Start the Django server with `python manage.py runserver`.
5. In a new window, install the frontend libraries by navigating to `frontend` and using the command `npm install`.
- If you recieve an error saying `The package-lock.json file was created with an old version of npm`, try the following:
  - Downgrade npm: `npm install -g npm@6.14.11`
  - Delete the `package-lock.json` file and the `node_modules` folder located in the `frontend` folder, then empty your trash bin
  - Type `npm -v` to ensure you are now running npm v6.14.11
  - Try `npm install` again
- If you recieve an error related to `node-sass`:
  - You must ensure your version of `node-sass` is compatible with your current version of `node`. Compatibility can be checked [here](https://www.npmjs.com/package/node-sass)
  - Known working versions of these for this project: `Node v14.16.0` with `node-sass v4.14.1`
7. Start the frontend server with `npm start`.

Navigate to `localhost:3000/` in your browser to view the app homepage. Select either of the sample projects to see what a computer vision project or dashboard project would look like (main difference lies in the "demo" tab).

If you wish to use the Django admin panel, you will first need to, again, navigate to the `backend` folder, run the command `python manage.py createsuperuser` and follow the instructions on the screen. Then, with the Django server running in the background, you can view the admin panel by navigating to `localhost:8000/admin` in your browser and logging in with your newly created credentials. This is where you can see your Django apps and their respective models (as well as their instantiations). 

## Customizing your project
If you are creating a computer vision project, please only edit the files within the `frontend/src/SampleCV` folder. Likewise, if you are creating a dashboard project, please only edit the files within the `frontend/src/SampleDashboard` folder.

First and foremost, you will want to change the name of the folder to be that of your project. Then, open the index.js file within your folder and change the component name towards the top and at the bottom of the code. Additionally, you will need to set the value of the `projectName` variable at the top of the code. Open the index.scss file and use the same projectName value at the top there as well.

You are welcome to customize your project page as much as you wish (however, please request permission before installing additional libraries!). Each "accordion" section is currently filled with placeholder data, so you will want to replace all of this with info related to your project. This includes uploading and importing headshots of your team for the "team members" tab. You may add/remove/edit accordion tabs however you'd like.

A sample chart from the Recharts library has been provided (in the "demo" tab for dashboard projects and in the "our model" tab for computer vision projects) along with a sample dataset, but you may choose to remove these if they are not needed. You can read about customization options on the Recharts website.

You will also see an example of an API call to our backend in the code, should you wish to utilize it.
