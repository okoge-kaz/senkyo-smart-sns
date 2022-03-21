import tweepy

# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = "AAAAAAAAAAAAAAAAAAAAAAeQaQEAAAAASr0Qyy%2BxYaxyWzn%2FRnVSijrIq1w%3Dzur31oHnmnl5YSwhnw34miBfafhRnNwIhNK2sgXFIexxft32im"

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = "ponsBYm47ZeC5n7XKO3cC6tB1"
consumer_secret = "086AK3NRCtirLhx12IAbDMZBaf2qzf2RMoNM37TQC5DAaM6gWt"

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = "1330077340374872066-4AfARxxKAr2kLuJosVcJ49msTPxWaG"
access_token_secret = "ZG7c8QeSnsHc94GBL54qFeQucdIG6IarVRWZS6QEhHvoB"

# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

# # You can provide the consumer key and secret with the access token and access
# # token secret to authenticate as a user
# client = tweepy.Client(
#     consumer_key=consumer_key, consumer_secret=consumer_secret,
#     access_token=access_token, access_token_secret=access_token_secret
# )

user_id = "1330077340374872066"
# response = client.get_users_followers(user_id)

# response = client.get_users_followers(user_id, max_results=1000)
# print(response)

# print(type(client.get_users_followers(user_id)))

# follower_count = len(client.get_followed_lists(user_id))

# print(follower_count)
# print(client.get_followed_lists(user_id))

followers_list = client.get_users_followers(user_id)

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)

user = api.get_user()
print(user)
