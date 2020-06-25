taskkill /F /IM chrome.exe /T

cd C:\Users\Nakul\AppData\Local\Google\Chrome\User Data\Default

copy History C:\Users\Nakul\Desktop\History_1  

cd C:\Users\Nakul\Desktop

sqlite3 History_1 "select url from  urls order by last_visit_time desc limit 5 " > C:\Users\Nakul\Desktop\chrome_history.txt


to_edge.py

PAUSE