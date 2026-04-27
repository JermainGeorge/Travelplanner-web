#django-admin startproject Travelplanner to create our website 
#python manage.py startapp planner to create our base app 

new updates rolling



migrations

making migrations for Location field in our models.py/booking 
non-null field error from the foreign Key attribute location and price_per_night


migration corruption issue from migrate command after makin non-null fields
##The error that comes with making migrations :
It is impossible to change a nullable field 'location' on accommodation to non-nullable without providing a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
 3) Quit and manually define a default value in models.py.
Select an option: 


What each option means :
1) Provide a one-off default now
You immediately give Django a value to use right now only once
Django will apply this value to all existing rows that currently have NULL in location
After that, new records will still follow whatever rules your model defines (not necessarily this default)
This does not permanently change your model, it’s just for fixing existing data during migration
2) Ignore for now
Django will continue with the migration without fixing existing NULL values
The database will still contain rows where location = NULL
This can lead to problems later because the column is now supposed to be NOT NULL
It assumes you will manually handle cleanup later using:
RunPython (Python script inside migration)
or RunSQL (raw SQL commands)
Essentially: “I’ll deal with inconsistent existing data myself later”
3) Quit and manually define a default value in models.py
Cancels the migration process
You go back to your models.py file and define a permanent default or rule
After updating the model, you re-run migrations
This means the default becomes part of your schema design going forward, not just for this migration


##This error is not about Django syntax — it’s about this principle:

You cannot enforce “required data” on a table that already contains missing data without deciding how to fill the gaps.


choose option 1
enter a string eg Nairobi for location and int for te prices 

