
#**Notify-Quote:**
This is a simple python script to fetch quotes from **[forismatic](http://forismatic.com/)** and display them using **notify-send**. Script is fairly simple.

API Documentation: http://forismatic.com/en/api/

#Steps to run: 
>1. Download the icon and notify-quote.py 
>2. pip install -r requirements.txt - to install required dependencies 
>3. python notify-quote.py

#Configuration
1. Two languages "English"  and "Russian" are supported, language can be configured using **lang** property in ***config.json*** to en or ru for English or Russian respectively.

2. Delay between quotes is controlled by **delay** property, specify time in seconds.

#TO DO:
>1. Offline Support by caching quotes
>2. Autostart Script



