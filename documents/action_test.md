
| 機能             | URL パターン       | ビュー/フォームの例         |
| ---------------- | ------------------ | --------------------------- |
| ユーザー登録     | /accounts/signup/  | CreateView/UserCreationForm |
| ユーザー情報変更 | /accounts/profile/ | UpdateView/UserChangeForm   |

##### 登録
/dj-rest-auth/registration/ (POST)
http://localhost:8000/dj-rest-auth/registration/
username
password1
password2
email
responce(example)
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NjE5OTUzLCJpYXQiOjE3MTY2MTk2NTMsImp0aSI6IjdkMjI3ZDhjZmQwYTQ3NTRhODM4NmU0MjNhOTZjMjEwIiwidXNlcl9pZCI6NX0.OcQoB2dQJrn2lcmwH9mIQA7zK9K1dSY4tDvdQ-gLiRQ",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNjcwNjA1MywiaWF0IjoxNzE2NjE5NjUzLCJqdGkiOiIxZjVmZWE2Y2M4YWI0NGRkODY1ZTU4MDJjNDk4ZDE1NiIsInVzZXJfaWQiOjV9.MSW4cj2dOU0qD4zturGNmfMFEuyCtLnJpNnllqUHr5E",
    "user": {
        "pk": 5,
        "username": "user04",
        "email": "user04@email.com",
        "first_name": "",
        "last_name": ""
    }
}

##### Verify Email
/dj-rest-auth/registration/verify-email/ (POST)
http://localhost:8000/dj-rest-auth/registration/verify-email/
key

##### Re-send Email
/dj-rest-auth/registration/resend-email/ (POST)
http://localhost:8000/dj-rest-auth/registration/resend-email/

email
Resends the email verification
| 機能 | 2 | method |
| ---------------- | ------------------ | --------------------------- |
| /dj-rest-auth/registration/ (POST) | 2 | post |
| /dj-rest-auth/registration/verify-email/ (POST) | 2 | post |
| /dj-rest-auth/registration/resend-email/ (POST) | 2 | post |

