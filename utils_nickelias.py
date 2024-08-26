''' ITERATION 3

Module: Elias Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this third iteration, I declare additional variables to show skills with different data types.

'''

#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Boolean variable showing if accepting new clients or not
accepting_new_clients: bool = True

# Integer variable showing number of consulting packages offered
consulting_packages: int = 3

# List showing analytic tool experience
analytic_tools: list = ["Python","Github","mySQL","Tableau","Microsoft Power BI"]

# List of floats showing daily temperature highs in Denver, CO (degrees Fahrenheit)
daily_temps: list = [95,93,88,86,90,90]


#####################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
Elias Analytics: Turning Complex Data into Clear Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Accepting New Clients:      {accepting_new_clients}
Consulting Packages:        {consulting_packages}
Analytic Tools:             {analytic_tools}
Daily Temp Highs in Denver  {daily_temps}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
   '''Return a byline for my analytics project.'''
   return byline
   
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
