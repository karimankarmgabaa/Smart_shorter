# Smart_shorter
## Overview
the task is to implement a simple api for smart link shortener service, a link shortener service like bit.ly, goo.gl and many others. with different redirection ‘destination’ URL/Link based on the users platform for example if the short link if a short link is opened for desktop web browser it will redirect to one location but if open for mobile Android for have a different location.
Imagine a App with download link when open from iOS it opens the page for the iOS app if from Android it opens the Android app download page, …etc
## Task
Implement a RESTful API for the shortlinks as documented below, not HTML or web design only JSON requests and responds. With no user authentication the API will be single user/open for all to read/write any link. Implementing user authentication is a bonus (basicAuth or OAuth2)
## REQUIREMENT
* Use MEAN Stack
* Use Flask  web framework
* Use git
* Use Python 
* git commit log is required write good commit log
* the task should be posted to Gitlab/Github and send the link
* Implement the API as documented below

* MVC, separate logic form representation,
* Use flask blueprint or app object.
## Data Schema 
### SHORT LINK SCHEMA
<pre>
slug: "s5G1f3"
ios:
  primary: "http://..."
  fallback: "http://..."
android:
  primary: "http://..."
  fallback: "http://..."
web: "http://..."
</pre>
### SHORTLINKS 
#### Example URI
<pre>
GET 127.0.0.1:5000/shortlinks
Request  "List Shortlinks"
Response  200
Response  404
Response  401
Response  500
Request  "Case Non-JSON Content-Type"
Response  400
</pre>
<pre>
Create New shortlink,

the JSON requrest below require all targts(ios,android,web) to be sent to create a new shortlink while slug is optional 
it will be genrated if not sent with the requrest this to allow for roundome alphanumiric shortlink and custome shortlink if slug was sent.
* Note
for the backend
the slug should be unique provided or auto generated
the slug is an case-sensitive alphanumeric
</pre>
### Example URI
<pre>
POST 127.0.0.1:5000/shortlinks
Request  "Create Shortlink"
Response  201

Response  404
Response  401

Response  500
Request  "Case Non-JSON Content-Type"
Response  400

</pre>
### NOTE
the slug is readonly once it’s been created, this means it can’t be update.
Only sent attr will be updated, other will stay as is
#### Example URI
<pre>
URI ParametersHide

Request  "ex: update iOS fallback only"
Request  "ex: update web only"
Response  201
Response  404
Response  401

Request  "Case Non-JSON Content-Type"
Response  400
</pre>
