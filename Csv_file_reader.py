""" Import csv Module"""
import csv

""" File Selection """
def choose_file():
    while True:
        try:
            file = input("Enter File Location: ")
        except FileNotFoundError:
            print("Error: File not Found..")
        except TypeError:
            print("Error: Invaild Input")
        except:
            print("Error: Some Error occured")
        else:
            print("File Connected Successfully!")
            return file

def main():

    file = choose_file()
    f1 = open(file,'r')
    reader = csv.reader(f1)
    print("All Information is Stored Below.")
    for i in reader:
        print(i)

#Main Program
if __name__ == "__main__":
    main()



