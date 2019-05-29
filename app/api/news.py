from newsapi import NewsApiClient

class NewsAPI:

	def __init__(self, 
				 api_key='aa7fcc75d198465a9030b81467c65f13',
				 country='br'):
		
		self.__api_key = api_key
		self.__country = country

	def top_headlines(self):

		newsapi = NewsApiClient(self.__api_key)

		top_headlines = newsapi.get_top_headlines(self.__country)

		return top_headlines


x = NewsAPI().top_headlines()

print(x)
