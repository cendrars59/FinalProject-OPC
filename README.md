# OPC-DA-PY-P13 Project

## 1.1 Purpose 
This project has been created in a context of Application developer learning path provided by OpenClassRooms. This project is a practice for evaluation. The practice description is [here](https://openclassrooms.com/fr/paths/68/projects/159/assignment) (Description in French)

## 1.2 Solution description

The proposed solution is to develop a web application for a rugby club management. The solution currently offers the following features:

* 1 - User account management (User creation (Via admin feature) / login / log out / User detailed information page).
* 2 - Club members management.
* 3 - Knowledge database to create practice or training session.

### 1.2.1 Integrated features to the solution. 
To satisfy the business need, several features have been implemented.

#### 1.2.1.1 - User management:
The application users offers several functionalities as described here under :
- Login 
- Logout 
- User profil update
- User information detailed view 
- Players management
- Managers management 
```
project
│   README.md   
│   ...
└───users
│       
```

#### 1.2.1.2- Static pages
The application pages offers several functionalities as described here under :
- Homepage 
- Mentions 
```
project
│   README.md   
│   ...
└───pages
│       
```

#### 1.2.1.3- Practices knowledge database management 
The application catlog offers several functionalities as described here under :
- Practices list  
- Practice CrU
```
project
│   README.md   
│   ...
└───practice
│       
```

#### 1.2.1.4- Training session knowledge database management 
The application catlog offers several functionalities as described here under :
- Training session list  
- Training session CrU
```
project
│   README.md   
│   ...
└───training_session
│       
```

# 2. Project settings

We strongly recommand to set the application into virtual environnement to avoid any conflict with others Python application.
## 2.1 Third part software & system

### 2.1.1 Python version 
The solution has been developed from 3.7.5 Python version -> see [Release note](https://www.python.org/downloads/release/python-375/)

### 2.1.2 Django 
The solution has been devellopped on top of Django 3.1.7 version -> see  [here](https://docs.djangoproject.com/en/3.1/releases/3.1.7/)

### 2.1.3 Requests 
In order to manage call to API and answer the librairy requests version 2.23.0 has been used -> see  [here](https://2.python-requests.org/en/master/)

### 2.1.4 Postgresql
For the project, We use a postgresql database version 12 -> see  [here](https://www.postgresql.org/)

### 2.1.5 Psyco pg2
Into the project, we use POSTGRESQL Database. In order to manage connection with it is used PSYCOPG2 librairy. see -> [here](https://www.psycopg.org/docs/Ok ).

# 2. Project settings

We strongly recommand to set the application into virtual environnement to avoid any conflict with others Python application.
## 2.1 Third part software & system

### 2.1.1 Python version 
The solution has been developed from 3.7.5 Python version -> see [Release note](https://www.python.org/downloads/release/python-375/)

### 2.1.2 Django 
The solution has been devellopped on top of Django 3.1.7 version -> see  [here](https://docs.djangoproject.com/en/3.1/releases/3.1.7/)

### 2.1.3 Requests 
In order to manage call to API and answer the librairy requests version 2.23.0 has been used -> see  [here](https://2.python-requests.org/en/master/)

### 2.1.4 Postgresql
For the project, We use a postgresql database version 12 -> see  [here](https://www.postgresql.org/)

### 2.1.5 Psyco pg2
Into the project, we use POSTGRESQL Database. In order to manage connection with it is used PSYCOPG2 librairy. see -> [here](https://www.psycopg.org/docs/Ok ).

# 3. Project installation

Here under the description of the installation procedure 
## 3.1 Third part software & system

- Installing Python 
- Installing Postgresql 
- To install the third parts librairies and django use pip install requirements.txt 
