# my_web_central

This app show me: weather forecast, what time my bus will be in the stop and Brazilian trending news.

The bus data is useful just for me! If you want change be aware that this data is provided by the [Brazilian transit company](http://www.sptrans.com.br/desenvolvedores/). 

It's really a personal app!

## APIs I used for this project

- [A weather API](http://apiadvisor.climatempo.com.br/doc) from a Brazillian company;
- [The NewsApi](https://newsapi.org/docs/);
- Traffic info from a [Brazilian transit company](http://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo-guia-de-referencia/). 

## How do I run it? (Not deployed yet)

This project use Flask to render the view, and for now, that's all.

So set it up is pretty simple:
- Clone this repository;
- Create a [Virtualenv](https://virtualenv.pypa.io/en/latest/) and activate it;
- Install the requirements ```pip install -r requirements.txt```
- Run the file ```app.py```

This simple app should be running!
