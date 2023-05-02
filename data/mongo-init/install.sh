echo IMPORTING COLLECTION
mongoimport --authenticationDatabase=admin --username=$MONGO_INITDB_ROOT_USERNAME --password=$MONGO_INITDB_ROOT_PASSWORD --db=task_management --collection=tasks --file=/tmp/tasks.json
echo DONE IMPORTING