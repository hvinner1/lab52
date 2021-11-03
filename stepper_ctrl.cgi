#!/usr/bin/python37all
import cgi
import json
import cgitb
cgitb.enable()

data = cgi.FieldStorage()

#json code
ang = data.getvalue('angle')
change = data.getvalue('change') #change
Zero = data.getvalue('Zero')
#do we need to getvalue from each button
data = {"angle":ang, "change":change, "Zero":Zero}
with open('lab4.txt', 'w') as f:
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('''
<html>
<form action="/cgi-bin/step.py" method="POST">
  <input type="range" id="angle" name="angle" min="0" max="360">
  <label for="angle">Angle</angle><br>
  <br>
  <input type="submit" value="Change Angle" name="change"> 
  <input type="submit" value="Zero" name="Zero"><br>
  <br>
</form>
<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550818/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&xaxis=time&yaxis=motor+angle"></iframe><br>
<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550818/widgets/372978"></iframe>
</html>
''')