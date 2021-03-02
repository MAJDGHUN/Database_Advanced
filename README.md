# Database_Advanced


<h1>BTC Data Scraper</h1>



<h2>Overview</h2>

*-In this task we will perform the process of scraping data from the site (https://www.blockchain.com/btc/unconfirmed-transactions). Based on this data, we will determine the most valuable Hash for Bitcoin per minute.*
<br></br>

This tool was designed in Python using the Visual Studio Code program.Several libraries were also used to complete this work, including:
<h4>BeautifulSoup, Requests, Pandas and time</h4>
<br></br>
<h2>Requirements</h2>

You can first download the Visual Studio Code program and then install the above libraries by using the following commands:


<h4>pip install BeautifulSoup</h4>
<h4>pip install Pandas</h4>
<h4>pip install Requests</h4>
<h4>pip install bs4</h4>
<h4>pip install redis</h4>
<br></br>

<h2>How to use</h2>

<h3>Step 1:</h3>
If you are working on a Linux operating system, you can do so through the command window and download the tool by using the following command:

<h4>git clone https://github.com/MAJDGHUN/Database_Advanced.git</h4>
<br></br>
<h3>Step 2:</h3>
<h4>cd Database_Advanced</h4>

<br></br>

<h3>Step 3:</h3>

After that, you must enter the tool path and give permission through the following command:
<h4>chmod +x sc.py</h4>
<h4>chmod +x redis_to_mongo.py</h4>
<h4>chmod +x run_mongo_redis.sh</h4>
<h4>chmod +x installmongo.shy</h4>
<br></br>

<br></br>
<h3>Step 4:</h3>

Before we run the Python file we have to install  MongoDB which is a general purpose, document-based, distributed database built for modern application developers and for the cloud.
Then we have to install Redis which is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.
<br></br>

To install MongoDB and redis you type the next commands:

<h4>bash installmongo.sh</h4>
<h4>bash installredis.sh</h4>


<br></br>
Now to run only the tool, we have to run the bash file "redis_to_mongo.", who will run the sc.py file and redis_to_mongo.py file.You type the following command:
<h4>bash run_mongo_redis.sh</h4>

<br></br>

<h2>Tutorials</h2>
<h4>https://www.edureka.co/blog/web-scraping-with-python/</h4>
<h4>https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer</h4>
<h4>https://www.youtube.com/watch?v=pWbMrx5rVBE&ab_channel=TraversyMedia</h4>
