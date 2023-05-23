import PySimpleGUI as sg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.orm.exc
from backend import CreateWindows, CreateDatabase, User, Query

# Här kan man välja tema på programmet
sg.theme("DarkBlue")


# INTERFACE-FUNCTIONS
# Här är olika funktioner som programmet kallar på när användaren trycker på knappar osv.
# Många av funktionerna i sin tur kallar på respektive funktion i backend-filen (som sköter queries osv)
class InterfaceFunctions:
    member_del = None
    member_update = None

    # ADD MEMBER FUNCTION
    # Här görs först en koll om values FEE_YES/NO är falska för att man inte ska kunna lämna det fältet blankt,
    # sedan görs ett test till för att sätta dess värde, och slutligen tar den datan från dom andra fälten och commitar
    @classmethod
    def add_member(cls):
        fee_paid = None

        if values["-FEE_YES-"] is False and values["-FEE_NO-"] is False:
            sg.popup_no_buttons("Please select Yes or No in the 'Fee paid?' field", auto_close=True,
                                auto_close_duration=1.5,
                                background_color="White", text_color="Black", no_titlebar=True, font=20)
        else:
            try:
                if values["-FEE_YES-"]:
                    fee_paid = "Yes"
                elif values["-FEE_NO-"]:
                    fee_paid = "No"

                member = User(first_name=values["-FIRST_NAME-"], last_name=values["-LAST_NAME-"],
                              address=values["-ADDRESS-"], post_address=values["-POST-"],
                              zip_code=values["-ZIPCODE-"], fee_paid=fee_paid)

                CreateDatabase.session.add(member)
                CreateDatabase.session.commit()

                sg.popup_no_buttons("Member added to the database!", auto_close=True, auto_close_duration=1.5,
                                    background_color="White", text_color="Black", no_titlebar=True, font=20)

                window.close()
            except AttributeError:
                sg.popup("Something went wrong! Exception: AttributeError", background_color="White",
                         text_color="Black", no_titlebar=True)

    # UPDATE-MEMBER SEARCH FUNCTION
    # Här sätts klassvariabeln member_update till ID-värdet som söks på för att sen kalla på search-query:n
    # och skriva ut resultatet som returneras ifrån den
    @classmethod
    def update_member_search(cls):
        InterfaceFunctions.member_update = values["-UPDATE_SEARCH-"]

        try:
            window["-UPDATE_SEARCH_RESULT-"].print(Query.search_query(member_id=values["-UPDATE_SEARCH-"]))
        except AttributeError:
            window["-UPDATE_SEARCH_RESULT-"].print("Could not find the member you searched for,"
                                                   " double-check the spelling and data-type")

    # UPDATE MEMBER FUNCTION
    # Den här funktionen använder sig först av samma klassvariabel som innan och gör en search-query på det igen
    # för att spara returnerade värdet i en ny variabel som används för att updatera medlemmen.
    # Det görs tester för att se till så att enbart nya värden som använder skriver in uppdateras, den kollar då
    # om det först har skrivits något i fälten alls, och om det är True kollar den om det är samma värde som tidigare,
    # är det False så uppdaterar den värdet i databasen
    @classmethod
    def update_member(cls):
        updated_record = CreateDatabase.session.query(User).filter(User.id == InterfaceFunctions.member_update).first()

        try:
            if values["-FIRST_NAME-"] and values["-FIRST_NAME-"] != updated_record.first_name:
                updated_record.first_name = values["-FIRST_NAME-"]
            if values["-LAST_NAME-"] and values["-LAST_NAME-"] != updated_record.last_name:
                updated_record.last_name = values["-LAST_NAME-"]
            if values["-ADDRESS-"] and values["-ADDRESS-"] != updated_record.address:
                updated_record.address = values["-ADDRESS-"]
            if values["-POST-"] and values["-POST-"] != updated_record.post_address:
                updated_record.post_address = values["-POST-"]
            if values["-ZIPCODE-"] and values["-ZIPCODE-"] != updated_record.zip_code:
                updated_record.zip_code = values["-ZIPCODE-"]
            if values["-FEE_YES-"]:
                updated_record.fee_paid = "Yes"
            else:
                updated_record.fee_paid = "No"

            CreateDatabase.session.commit()

            sg.popup_no_buttons("Member updated!", auto_close=True, auto_close_duration=1.5,
                                background_color="White", text_color="Black", no_titlebar=True, font=20)
            window.close()
        except AttributeError:
            window["-UPDATE_SEARCH_RESULT-"].print("No member have been selected or "
                                                   "the member you searched for does not exist; Nothing was updated.")

    # SEARCH FOR MEMBER FUNCTION
    @classmethod
    def search_member(cls):
        try:
            window["-MULTILINE-"].print(Query.search_query(member_id=values["-SEARCH_INPUT-"]))

        except AttributeError:
            window["-MULTILINE-"].print("Could not find the member you searched for,"
                                        " double-check the spelling and data-type")

    # LIST ALL DATA
    # Här testas först om det returnerade värdet av query:n är None
    # (som sätts i dess backend-funktion om variabeln är tom), annars kör en loop igenom datan och skriver ut det
    @classmethod
    def list_all_members(cls):
        if Query.list_all_query() is None:
            window["-MULTILINE-"].print("There is currently no data stored in the database.")
        else:
            for user in Query.list_all_query():
                try:
                    window["-MULTILINE-"].print(f"ID: {user.id}"
                                                f"\nFirst name: {user.first_name}"
                                                f"\nLast name: {user.last_name}"
                                                f"\nAddress: {user.address}"
                                                f"\nPost address: {user.post_address}"
                                                f"\nZip code: {user.zip_code}"
                                                f"\nFee paid?: {user.fee_paid}\n")
                except AttributeError:
                    window["-MULTILINE-"].print("Something went wrong")
                except TypeError:
                    window["-MULTILINE-"].print("Something went wrong")

    # DELETE-SEARCH FUNCTION
    @classmethod
    def delete_search(cls):
        InterfaceFunctions.member_del = values["-DEL_SEARCH-"]

        try:
            window["-DEL_SEARCH_RESULT-"].print(Query.search_query(member_id=values["-DEL_SEARCH-"]))
        except AttributeError:
            window["-DEL_SEARCH_RESULT-"].print("Could not find the member you searched for,"
                                                " double-check the spelling and data-type")

    # DELETE BUTTON FUNCTION
    @classmethod
    def delete_member(cls):
        try:
            Query.delete_query(member_id=InterfaceFunctions.member_del)
            sg.popup_no_buttons(f"Member deleted", auto_close=True, auto_close_duration=1,
                                background_color="White", text_color="Black", no_titlebar=True, font=20)

        except sqlalchemy.orm.exc.UnmappedInstanceError:
            window["-DEL_SEARCH_RESULT-"].print("Could not find the member you tried to delete,"
                                                " member doesn't exist or have already been deleted")


