'''
Created on 17-May-2020

@author: dineshkumar kolimi
'''

import socket
from signal import signal, SIGINT

def handler(signal_received, frame):
        # Handle any cleanup here
        print("Alarmed")
        print('SIGINT or CTRL-C detected. Exiting gracefully')
        exit(0)

class Client(object):
    '''
    classdocs
    '''
    hostName = None
    s = None
    
    def __init__(self, port):
        '''
        Constructor to create a socket and connect to server
        '''
        try:
            self.s = socket.socket()
            hostName = socket.gethostname()
            self.s.connect((hostName, port))
        except socket.error:
            print ("error connecting to server")
            exit()
        
    def chooseService(self):
        '''
        method provides various services for the user to choose
        '''
        print("Select one of the option below\n \
            1. Find customer\n \
            2. Add customer\n \
            3. Delete customer\n \
            4. Update customer age\n \
            5. Update customer address\n \
            6. Update customer phone\n \
            7. Print report\n \
            8. Exit\n \
        ")
        try:
            while True:
                inVal = input("enter the option: ")
                print (inVal)
                if inVal.isdigit():
                    break
                if inVal.strip() == "":
                    print("please enter a integer!!")
                    continue
                if inVal[0] in ['+', '-']:
                    print("enter a option with out any precedent!!")
        except IndexError:
            print("option is empty")
        except ValueError:
            print("invalid value given")

        return int(inVal)
    
    def sendReqToServer(self, message, reqCode):
        '''
        sends a request to the server by encoding the data to bytes
        '''
        self.s.send(bytes(reqCode + '-' + message + '|', 'utf-8'))
        
    def receiveRespFromServer(self):
        '''
        receives response from server and decodes the message
        '''
        return "Response from server: \n" + (self.s.recv(1024)).decode('utf-8') + "\n"
    
    def getCustomerName(self):
        '''
        takes Customer Name from user
        '''
        while True:
            inVal = input("enter the name of customer: ")
            if inVal.strip() == "":
                print("Please give a name instead of empty literals!!")
            else:
                break
        return inVal
    
    def getCustomerAge(self):
        '''
        takes Customer Age from user
        '''
        while True:
            inVal = input("enter the age of customer: ")
            if inVal.isdigit():
                break
            if inVal.strip() == "":
                print("please enter a digit!!")
                continue
            if inVal[0] in ['+', '-']:
                print("enter a number with out any precedent: ")
            else:
                print("please give an integer value!!")
        return inVal
    
    def getCustomerAddress(self):
        '''
        takes Customer Address from user
        '''
        return input("enter the address of customer: ")
    
    def getCustomerPhone(self):
        '''
        takes Customer Phone number from user
        '''
        return input("enter the phone number of customer: ")
    
    def findCustomer(self):
        '''
        creates a request to find the customer from data base
        sends the request and process the response from server
        '''
        reqMsg = self.getCustomerName()
        self.sendReqToServer(reqMsg,'1')
        print (self.receiveRespFromServer())
        
    def addCustomer(self):
        '''
        creates a request to add the customer details to data base
        sends the request and process the response from server
        '''
        reqMsg = self.getCustomerName() + '|' + \
            self.getCustomerAge() + '|' + self.getCustomerAddress() + \
            '|' + self.getCustomerPhone()
        self.sendReqToServer(reqMsg,'2')
        print (self.receiveRespFromServer())
        
    def deleteCustomer(self):
        '''
        creates a request to delete a customer detail from data base
        sends the request and process the response from server
        '''
        reqMsg = self.getCustomerName()
        self.sendReqToServer(reqMsg,'3')
        print (self.receiveRespFromServer())
        
    def updateAge(self):
        '''
        creates a request to update the customer age in data base
        sends the request and process the response from server
        '''
        reqMsg = self.getCustomerName() + '|' + \
            self.getCustomerAge()
        self.sendReqToServer(reqMsg,'4')
        print (self.receiveRespFromServer())
        
    def updateAddress(self):
        '''
        creates a request to update the customer address in data base
        sends the request and process the response from server
        '''
        reqMsg = self.getCustomerName() + '|' + \
            self.getCustomerAddress()
        self.sendReqToServer(reqMsg,'5')
        print (self.receiveRespFromServer())
        
    def updatePhone(self):
        '''
        creates a request to update the customer phone in data base
        sends the request and process the response from server
        '''
        reqMsg = self.getCustomerName() + '|' + \
            self.getCustomerPhone()
        self.sendReqToServer(reqMsg,'6')
        print (self.receiveRespFromServer())
        
#     def printCustomerData(self, serResp):
#         userData = serResp.split('?')
#         for item in userData:
#             print(item)
        
    def printReport(self):
        '''
        creates a request to get the print report from server
        sends the request and process the response from server
        displays the report data
        '''
        self.sendReqToServer('print', '7')
        serResp = ""
        while True:
            serResp += self.s.recv(1024).decode('utf-8')
            if serResp.endswith("-1"):
                print(serResp.rsplit('-1')[0])
                print ("<---- end of user data ---->")
                break
            
    def closeConnection(self):
        '''
        creates a request to close the connection with the client
        properly closes the connection with server and quits
        '''
        self.sendReqToServer('exit', '8')
        print (self.receiveRespFromServer())
        self.s.close()
            
    def invalidOption(self):
        '''
        Notifies user if invalid option is provided
        '''
        print("invalid option given please try again!!")
        
    def runServices(self):
        '''
        Serves the user by taking necessary inputs
        accordingly calls the methods to server 
        and entire functionality is carried
        '''
        while True:
            option = self.chooseService()
            switcher = {
                1   :  "findCustomer",
                2   :  "addCustomer",
                3   :  "deleteCustomer",
                4   :  "updateAge",
                5   :  "updateAddress",
                6   :  "updatePhone",
                7   :  "printReport",
                8   :  "closeConnection"
            }
            fun = switcher.get(option,"invalidOption")
            getattr(Client, fun)(self)
            if option == 8:
                break

        
if __name__ == '__main__':
    signal(SIGINT, handler)
    cli = Client(12345)
    connectionState = cli.s.recv(1024)
    print (connectionState.decode('utf-8'))
    cli.runServices()            
        
        






    