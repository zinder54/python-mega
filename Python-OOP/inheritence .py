'''single inheritance'''
# class Apple:
#     manufacturer = "Apple inc."
#     contact = "www.apple.com/contact"

#     def contact_details(self):
#         print("to contact us please log into", self.contact)

# class MacBook(Apple):
#     def __init__(self):
#         self.year_of_manufacture = 2017
    
#     def manufacture_details(self):
#         print(f"this MacBook was manufactured in the year {self.year_of_manufacture} by {self.manufacturer}")

# mac = MacBook()
# mac.manufacture_details()
# mac.contact_details()
'''multiple inheritance'''
# class OperatingSystem:
#     multitasking = True

# class Apple:
#     website = "www.apple.com"

# class MacBook(OperatingSystem, Apple):#if two variables named the same, 
#     #the one choen when called depends on order in this class bracket
#     def __init__(self):
#         if self.multitasking is True:
#             print(f"this is a multitasking system, visit {self.website} for more details")

# mac = MacBook()
'''multilevel inheritance'''
class MusicalInstruments:
    number_of_major_keys = 12
class StringInstruments(MusicalInstruments):
    type_of_wood = "tonewood"

class Guitar(StringInstruments):
    def __init__(self):
        self.number_of_strings = 6
        print(f"this guitar has {self.number_of_strings}. it is made of {self.type_of_wood}, and can play {self.number_of_major_keys} keys.")

guitar = Guitar()