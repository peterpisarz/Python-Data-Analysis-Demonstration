# Python Data Demonstration

## Data Analysis Examples using Automobile Engine Data

I've created this project to demonstrate some standard python data analysis. 

First I generated a standard pandas dataframe by prompting ChatGPT for some 
fictitious data to play around with. Imagine this data has been produced using 
sensors on an in-production vehicle or was read off a customer's car. In an 
application like this troubleshooting or fine-tuning of the car's computer might 
be necessary to troubleshoot or optimize an issue.

## Setup
1. Clone this directory to a new project folder

2. Install the requirements.txt file using pip
```bash
pip install -r requirements.txt
```

3. Run main.py

The terminal will import the code and generate a series of test, data scrubbing 
exercises and produce a plot of the RPMs over time.

## Explanation of Code

1. First the code displays the the pandas dataframe. This is useful for general 
visibility, looking at specific values and getting a high level view of what 
   you're working with
   
2. Next the code calls the getValueAtRPM() function. This is a way of finding exact 
values in the dataset. I imagine a vehicle computer engineer needing this type 
   of functionality to determine what the fuel consumption is at a given RPM. This 
   function also demonstrates an error handling case in the event you select an RPM 
   with no corresponding parameter
   
3. As a more niche use case of data manipulation, I return the values for a certain 
parameter in a given rpm range. In my specific example I want to know what RPMs 
   are producing a particular Oil Pressure (psi).
   
4. In the next case I return the average Engine Temperature across the entire 
dataset. This is a more simplified example, but it's a useful feature of pandas 
   worth demonstrating.
   
5. Determining the max() and min() Battery Voltage can also be achieved easily using 
pandas. After getting the max and min I take it one step further and get the corresponding
   RPMs associated with these values. This section also displays some form factoring 
   to make the code more human readable.
   
6. I wanted to demonstrate some more advanced uses of pandas and display knowledge of 
loops and conditional statements in my code. I decided to scan the data and find all 
   of the values for Throttle Position which are greater than 85%. Perhaps an engineer 
   would like to examine engine characteristics at these high values. The data is output 
   into a new dataframe which in turn could be analyzed further.
   
7. Next I plot the data over Time. Again I consider this to be a dataset of 
an engine's performance. I wrote a function for this particular plot feature so that 
   the input and form factor would be minimal. This increases readability and is 
   essential to consider when working on a team with other developers.
   
8. Finally I use the scikit library to show a Kmean cluster of the Fuel Consumption data. 
This data is roughly linear so there may be better options in analyzing a parameter like 
   this but I wanted to demonstrate how it would be done
   
## Future State

There are many ways to add to data analysis like this but I intended for this to be 
a brief overview of common practices. Some things to consider when expanding on this 
project could be:

1. Creating a Dashboard front end for interactive data visualization. Often this is done 
with the Plotly library. I would likely add radio buttons to toggle parameters over time. 
   In this way you could turn parameter "on and off" against others for quickly visibility. 

   
2. If the Plotly dashboard indicated that there may be correlation between certain 
parameters, you could do further in depth statistical analysis. An example of these types of 
   techniques would be either regression or classification.
   
3. Including JSON dumps for efficient data storage. Certain functions return data which 
you may want to retain for long periods of time. Utilizing JSON dumps would be a solution. 
   For example the min_v and max_v values could be stored as a JSON file alongside their
   min_v_rpm and max_v_rpm values. This is easy to do with the JSON library and makes 
   storage efficient
   
4. Integrate with a project management such as JIRA to pull data from a centralized location. 
You can interact with a tool like this using the REST API.