# WHILE-LOOP FÖR DATABASE-CONNECT/CREATE
# Här bestäms vilket fönster som ska visas, i detta fall start_window.
# Jag använder också sg.read_all_windows så att alla fönster läses när dom är aktiva, man slipper då nesting helt
window1 = CreateWindows.start_window()
while True:
    window, event, values = sg.read_all_windows()

    # Stänger av programmet
    if event == "-START_EXIT-" or event == sg.WIN_CLOSED:
        sg.popup_no_buttons("Exiting, bye!", auto_close=True, auto_close_duration=1.5,
                            background_color="White", text_color="Black", no_titlebar=True, font=20)
        exit()

    # Ett test görs för att se till att man väljer en path för sin db, sen sätts en variabel till den path:en.
    # Vi kallar på funktionen create_db som ligger i backend, och skickar in som parameter sqlalchemy:s create_engine
    # funktion, tillsammans med path:en. Vi kallar också på sessionmaker för att skapa en session.
    # Det här görs inför varje start av programmet så att man kan välja att skapa en ny databas eller
    # connect:a till en befintlig db.
    elif event == "-CREATE_DATABASE-":
        if not values["-FOLDER_PATH-"]:
            sg.popup_no_buttons("You must select the folder destination!", auto_close=True, auto_close_duration=2,
                                background_color="White", text_color="Black", no_titlebar=True, font=20)
        else:
            folder_path = values["-FOLDER_PATH-"]
            CreateDatabase.create_db(engine=create_engine(f"sqlite:///{folder_path}/idrottsföreningen.db"))
            CreateDatabase.session = sessionmaker(CreateDatabase.engine)()
            sg.popup_no_buttons("Database & tables created", auto_close=True, auto_close_duration=1.5,
                                background_color="White", text_color="Black", no_titlebar=True, font=20)
            window.close()
            break

# WHILE-LOOP FÖR RESTEN AV PROGRAMMET
# Här körs större delen av programmet och beskriver vad som ska hända när användaren trycker på alla olika knappar osv.
# Jag delade in det i 2 loopar, en för db-creation som bara behövs göras en gång i starten av programmet,
# och en för resten av programmet
window2, window3, window4, window5, window6 = CreateWindows.main_window(), None, None, None, None
while True:
    window, event, values = sg.read_all_windows()

    # Kollar vilket fönster som är aktivt, är det fönster 2 så stänger programmet av om man trycker på exit eller X
    # Annars om det inte är fönster 2 så stänger programmet bara fönstret om man trycker på respektive knapp eller X
    if window == window2 and event == sg.WIN_CLOSED or event == "-MAIN_EXIT-":
        sg.popup_no_buttons("Exiting, bye!", auto_close=True, auto_close_duration=1.5,
                            background_color="White", text_color="Black", no_titlebar=True, font=20)
        exit()

    elif not window == window2 and event == sg.WIN_CLOSED or event == "-CANCEL_ADD-" or event == "-DEL_CANCEL-" \
            or event == "-UPDATE_CANCEL-":
        window.close()

    elif event == "-ADD_MEMBER-" and not window4:
        CreateWindows.add_member_window()

    if event == "-ADD-":
        InterfaceFunctions.add_member()

    elif event == "-UPDATE_MEMBER-" and not window6:
        CreateWindows.update_member_window()

    if event == "-UPDATE_SEARCH_BUTTON-":
        InterfaceFunctions.update_member_search()

    if event == "-UPDATE-":
        InterfaceFunctions.update_member()

    elif event == "-SEARCH-":
        InterfaceFunctions.search_member()

    elif event == "-LIST_ALL-":
        InterfaceFunctions.list_all_members()

    elif event == "-DEL_MEMBER-" and not window5:
        CreateWindows.delete_window()

    if event == "-DEL_SEARCH_BUTTON-":
        InterfaceFunctions.delete_search()

    if event == "-DEL_BUTTON-":
        InterfaceFunctions.delete_member()
