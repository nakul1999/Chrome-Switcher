import webbrowser


#register chrome

# path_to_chrome = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path_to_chrome))


#register edge

path_to_edge= r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
webbrowser.register('edge',None,webbrowser.BackgroundBrowser(path_to_edge))


#read the data file 
with open('C:/Users/Nakul/Desktop/chrome_history.txt','r') as f:
    data= f.read()
    
data = data.split('\n')

#open in the edge

for i in data:
	webbrowser.get('edge').open(i)
	
