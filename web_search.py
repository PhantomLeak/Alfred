import webbrowser
import alfred as af  

def googlesearch(i):
    websearch = "https://www.google.com/search?q=" + i
    print("Loading...")
    webbrowser.open(websearch, new=0, autoraise=True)
    again = input("Would you like to enter another search?: ")
    if again == "yes":
        googlesearch()
    elif again == "no":
        print('Not a problem! \n')
        af.alfred_main(1)