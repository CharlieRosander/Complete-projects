import PySimpleGUI as sg
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# CLASS FOR DATABASE-CREATION
# Här har jag satt databasens delar som klass-variabler som defineras senare i programmet där det behövs
# Databasen skapas när funktionen blir kallad, och engine är satt som en parameter för att kunna fungera med
# browse-folder funktionen av programmet (Så att man kan sätta sin egna destination där db skapas)
class CreateDatabase:
    engine = None
    Base = declarative_base()
    session = None

    @classmethod
    def create_db(cls, engine):
        CreateDatabase.engine = engine
        CreateDatabase.Base.metadata.create_all(CreateDatabase.engine)


# CLASS FOR WINDOWS
# Här är alla windows som används i programmet skrivna inom funktioner för att lätt kunna kalla på dom där det behövs
# Layouten beskrivs först för att sedan returnera själva fönstret
# Alla element har sin unika key för att enkelt kunna separera allting och använda dess event/value
class CreateWindows:

    @staticmethod
    def start_window():
        start_layout = [[sg.vtop([sg.Text("Welcome to 'Idrottsföreningen'.\n"
                                          "\nStart by choosing the folder where the database will be created."
                                          "\nIf the database is already created, choose the folder where "
                                          "the database is located to connect to it.\n"
                                          "\nClick 'Connect/Create database' to continue.\n"
                                          "\nThis procedure is required each time the program is started.\n",
                                          font=11)]),
                         [sg.Text("")],
                         [sg.Text("")],
                         [sg.Input(key="-FOLDER_PATH-"), sg.FolderBrowse()],
                         sg.Button("Connect/Create database", font=12, key="-CREATE_DATABASE-"),
                         sg.Push(), sg.Button("Exit", font=12, key="-START_EXIT-")
                         ]]

        return sg.Window("Database setup", start_layout, finalize=True)

    @staticmethod
    def main_window():
        main_layout = [[
            [sg.Text("Welcome to the main menu!\n"
                     "\n"
                     "Click 'Search for member' to search for a member using their unique ID.\n"
                     "Click 'List all members' to list every member currently stored in the database.\n"
                     "Click 'Add member' to start adding a member.\n"
                     "Click 'Update member' to start updating an already existing member.\n"
                     "Click 'Delete member' to start deleting a member from the database.",
                     auto_size_text=True)],
            [sg.Text("Search for member: "), sg.Input(key="-SEARCH_INPUT-", do_not_clear=False),
             sg.Button("Search", key="-SEARCH-"),
             sg.Button("List all members", key="-LIST_ALL-")],
            [sg.Multiline(size=(125, 25), key="-MULTILINE-", do_not_clear=False)],
            sg.Button("Add member", key="-ADD_MEMBER-"),
            sg.Button("Update member", key="-UPDATE_MEMBER-"),
            sg.Button("Delete member", key="-DEL_MEMBER-"),
            sg.Push(), sg.Button("Exit", key="-MAIN_EXIT-")
        ]]

        return sg.Window("Main menu", main_layout, finalize=True)

    @staticmethod
    def add_member_window():
        add_member_layout = [
            [sg.Text("Enter the details of the member you want to add.")],
            [sg.Text("First name: "), sg.Push(), sg.Input(key="-FIRST_NAME-")],
            [sg.Text("Last name: "), sg.Push(), sg.Input(key="-LAST_NAME-")],
            [sg.Text("Address: "), sg.Push(), sg.Input(key="-ADDRESS-")],
            [sg.Text("Postal address: "), sg.Push(), sg.Input(key="-POST-")],
            [sg.Text("Zip code: "), sg.Push(), sg.Input(key="-ZIPCODE-")],
            [sg.Text("Fee paid?: "), sg.Radio("Yes: ", group_id=1, key="-FEE_YES-"),
             sg.Radio("No: ", group_id=1, key="-FEE_NO-")],
            [sg.Button("Add", key="-ADD-"), sg.Push(),
             sg.Button("Cancel", key="-CANCEL_ADD-")]
        ]
        return sg.Window("Add member", add_member_layout, finalize=True)

    @staticmethod
    def update_member_window():
        update_member_layout = [
            [sg.Text("Write the ID of the member you want to search for:")],
            [sg.Input(size=(53, 1), key="-UPDATE_SEARCH-", do_not_clear=False),
             sg.Button("Search", key="-UPDATE_SEARCH_BUTTON-")],
            [sg.Multiline(size=(60, 10), key="-UPDATE_SEARCH_RESULT-", do_not_clear=False)],
            [sg.Text("")],
            [sg.Text("Enter the details of the member you want to update:")],
            [sg.Text("First name: "), sg.Push(), sg.Input(key="-FIRST_NAME-")],
            [sg.Text("Last name: "), sg.Push(), sg.Input(key="-LAST_NAME-")],
            [sg.Text("Address: "), sg.Push(), sg.Input(key="-ADDRESS-")],
            [sg.Text("Postal address: "), sg.Push(), sg.Input(key="-POST-")],
            [sg.Text("Zip code: "), sg.Push(), sg.Input(key="-ZIPCODE-")],
            [sg.Text("Fee paid?: "), sg.Push(), sg.Radio("Yes: ", group_id=1, key="-FEE_YES-"),
             sg.Radio("No: ", group_id=1, key="-FEE_NO-")],
            [sg.Text("")],
            [sg.Button("Update", key="-UPDATE-"), sg.Push(),
             sg.Button("Cancel", key="-UPDATE_CANCEL-")]
        ]
        return sg.Window("Update member", update_member_layout, finalize=True)

    @staticmethod
    def delete_window():
        del_layout = [
            [sg.Text("Write the ID of the member you want to search for")],
            [sg.Input(key="-DEL_SEARCH-", do_not_clear=False), sg.Button("Search", key="-DEL_SEARCH_BUTTON-")],
            [sg.Multiline(size=(55, 10), key="-DEL_SEARCH_RESULT-", do_not_clear=False)],
            [sg.Button("Delete member", key="-DEL_BUTTON-"), sg.Push(), sg.Button("Cancel", key="-DEL_CANCEL-")]

        ]
        return sg.Window("Delete member", del_layout, finalize=True)


