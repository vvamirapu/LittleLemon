# LittleLemon

## APIs

All the APIs require authentication

* `restaurant/api-auth-token/`
* `restaurant/menu/`
* `restaurant/menu/(?P<pk>[^/.]+)`
* `restaurant/booking/`
* `restaurant/booking/tables`
* `restaurant/booking/tables/(?P<pk>[^/.]+)/`

* `api/menu-items/`
* `api/menu-items/(?P<pk>[0-9]+)`
* `api/message/`
* `api/users/`

* `auth/`
* `auth/users/set_password/`
* `auth/users/reset_password_confirm/`
* `auth/users/activation/`
* `auth/users/(?P<username>[^/.]+)/`
* `auth/users/resend_activation/`
* `auth/users/`
* `auth/users/me/`
* `auth/users/reset_username_confirm/`
* `auth/users/set_username/`
* `auth/users/reset_password/`
* `auth/users/reset_username/`
* `auth/token/login/`
* `auth/token/logout/`
