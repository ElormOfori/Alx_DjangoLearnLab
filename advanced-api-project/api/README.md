#Advanced API Project

#Overview
This project is a Django REST Framework-based API that manages books and authors. It demonstrates the use of generic views, permission classes, and nested serializers.

#API Endpoints

API Endpoints
GET /api/books/ - Retrieve all books.
POST /api/books/ - Create a new book (Authenticated users only).
GET /api/books/<id>/ - Retrieve a specific book.
PUT /api/books/<id>/ - Update a book (Authenticated users only).
DELETE /api/books/<id>/ - Delete a book (Authenticated users only).

#Books
| HTTP Method | Endpoint | Description | Permissions |
|------------|---------|-------------|-------------|
| GET | `/books/` | Retrieve all books | Public (no authentication required) |
| GET | `/books/<int:pk>/` | Retrieve a specific book by ID | Public |
| POST | `/books/create/` | Create a new book | Authenticated users only |
| PUT | `/books/<int:pk>/update/` | Update an existing book | Authenticated users only |
| DELETE | `/books/<int:pk>/delete/` | Delete a book | Authenticated users only |

#Permissions and Authentication
- The API uses Django REST Framework’s permission classes to control access.
- Unauthenticated users can read (GET) book data.
- Only authenticated users can create, update, and delete books.

#Testing the API
You can test the API using:
#Postman


