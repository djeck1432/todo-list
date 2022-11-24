# TODO list

## Installation:

- Create new dir and change your current dir to `project`:
```
mkdir proejct
cd project 
```
- Clone repository to `project` dir: 
```bash
git clone git@github.com:djeck1432/todo-list.git
```
- Run docker-compose:
```
docker-compose up -d
```
- Stop docker-compose:
```bash
docker-compose down
```

## Good to know:

1. It will automatically create for you superuser with next credentials:
`user_name=root` and `password=root`
3. For comfort and easy testing, you can use `swagger` with next credentials: `user_name=root` and `password=root` follow this next link
 [http://0.0.0.0:8800/api/docs/](http://0.0.0.0:8800/api/docs/).


## How to auth:
 
1. We need to get user `token` to work with API:
```curl
curl --location --request POST 'http://0.0.0.0:8800/token-auth/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "root",
    "password": "root"
}'
```
As result will be: `{"token":"<user_token>"}%`
2. For all further requests, please add token to headers, like this:
`Authorization: Token <token>`



