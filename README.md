# Djangobook

A small social network built with Django, in the spirit of Instagram: users sign up, publish photo posts, like them, follow other users and search for people.

It started as a university web-development project (2023). The static HTML/CSS mock-up that came first lives in [`prototype/`](prototype/), with its original commit history.

## Features

- Sign up, log in and log out
- User profiles with first/last name, bio, location and profile picture
- Photo posts with captions, shown in a feed made of the posts of the people you follow plus your own
- Likes
- Follow / unfollow
- Search for users
- Account settings page

## Stack

| Part | Technology |
|---|---|
| Backend | Django 5.2 (LTS), Python 3.10+ |
| Database | SQLite |
| Static files | WhiteNoise |
| Images | Pillow |
| Production server | Gunicorn (deployed on Railway) |
| Front end | Django templates, plain CSS and JavaScript |

## Project layout

```
core/         The app: models (Profile, Post, LikePost, FollowersCount), views, URLs
djangobook/   Project settings, URL configuration, WSGI/ASGI entry points
templates/    HTML templates
static/       CSS, JavaScript and images
media/        Uploaded images (only the default avatar is tracked by git)
prototype/    Original static HTML/CSS front-end mock-up
```

## Run it locally

```sh
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export DJANGO_DEBUG=1              # Windows PowerShell: $env:DJANGO_DEBUG="1"
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ and create an account from the sign-up page. With `DJANGO_DEBUG=1` no secret key is needed; in any other mode `DJANGO_SECRET_KEY` is required.

## Configuration

All settings come from environment variables (see [`.env.example`](.env.example)):

| Variable | Meaning | Default |
|---|---|---|
| `DJANGO_DEBUG` | `1` enables debug mode, local development only | off |
| `DJANGO_SECRET_KEY` | Django secret key, **required** when debug is off | none |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated host names | `localhost,127.0.0.1` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Comma-separated origins, e.g. `https://your-app.up.railway.app` | empty |

## Deploy (Railway or similar)

1. Set the four variables above in the hosting dashboard. Generate a key with `python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"`.
2. Build step: `pip install -r requirements.txt && python manage.py collectstatic --noinput`.
3. Start command (also in [`Procfile`](Procfile)): `gunicorn djangobook.wsgi`, after `python manage.py migrate` on release.

## Known limitations

- Posts and likes refer to users by name (plain text fields) instead of foreign keys, so renaming a user does not update their posts. Moving to foreign keys is the main planned improvement.
- Uploaded images are stored on the local disk. On hosts with an ephemeral file system they disappear on redeploy, and they are served by Django only in debug mode; production needs object storage (for example S3) or a persistent volume.
- There are no automated tests yet beyond Django's empty test module.
- SQLite is fine for a demo but not for concurrent production use.
