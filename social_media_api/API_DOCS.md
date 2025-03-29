## Like a Post
**POST** /posts/<int:pk>/like/
- Requires authentication.
- Likes a post and creates a notification.

## Unlike a Post
**POST** /posts/<int:pk>/unlike/
- Requires authentication.
- Removes a like from a post.

## Fetch Notifications
**GET** /notifications/
- Requires authentication.
- Returns a list of unread notifications.
