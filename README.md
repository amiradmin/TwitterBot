# Twitter Mentions Collector

This app check an account id mentions and will insert the tweet details in case of "save" keyword has written in the reply message.

## Installation
### Dillinger requires Django3 to run.
#### Install packages with pip from requirements.txt file
`pip install -r requirements.txt`

### Migrate 
`Python3 manage.py migrate` 

Create an user to login to Django admin panel
`Python3 manage.py createsuperuser`

### Run Django development server
`Python3 manage.py runserver`


## Usage

Send a request to the API with the help of Postman with following link:
Http://localhost:8000/twitterapi/mention

You will get a list of mentions and also yoi csn see mentions in Django admin panel

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b develop`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin develop
5. Submit a pull request :D

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Feel Free!**