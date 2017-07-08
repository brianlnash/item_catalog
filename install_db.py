from item_database_config import Category
from database_operations import DatabaseOperations

db = DatabaseOperations()
new_categories = [Category(name='Cheetos that look like Jesus'),
                  Category(name='Pizza boxes from around the county'),
                  Category(name='Assorted goo'),
                  Category(name='Y2K rations'),
                  Category(name='McDonald\'s Beanie Babies: AKA The College Fund'),
                  Category(name='Mumified former pets'),
                  Category(name='Unidentifiable')]
for new_category in new_categories:
    db.addToDatabase(new_category)