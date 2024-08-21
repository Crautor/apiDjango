# Django API Project

## Introduction
This is a Django-based API project designed to manage user information. The API supports basic CRUD operations including creating, retrieving, updating, and deleting users.

## Requirements
- Python 3.x
- pip (Python package installer)

## Install
To set up the project, follow these steps:

#### 1. Clone the repository:

````
    git clone https://github.com/Crautor/apiDjango.git
````

#### 2. Navigate to the project directory:
````
    cd apiDjango
````

#### 3. Set up a virtual environment:
````
    py -m venv venv
````
#### 4. Open the project in Visual Studio Code:
````
    code .
````
#### 5. Open Terminal on Visual Studio Code:
- Press the `ctrl+'` .

#### 6. Activate the virtual environment:
````
    ./venv/Scripts/activate
````

### Optional (Windows)
If you are on Windows and encounter issues executing the script, follow these steps:

#### 1. Open ``Windows PowerShell`` as Administrator:

    - Press the `Win` key and type `Windows PowerShell`.
    - Right-click on `Windows PowerShell` and select `Run as administrator`.


#### 2. Set the execution policy to allow the script:

````
    Set-ExecutionPolicy RemoteSigned
````
    
#### 3. Type `S` to confirm and press `Enter`.

#### 4. Retry activating the virtual environment in the VS Code terminal:

````
    ./venv/Scripts/activate
````

#

#### 6. Change the Python interpreter in VS Code to the virtual environment:

- Press `Ctrl+Shift+P` to open the command palette.
- Type `Python: Select Interpreter` and press `Enter`.
- Choose the interpreter with `('venv':venv)` in its name.

#### 7. Install the required packages:

````
    pip install -r requirements.txt
````

#### 8. Run the development server:

````
    py manage.py runserver
````


## API Routes

### Return All Users (Array)

```http
  GET http://127.0.0.1:8000/api/user
```
### Return All Users with their ids (Array)

```http
  GET http://127.0.0.1:8000/api/user/ids
```

### Return One User (Object)

```http
  GET http://127.0.0.1:8000/api/user/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Required**: user id |


### Return All User By Departament (Array)

```http
  GET http://127.0.0.1:8000/api/user/departament/${departament}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `departament`      | `string` | **Required**: user departament (Case Sensitive) |


### Create New User

```http
  POST http://127.0.0.1:8000/api/user/create
```

| Parâmetro    | Tipo       | Descrição                                   |
| :----------  | :--------- | :------------------------------------------ |
| `name`       | `CharField(100)` | **Required**: User name |
| `email`      | `EmailField` | **Required**: User email |
| `departament`| `CharField(100)` | **Required**: User departament |
   
#### Ex:
````
{
    "name": "userName",
    "email": "userEmail@Domain.com",
    "departament": "userDepartament"
}
````

### Update User

```http
  PUT http://127.0.0.1:8000/api/user/update/${id}
```

| Parâmetro    | Tipo       | Descrição                                   |
| :----------  | :--------- | :------------------------------------------ |
| `id`       | `int` | **Required**: User id |
| `name`       | `CharField(100)` | **Required**: User name |
| `email`      | `EmailField` | **Required**: User email |
| `departament`| `CharField(100)` | **Required**: User departament |
   
#### Ex:
````
{
    "name": "newUserName",
    "email": "newUserEmail@Domain.com",
    "departament": "newUserDepartament"
}
````


### Delete User
```http
  DELETE http://127.0.0.1:8000/api/user/delete/${id}
```

| Parâmetro    | Tipo       | Descrição                                   |
| :----------  | :--------- | :------------------------------------------ |
| `id`       | `int` | **Required**: User id |

