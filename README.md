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

But before we run the Python file we have to install  MongoDB which is a general purpose, document-based, distributed database built for modern application developers and for the cloud.
<br></br>
<h3>Step 4:</h3>

Firstly you have to  give permission for the installmongo.sh file by using the next command:
<h4>chmod +x installmongo.sh</h4>


<br></br>
<h3>Step 5:</h3>

To run installmongo.sh you type the next command:

<h4>bash installmongo.sh</h4>

The installmongo.sh file will install the mongoDB and the run the sc.py file automatically.
<br></br>
<h3>Notice<h3>: To run only the tool, type the following command:

<h4>python3 sc.py</h4>
<br></br>

<h2>Tutorials</h2>
<h4>https://www.edureka.co/blog/web-scraping-with-python/</h4>
<h4>https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer</h4>
