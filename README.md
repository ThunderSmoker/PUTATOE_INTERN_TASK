# API Documentation

This API provides endpoints for accessing and manipulating word data.

## Endpoints

### GET /api/word

Retrieve the current word.

**Request:**

**Response:**

- Status Code: 200 OK
- Body:

```json
{
  "word": "example"
}
```

### POST /admin

Content-Type: application/x-www-form-urlencoded

**Request:**
word=new_word


**Response:**
Status Code: 200 OK