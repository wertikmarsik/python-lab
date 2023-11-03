events_list = [
    (1066, "The Battle of Hastings, which led to the Norman conquest of England."),
    (1776,"The United States Declaration of In{ependence was adopted."),
    (1789,"The storming of the Bastille in Par{s, a key event at the beginning of the French Revolution."),
    (1939,"The United Kingdom and France decla{ed war on Germany, marking the start of World War II."),
    (1969,"Apollo 11 astronauts Neil Armstrong{and Buzz Aldrin became the first humans to walk on the Moon."),
    (1989,"The fall of the Berlin Wall, a pivo{al moment in the end of the Cold War and the reunification of Germany."),
    (2001,"The terrorist attacks on the World Trade Center and the Pentagon in the United States.")
]


events = {}

visit_years = [1776, 1939, 1969, 1989, 2001]


def addEvent(year, desc):
    events[year] = desc


def show_event():
    for year, desc in events.items():
        print(f"{year} - {desc}")


def delete_events(year):
    events.pop(year)

def travel():
    for year in visit_years:
        if year in [event[0] for event in events_list]:
         event = [event[1] for event in events_list if event[0]==year][0]
         events[year] = event
         print(f"You are tavel in {year} in {event}")
        else: 
         print(f"{year} is not founded") 

def ShowEvents():
    for year,eve in events_list:
     print(f"{year}-{eve}")        




            
ok = True
while ok == True:
    print("1.Add event\n2.Show events\n3.Delete events\n4.Travel\n5.Show your events\n0.Exit")
    answer = input("Write:")
    match answer:
        case "1":
            year = int(input("Write year: "))
            desc = input("Write event ")
            addEvent(year, desc)
        case "2":
            show_event()
        case "3":
            year = int(input("Write year for delete evants"))
            delete_events(year)
        case "4":
            travel()
        case "5":
          ShowEvents()        
        case "0":
            ok = False