# Summarize Text API

This Django application provides an API endpoint for summarizing text using the LangChain library and OpenAI language models.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2. Set up environment variables
    
    ``export OPENAI_API_KEY=your_openai_api_key``
## Usage

```Summarize Text Endpoint
Endpoint: /summarize/<notes_id>/

Method: GET

Request
Parameters
notes_id: ID of the note to be summarized.
Response
Success Response: 200 OK

Body:
{
  "summarized_text": "The summarized text goes here."
}

```

### Error Response: 500 Internal Server Error
``{
  "error": "Details about the error."
}``


### Add a Note:
```
* Endpoint: /post-note/

* Method: POST

* Request
* Data: Note data in the request body.
* Response
* Success Response: 201 Created

* Body: Serialized note data.
* Error Response: 400 Bad Request
* Body: Details about the validation error.
* Get a Note
* Endpoint: /get-note/<id>/

* Method: GET

* Request
* Parameters
* id: ID of the note to retrieve.
* Response
* Success Response: 200 OK
* Body: Serialized note data.
* Error Response: 404 Not Found
* Body:
* json
* Copy code
* {
*   "error": "Note not found."
* }``

```
### Update a Note
```
Update a Note
Endpoint: /put-note/<id>/

Method: PUT

Request
Parameters
id: ID of the note to update.
Data: Updated note data in the request body.
Response
Success Response: 200 OK

Body: Serialized updated note data.
Error Response: 400 Bad Request

Body: Details about the validation error.
```
### Partially Update a Note:
```
Endpoint: /patch-note/<id>/

Method: PATCH

Request
Parameters
id: ID of the note to partially update.
Data: Partially updated note data in the request body.
Response
Success Response: 200 OK

Body: Serialized partially updated note data.
Error Response: 400 Bad Request

Body: Details about the validation error.
```


### Delete a Note

```
Endpoint: /delete-note/<id>/

Method: DELETE

Request
Parameters
id: ID of the note to delete.
Response
Success Response: 204 No Content

Body: Deletion success message.
Error Response: 404 Not Found

Body:
{
  "error": "Note not found."
}
``` 
### Development
For local development, you can run the Django development server
```python manage.py runserver```

### License 

```

Make sure to replace `your_openai_api_key` in the environment variable setup with your actual OpenAI API key. Additionally, adjust the endpoints and method details as needed for your Django project.

```