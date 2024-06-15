### django_dj_rest_auth_tasks
- django + dj_rest_auth + JWT を使う上でのポイントは、カスタムユーザを作ることです。
- （これに尽きるかなあ）
##### 機能
- 認証　JWT(Json Web Token) Token認証
- アプリ（例）Todo_tasksアプリ　API利用（作成中）
### todo_task: API一覧
| 機能名                           | エンドポイント                | メソッド      | 入力                                                                         | 出力                                                                                               | Note                                                   |
|----------------------------------|------------------------------|--------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| ログイン                         | /dj-rest-auth/login/         | POST         | username, password                                                           | key                                                                                               | 認証が必要                                             |
| ログアウト                       | /dj-rest-auth/logout/        | POST         |                                                                              |                                                                                                    | 認証が必要                                             |
| タスクの作成                     | /api/tasks/                  | POST         | title, description, due_date                                                 | id, title, description, due_date, completed, created_at, updated_at                                | 認証が必要                                             |
| タスクの一覧取得（全てのタスク） | /api/tasks/                  | GET          |                                                                              | [ {id, title, description, due_date, completed, created_at, updated_at}, ... ]                     | 認証が必要                                             |
| タスクの一覧取得（ユーザーごと） | /api/tasks/user/             | GET          |                                                                              | [ {id, title, description, due_date, completed, created_at, updated_at}, ... ]                     | 認証が必要                                             |
| タスクの詳細取得                 | /api/tasks/<int:id>/         | GET          |                                                                              | {id, title, description, due_date, completed, created_at, updated_at}                              | 認証が必要                                             |
| タスクの更新                     | /api/tasks/<int:id>/         | PUT/PATCH    | title, description, due_date, completed                                      | {id, title, description, due_date, completed, created_at, updated_at}                              | 認証が必要                                             |
| タスクの削除                     | /api/tasks/<int:id>/         | DELETE       |                                                                              |                                                                                                    | 認証が必要                                             |
| タスクのステータス変更           | /api/tasks/<int:id>/status/  | POST         | completed                                                                    | {id, title, description, due_date, completed, created_at, updated_at}                              | 認証が必要                                             |
| 期限切れのタスク一覧取得         | /api/tasks/overdue/          | GET          |                                                                              | [ {id, title, description, due_date, completed, created_at, updated_at}, ... ]                     | 認証が必要                                             |
| 作成日または更新日でのフィルタリング | /api/tasks/filter/           | GET          | created_at, updated_at (例: ?created_at=2024-06-10, ?updated_at=2024-06-10)  | [ {id, title, description, due_date, completed, created_at, updated_at}, ... ]                     | 認証が必要                                             |
## 認証関連 allauth + JWT(token認証)
### Basic
| 機能名                            | API                                             | 入力                                       | 出力                                               | Note                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ----------------------------------------------- | ------------------------------------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ログイン                          | /dj-rest-auth/login/ (POST)                     | username, email, password                  | Returns Token key                                  |                                                                                                                                                                                                                                                                                                                                                                                                  |
| ログアウト                        | /dj-rest-auth/logout/ (POST)                    |                                            |                                                    | Note ACCOUNT_LOGOUT_ON_GET = True to allow logout using GET. This is the exact same configuration from allauth. NOT recommended, see: http://django-allauth.readthedocs.io/en/latest/views.html#logout                                                                                                                                                                                           |
| パスワードリセット                | /dj-rest-auth/password/reset/ (POST)            | email                                      |                                                    |                                                                                                                                                                                                                                                                                                                                                                                                  |
| パスワードリセット確認            | /dj-rest-auth/password/reset/confirm/ (POST)    | uid, token, new_password1, new_password2   |                                                    | Note uid and token are sent in email after calling /dj-rest-auth/password/reset/                                                                                                                                                                                                                                                                                                                 |
| パスワード変更                    | /dj-rest-auth/password/change/ (POST)           | new_password1, new_password2, old_password |                                                    | Note OLD_PASSWORD_FIELD_ENABLED = True to use old_password. Note LOGOUT_ON_PASSWORD_CHANGE = False to keep the user logged in after password change                                                                                                                                                                                                                                              |
| ユーザー情報                      | /dj-rest-auth/user/ (GET, PUT, PATCH)           | username, first_name, last_name            | Returns pk, username, email, first_name, last_name |                                                                                                                                                                                                                                                                                                                                                                                                  |
| トークン検証                      | /dj-rest-auth/token/verify/ (POST)              | token                                      | Returns an empty JSON object                       | Note USE_JWT = True to use token/verify/ route. Takes a token and indicates if it is valid. Will return a HTTP 200 OK in case of a valid token and HTTP 401 Unauthorized with {"detail": "Token is invalid or expired", "code": "token_not_valid"} in case of an invalid or expired token.                                                                                                       |
| トークンリフレッシュ              | /dj-rest-auth/token/refresh/ (POST)             | refresh                                    | Returns access                                     | Note USE_JWT = True to use token/refresh/ route. Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid. HTTP 401 Unauthorized with {"detail": "Token is invalid or expired", "code": "token_not_valid"} in case of an invalid or expired token.                                                                                            |

### 登録 Registration

| 機能名                            | API                                             | 入力                                  | 出力 | Note                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ----------------------------------------------- | ------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 登録                              | /dj-rest-auth/registration/ (POST)              | username, password1, password2, email |      |                                                                                                                                                                                                                                                                                                                                                                                                  |
| メール検証                        | /dj-rest-auth/registration/verify-email/ (POST) | key                                   |      | Note If you set account email verification as mandatory, you have to add the VerifyEmailView with the used name. You need to import the view: from dj_rest_auth.registration.views import VerifyEmailView. Then add the url with the corresponding name: path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent') to the urlpatterns list. |
| メール再送信                      | /dj-rest-auth/registration/resend-email/ (POST) | email                                 |      | Resends the email verification                                                                                                                                                                                                                                                                                                                                                                   |

### SNS
| 機能名                            | API                                             | 入力                                  | 出力 | Note                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ----------------------------------------------- | ------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ソーシャルメディア認証 - Facebook | /dj-rest-auth/facebook/ (POST)                  | access_token, code                    |      | Note access_token OR code can be used as standalone arguments, see https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/views.py                                                                                                                                                                                                                                        |
| ソーシャルメディア認証 - Twitter  | /dj-rest-auth/twitter/ (POST)                   | access_token, token_secret            |      |                                                                                                                                                                                                                                                                                                                                                                                                  |

