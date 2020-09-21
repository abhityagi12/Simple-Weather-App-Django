from django.shortcuts import render
import json
import urllib.request
# from django.http import HttpResponse
# Create your views here.


# def get_html_content(city):
# 	import requests
# 	USER_AGENT = "Mozilla/5.0 (X11; Linux X86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# 	LANGUAGE = "en-US,en;q=0.5"
# 	session=requests.Session()
# 	session.headers['User-Agent']=USER_AGENT
# 	session.headers['Accept-Language']=LANGUAGE
# 	session.headers['Content-Language']=LANGUAGE
# 	city=city.replace(' ','+')
# 	html_content=session.get(f'https://www.google.com/search?q=weather+in+{city}').text
# 	return html_content


def home(request):
	if request.method=='POST':
		city=request.POST['city']

		source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=3877cbe1793329268e6b187df4db633d').read() 

		# source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q ='+ city + '&appid =3877cbe1793329268e6b187df4db633d').read()
		list_of_data=json.loads(source)
		data={
			'city_name':str(list_of_data['name']),
			'country_code':str(list_of_data['sys']['country']),
			'temp':str(int((list_of_data['main']['temp']-32)*5/9))+'° C',
			'pressure':str(list_of_data['main']['pressure']),
			'humidity':str(list_of_data['main']['humidity']),
		}
	else:
		data={}
		
	# weather_data=None
	# if 'city' in request.GET:
	# 	#fetch weather data
	# 	city=request.GET.get('city')
	# 	html_content=get_html_content(city)
	# 	from bs4 import BeautifulSoup
	# 	soup=BeautifulSoup(html_content,'html.parser')
	# 	weather_data=dict()
	# 	weather_data['region']=soup.find('div', attrs={'id': 'wob_loc'}).text
	# 	weather_data['daytime']=soup.find('div', attrs={'id': 'wob_dts'}).text
	# 	weather_data['status']=soup.find('div', attrs={'id': 'wob_dcp'}).text
	# 	weather_data['temp']=soup.find('span', attrs={'id': 'wob_tm'}).text
	return render(request, 'core/home.html', {'weather':data})

	