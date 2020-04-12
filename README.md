# DilCMS
Personal for fun CMS

## Features
- Page Management -> Add / Remove components from page
- Editor -> Visual drag and drop editor for adding and removing components

## Architecture
Python Flask Backend
- Static file server and REST listener

## Usage
Build your frontend application and place into the `/app/dilcms/serve-folder`.
- Your Application should make use of the DilCMS api to get and render Page Models.
- For an example PageModelRenderer see [DilCMS React PageModelRenderer](dilcms-react-page-model-renderer)

Run Docker container with build flag to pick up possible changes:
```sh
docker-compose up --build
```

With container running pages should be available at:
- [localhost:5000/home](http://localhost:5000/home)
