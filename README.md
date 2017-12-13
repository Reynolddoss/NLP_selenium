# NLP_selenium
Using the above code you can use the Natural Language Processing facility provided by IBM Watson services (Natural language understanding & Discovery News) Without using their APi
# Prerequisites
 * Python
 * firefox browser
 * Selenium library
   (Download link : http://www.seleniumhq.org/download/ )

## Walk through the code

 * Serve the msg  variable in the code with the article or the text that has to be processed.
 * Initially web_driver_load() would start up the firefox browser.
 * website_login() here the function resquires the http address of the NLU from the bluemix website.
 * wait function holds the program to pause.
 * Later sendMessage() would call the function that would place the the article into the web page text area.
 *Within this function the friver selects the text area through the source code of the page and then puts the article in the text area.
 * After which the click action is done on to process the article
 * Lastly the result are captured through the page source code and then its stored in a variable for furthur use.

## Drawbacks

 * This is applicable only till the structure of the web page remains same.
 * The driver need to be placed in path. The path of the driver needds to be copied and to be mentioned in the webdriver.firefox("path").
 
  


