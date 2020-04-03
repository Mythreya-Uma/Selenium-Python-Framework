from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com")
driver.maximize_window()
Comments: Working as Expected

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

Comments: Logs for the State Fin_Wait_2
    TCP    127.0.0.1:12871        view-localhost:52651   FIN_WAIT_2
    TCP    127.0.0.1:52651        view-localhost:12871   CLOSE_WAIT
        
DevTools listening on ws://127.0.0.1:12871/devtools/browser/46c0575e-bff3-470e-a78b-ff5d08cb80a3
Traceback (most recent call last):
  File "firsttest.py", line 5, in <module>
    driver.maximize_window()
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python37-32\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 737, in maximize_window
    self.execute(command, params)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python37-32\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python37-32\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: cannot get automation extension
from unknown error: page could not be found: chrome-extension://aapnijgdinlhnhlmodcfapnahmbfebeb/_generated_background_page.html
  (Session info: chrome=80.0.3987.149)
  (Driver info: chromedriver=2.24.417431 (9aea000394714d2fbb20850021f6204f2256b9cf),platform=Windows NT 10.0.18362 x86_64)

   Observations: driver.maximize_window() is not listening to the localhost port and established the connections.
   Fix for the original code will be provided tommorow EOD.(04-04-2020)
   workaround: try installing new automation extension for the chrome selenium webdriver. Expections not occuring.
   
