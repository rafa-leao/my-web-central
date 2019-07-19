from api.news import NewsAPI


def news():

	news_headlines = NewsAPI().top_headlines()

	return [news_headlines['articles'][0],
			news_headlines['articles'][1],
			news_headlines['articles'][2],
			news_headlines['articles'][3],
			news_headlines['articles'][4]]