# CLASS FOR TABLES
class User(CreateDatabase.Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    post_address = Column(String)
    zip_code = Column(Integer)
    fee_paid = Column(String)


# CLASS FOR QUERIES
class Query:

    # Skickar en search-query till databasen där man filtrerar på ID och returnerar datan
    @classmethod
    def search_query(cls, member_id):
        result = CreateDatabase.session.query(User).filter(User.id == member_id).first()
        CreateDatabase.session.commit()

        return f"Your search found member:\n" \
               f"ID: {result.id}\n" \
               f"First name: {result.first_name}\n" \
               f"Last name: {result.last_name}\n" \
               f"Address: {result.address}\n" \
               f"Post Address: {result.post_address}\n" \
               f"Zipcode: {result.zip_code}\n" \
               f"Fee paid?: {result.fee_paid}"

    # Skickar en search-query till databasen där man filtrerar på ID
    # och sparar det i en variabel och tar sedan bort det ur databasen
    @classmethod
    def delete_query(cls, member_id):
        obj = CreateDatabase.session.query(User).filter(User.id == member_id).first()
        CreateDatabase.session.delete(obj)
        CreateDatabase.session.commit()

    # Skickar en search-query till databasen och tar alla occurrences,
    # sparar det i en variabel och gör ett test för att se om den är tom, är den tom sätts data till None
    # för att enkelt i nästa steg kunna testas i en if-sats. Annars returnera data
    @classmethod
    def list_all_query(cls):
        data = CreateDatabase.session.query(User).all()
        CreateDatabase.session.commit()

        if not data:
            data = None
        return data
