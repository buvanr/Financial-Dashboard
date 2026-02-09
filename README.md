# Financial-Dashboard

This project is an interactive dashboard that visualises a company's financial anlytics over a period of time. The long term goal is to keep updating and adding new features to this application such that it can be used by everyone. The aim of this project is to provide a simple and informatic dashboard such that beginners and experts alike can use this application to study or monitor a company's analytics. This can be to either influence their actions in a stock market/investments or to learn about a company. 

* I created this project using Python and the necessary libraries. 
* I use a Virtual Environment (venv) to keep my projects isolated from other projects to help prevent any overlap and subsequent issues. 
* I install and require pandas, streamlit and plotly.express libraries for this project to function. 
* The Key Performance Indicators (KPIs) here are: Revenue, Salay Payments, Debt, Rent, Miscellaneous Costs.
* Pandas is used to create and import a comany's data which can be used to display in the dashboard. 
* Streamlit and plotly.express libraries are used to create and display the charts and information of the company's financial analytics in the dashbaord.
* Used a line chart to display every KPI in comaprison with one other in one single place. 
* Used pie charts to display individual KPIs to show the spread of the finances across each month.  
* Combining plotly.express and streamlit made it possible for the charts shown in thedashboard to be intercative, further improving the users' experience. 

**Instructions for End User** 
    * First, we need to set up the virtual environment by typing and running 'python3 -m venv venv' in the terminal, followed by 'venv/bin/activate'.
    * Now, we install the required libraries by typing 'pip install pandas streamlit plotly' in the terminal. 
    * To finally run the application, type 'streamlit run app.py' in the terminal.
    * You can view the financial trend of a comapny over a year by interacting with the graphs. You cna zoom in and concentrate ona certain period or you can pan to view additional periods. 
    * You can also download any of the graphs available onto your device to make studying or viewing more convenient. 