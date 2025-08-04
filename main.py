import os
from modules import time_utils,web_utils,note_utils,todo_utils,email_utils
from modules import weather_utils,news_utils,fun_utils
from dotenv import load_dotenv
load_dotenv()


print("Hii....I am your Smart Assistant...How can i help you??")
while(True):
    
    print("Press 1 for date and time")
    print("Press 2 for web search")
    print("Press 3 for Notes app")
    print("Press 4 for To-Do List")
    print("Press 5 for Email Automation")
    print("Press 6 for Weather Report")
    print("Press 7 for News Headlines")
    print("Press 8 for Joke of the day")
    print("Press 9 for Quote of the day")
    print("Press 0 to exit")
    
    response = int(input("Enter the response:"))
    
    if response == 0:
        print("---SEE YOU LATER---")
        break

    elif response == 1:
        time_utils.show_time_and_date()

    elif response == 2:
        web_utils.open_website()

    elif response == 3:
        while True:
            print("\n1. Create Note\n2. Read Note\n3. Update Note\n4. Delete Note\n5. List Notes\n6. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                note_utils.create_note()
            elif choice == "2":
                note_utils.read_note()
            elif choice == "3":
                note_utils.update_note()
            elif choice == "4":
                note_utils.delete_note()
            elif choice == "5":
                note_utils.list_notes()
            elif choice == "6":
                break
            else:
                print("Invalid input.")
        
    elif response == 4:
        while True:
            print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Mark Task Done\n5. Exit")
            choice = input("Choose: ")
            
            if choice == "1":
                todo_utils.add_task()
            elif choice == "2":
                todo_utils.remove_task()
            elif choice == "3":
                todo_utils.view_tasks()
            elif choice == "4":
                todo_utils.mark_done()
            elif choice == "5":
                break
            else:
                print("Invalid option.")


    elif response == 5:
        email_utils.send_email()

    elif response == 6:
        while(True):
            resp = input("want weather updates ?(y/n): ").lower()
            if resp != 'n':
                weather_utils.get_weather()
            else:
                break

    elif response == 7:
        while(True):
            resp = input("want NEWS Headlines ?(y/n): ").lower()
            if resp != 'n':
                news_utils.get_news()
            else:
                break


    elif response == 8:
        while(True):
            resp = input("Want a joke??(y/n): ")
            if resp !='n':
                fun_utils.get_jokes()
            else:
                break


    elif response == 9:
        while(True):
            resp = input("Want a Quote??(y/n): ")
            if resp !='n':
                fun_utils.get_quotes()
            else:
                break       