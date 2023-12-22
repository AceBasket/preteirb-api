# API server for *Pret'eirb*

This project is the backend for an [android app](https://github.com/AceBasket/preteirb) I built. 


## Setting up
To build it locally, 
you need to adapt the `.env.config` file in the root folder and provide the necessary settings:
### For the postgresql database:
- DBNAME=`<database name>`
- DBHOST=`<database url ('localhost' if database is local)>`
- DBUSER=`<database user>`
- DBPASS=`<user password>`

### For the Azure storage account:
- AZURE_STORAGE_CONNECTION_STRING=`<connection string given by azure for the storage account>`
- AZURE_CONTAINER=`<name of storage account container where you want the images to be stored>`

For the Azure storage account, I haven't deleted mine so you don't need to change it.

## Run the code
Navigate to the root folder of the project then run those commands in order:
1. ```pip install -r requirements.txt```
2. ```python manage.py migrate```
3. ```python manage.py runserver```

The django app should now be running on [localhost:8000](localhost:8000). You can find the api schema on [localhost:8000/api/schema/swagger-ui](localhost:8000/api/schema/swagger-ui)
