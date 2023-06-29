# sqlalchemy-challenge

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

Part 1: Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib.

For this part the most recent date in the data set was identified. From there a precipitation analysis was completed starting with the daily precipitation totals in inches was plotted in a bar graph covering the period of one calendar year immediately preceeding the most recent date identified in the data set. Next, using the data set, a table was created that provides the dataset count, mean, std dev, min, 25%, 50%, 75% and max data points.

Next the weather stations were looked at. First, a count of the number of weather stations was completed. From there the most active stations were identified, and from this list, the data from the most active station was reviewed to provide the lowest and highest recorded temperatures, as well as the average temperature at that station for the dataset. Finally, to visualize the temperature history, a bar chart was plotted show the frequency of temperatures throughout the year.

Part 2: Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed.

An app was built called ClimateApp.py to all for quick view of all data, and specific data points for temperature and precipitation. Based on the route copied you can view the daily precipitation, daily temperature, weather station identification and min, max and avg temperature based on either a specific dated YYYY-MM-DD (i.e. 2016-08-23) or over a period of time YYYY-MM-DD to YYYY-MM-DD (i.e. 2016-08-23/2016-08-31). When copying the route for the specific date or over period of time, be sure to replace the last bit o f the address with the desired date(s) as formatted in the previous sentence.

In order to complete this challenge teaching materials, and in class examples were utilized. Additionally, the instructor provided outside resources that were helpful in further understanding what was needed to complete the assignment; those resources included: https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_declaring_mapping.htm, https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/. Finally, I again utilized https://codepal.ai/code-reviewer to assit in troubleshooting errors.
