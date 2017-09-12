import requests

# This is a simple script that POSTs to a Google Form to collect data
# this is the url to the Google Form
url = "https://docs.google.com/forms/d/1YyzdtjpA_bIAfaORtrL8_43aEGuy6c61U_gC9khqdN0/formResponse"

# grab the field names either from an example form, or by inspecting a POST request using
# your browser's dev tools.
r = requests.post(url, data = {"entry.1718183009":"1234"})
if r.status_code == 200:
  print "Success"
else:
  print "Unsuccessful: " + str(r.status_code)
