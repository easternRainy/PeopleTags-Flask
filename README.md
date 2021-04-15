# PeopleTags
![](images/000.png)
- [Demo Site](https://rebrand.ly/snnkn6x)
- [Web App Screenshots](Screenshots.md)

## Introduction
This is a flask website to manage personal social information. You could add persons, saving their information, adding them to groups, and tagging posts with persons or groups. All information is private except public posts, which could be seen by ANY user.

This website is adapted from my homework project, in which my team use Java Servlet to complete the website. Please checkout [here](https://github.com/secregister01/2019-10-28_PeopleTags.git) for the previous work.

## Deployment
### Install PostgreSQL
Use ANY method to install PostgreSQL depending on the operating system, then run

```
postgres -D /usr/local/var/postgres
```

to start the data base server.

### Install python dependencies

```
pip install -r requirements.txt
```

### Create the database

```
psql -U postgres -h localhost -d msds691 -f Database/create_db.sql
```

Where we could modify `postgres` to other username and `msds691` to other database name.

### Start PeopleTags server
```
chmod 755 start_server.sh
./start_server.sh
```
