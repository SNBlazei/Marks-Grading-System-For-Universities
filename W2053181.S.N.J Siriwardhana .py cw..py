
# I declare that my work contains no examples of misconduct, such as plagiarism, or 
#collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID:w2053181
# Date:12/10/2023







from token import STAR


from graphics import *
#Initializing Variables
count = 0
progress_count = 0
exclude_count = 0
do_not_progress_count = 0
module_trailer_count = 0
#Initializing Data List
Records__ = []



def get_pass_mark():
    while True:
        try:
            x = int(input("Enter the Pass credit: "))
            if x in range(0, 121, 20):
                return x
            else:
                print("out of range")
        except ValueError:
            print("integer required")


def get_defer_mark():
    while True:
        try:
            y = int(input("Enter the defer credit: "))
            if y in range(0, 121, 20):
                return y
            else:
                print("out of range")
        except ValueError:
            print("integer required")


def get_fail_mark():
    while True:
        try:
            z = int(input("Enter Your Fail credit: "))
            if z in range(0, 121, 20):
                return z
            else:
                print("out of range")
        except ValueError:
            print("integer required")

def get_choice():
    while True:
        print("Would you like to enter another set of data")
        option = input("Enter 'y' for yes and 'q' to quit and view results : ")
        option = option.lower()

        if option not in ['y','q']:
            print("invalid option Enter 'y' or 'q' ")
            continue
        else:
            return option


def check_total(mark):
    while True:
        
        if mark == 120:
            return mark
        else:
            print("Total Incorrect")
            main()

def main():
    global progress_count
    global exclude_count
    global do_not_progress_count
    global module_trailer_count
    global out__come
    global get_records
    global choice

    while True:
        X = get_pass_mark()
        Y = get_defer_mark()
        Z = get_fail_mark()

        total_mark = X + Y + Z

        check_total(total_mark)
    

        if X == 120:
            out__come = " Progress"
            print(out__come)
            progress_count += 1
        elif X == 100:
            out__come = " Progress (module trailer) "
            print(out__come)
            module_trailer_count += 1
        elif Z >= 80:
            out__come = " Exclude"
            print(out__come)
            exclude_count += 1
        else:
            out__come = " Do not progress - module retriever"
            print(out__come)
            do_not_progress_count += 1
 #store student data to the list
        get_records = (f"{out__come} - {X} , {Y} , {Z}")
        Records__.append(get_records)
        

        choice = get_choice()
        

        if choice == "q":
            for s in Records__:
                print(f"{s}")
                with open('data.txt', 'w') as f:
                    for i in Records__:
                        f.write(f"{i}\n")
                    f.close()
            break
        
        



    # Create histogram
    win = GraphWin("Progression Histogram", 1200, 800)
    win.setBackground("White")

    label = Text(Point(600, 20), "Histogram Results")
    label.setStyle("bold")
    label.setSize(18)
    label.setTextColor("grey")
    label.draw(win)

    categories = ["Progress", "Module Trailer", "Retriever", "Excluded"]
    counts = [progress_count, module_trailer_count, do_not_progress_count, exclude_count]
    colors = ["PaleGreen", "PaleGreen4", "DarkOliveGreen4", "LightPink"]

    total_students = sum(counts)

    for i in range(4):
        category_label = Text(Point(150 + i * 300, 700), categories[i])  
        category_label.draw(win)

        bar_height = counts[i] * 10
        bar = Rectangle(Point(100 + i * 300, 600), Point(200 + i * 300, 600 - bar_height))
        bar.setFill(colors[i])
        bar.draw(win)

    
        count_label = Text(Point(150 + i * 300, 600 - bar_height - 20), str(counts[i]))
        count_label.setTextColor("black")
        count_label.draw(win)

    line = Line(Point(100, 600), Point(1200, 600))
    line.setWidth(2)
    line.draw(win)

    total_label = Text(Point(600, 770), f"outcomes in total: {total_students}")
    total_label.setSize(18)
    total_label.draw(win)

    win.getMouse()
    win.close()
    quit()
    
if __name__ == "__main__":
    main()


