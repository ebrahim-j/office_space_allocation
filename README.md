# Dojo Space Allocator

## Introduction

**Dojo Space Allocator** is a CLI app that digitizes room allocation for Fellow and Staff at The Dojo. **Staff** can only be allocated office space while **Fellows** are allocated office space and living space if they choose so.


* Link to demo video: [![DOJO SPACE](https://asciinema.org/a/e3fjk7vrtvxw919n6k8bqxrgg.png)](https://asciinema.org/a/e3fjk7vrtvxw919n6k8bqxrgg)


## Installation and setup
Clone the repo into a folder of your choice on your 'terminal'
```
git clone https://github.com/mnjaggah/office_space_allocation.git
```
Create a virtual environment.
```
virtualenv venv
```
Navigate to the project folder
```
cd office_space_allocation
```
Activate your virtual environment
```
source venv/bin/activate
```
Install the required packages
```
pip install -r requirements.txt
```

## Launching the application
```
python3 run.py
```
You are good to go!
Interact with the program by running the following commands

## Commands to run:

* To create a new office or living space run ```create_room <room_type> <room_names>```

* To add a new staff or fellow run```add_person <person_name> <email_address> <role> [<wants_accomodation>]```.
 For fellows who want accomodation specify 'y' option

* To view all members in any room run ```print_room <room_name>```

* To view all allocations i.e. every room and their occupants run ```print_allocations [--o=filename]``` 
 specifying a filename saves the records in a ```.txt``` file

* To view all unallocated persons run ```print_unallocated [--o=filename]``` 
 specifying a filename saves the records in a ```.txt``` file

* ```load_people <filename>``` loads people from an existing ```.txt``` file

* ```reallocate_person <emailaddress> <new_roomname>``` reallocates a person from their current room to the given room

* ```save_state <database_name>``` saves the current state of the application to the given database

* ```load_state <database_name>``` loads data from an exisitng SQL database

## Testing
* Run ```nosetests ```

 *  To view test coverage statistics, run the following command;
 	```nosetests --with-coverage```
    