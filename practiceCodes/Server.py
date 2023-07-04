'''
Created on 17-May-2020

@author: dineshkumar kolimi
'''

import socket
from signal import signal, SIGINT

def handler(signal_received, frame):
        # Handle any cleanup here
        print('SIGINT or CTRL-C detected. Exiting gracefully')
        exit(0)

class Server(object):
    '''
    classdocs
    '''
    hostName = None
    clientObj = None
    clientAddress = None
    userData = {}
    s = None
    
    def __init__(self, port):
        '''
        Constructor to create a socket
        '''
        try:
            self.s = socket.socket()
            hostName = socket.gethostname()
            self.s.bind((hostName, port))
            self.s.listen(5)
        except socket.error:
            print ("error creating a socket")
    
    def loadUserData(self):
        '''
        loads user data from file
        '''
        try:
            fs = open("data.txt", 'r+')
            while True:
                line = fs.readline()
                if not line:
                    break
                self.addToDataStructure(line)
        except IOError:
            print("error while reading a file")
        
        finally:
            fs.close()
            
    def addToDataStructure(self, line):
        '''
        adds a client and related data to a data structure
        '''
        listVal = (line.split('|'))
        key = listVal[0].strip()
        if key == '':
            return -1
        elif key in self.userData:
            return -1
        else:
            value = {"age": listVal[1].strip(), "address": listVal[2].strip(), "phone": listVal[3].strip()}
            self.userData.update({key: value})
        
    def findCustomer(self, data):
        '''
        search for customer name from the database
        ''' 
        key = data.split('|')[0].strip()
        if key not in self.userData.keys():
            self.sendMessageToclient("customer not found")
        else:
            val = self.userData[key]
            clientMessage = "%s|%s|%s|%s"%(key, val['age'], val['address'], val['phone'])
            self.sendMessageToclient(clientMessage)
    
    def addCustomer(self, customerData):
        '''
        adds customer to the data base
        ''' 
        if self.addToDataStructure(customerData) == -1:
            self.sendMessageToclient("customer data already present")
        else:
            self.sendMessageToclient("customer data successfully added")
         
    def deleteCustomer(self, data):
        '''
        deletes the customer details
        '''
        key = data.split('|')[0].strip()
        if key not in self.userData.keys():
            self.sendMessageToclient("customer not fount")
        else:
            del self.userData[key]
            self.sendMessageToclient("customer is successfully deleted")
        
    def updateCustomerAge(self, data):
        '''
        loads user data from file
        '''  
        key = data.split('|')[0].strip()
        val = data.split('|')[1].strip()
        if key not in self.userData.keys():
            self.sendMessageToclient("customer not fount")
        else:
            (self.userData[key])['age'] = val
            self.sendMessageToclient("customer age is successfully updated")
        
    def updateCustomerAddress(self, data):
        '''
        updates the address of a customer
        ''' 
        key = data.split('|')[0].strip()
        val = data.split('|')[1].strip()
        if key not in self.userData.keys():
            self.sendMessageToclient("customer not fount")
        else:
            (self.userData[key])['address'] = val
            self.sendMessageToclient("customer address is successfully updated")
            
    def updateCustomerPhone(self, data):
        '''
        updates the phone number of a customer
        ''' 
        key = data.split('|')[0].strip()
        val = data.split('|')[1].strip()
        if key not in self.userData.keys():
            self.sendMessageToclient("customer not fount")
        else:
            (self.userData[key])['phone'] = val
            self.sendMessageToclient("customer phone is successfully updated")
        
    def printReport(self, data):
        '''
        sends a copy of entire data base for the client to verify at its end
        '''
        print("sending "+ data.split("|")[0] + " response!!")
        #To check if list is empty
        if not bool(self.userData):
            self.sendMessageToclient("Customer Data is empty")      
        for key in sorted(self.userData):
            val = self.userData[key]
            clientMessage = "%s|%s|%s|%s\n"%(key, \
                                "null" if val['age'] == "" else val['age'], \
                                "null" if val['address'] == "" else val['address'], \
                                "null" if val['phone'] == "" else val['phone']
                            )
            self.sendMessageToclient(clientMessage)
        print(data.split("|")[0] + "response is sent!!")
        self.sendMessageToclient("-1")
        
    def writeCustomerDataToFile(self):
        '''
        writes user data to file
        '''
        try:
            fs = open("data.txt", 'w')
            for key in sorted(self.userData):
                val = self.userData[key]
                clientMessage = "%s|%s|%s|%s\n"%(key, val['age'], val['address'], val['phone'])
                fs.write(clientMessage)
                
        except IOError:
            print("error while reading a file")
        
        finally:
            fs.close()
            
    def sendMessageToclient(self, message):
        '''
        sends a message to the client
        '''
        self.clientObj.send(bytes(message, 'utf-8'))
        
    def receiveMessageFromclient(self):
        '''
        receives response from clients
        '''
        return self.clientObj.recv(1024)
        
    def closeClientConnection(self, data):
        '''
        closes connection with the client
        '''
        print(data.split("|")[0] + "ing client connection!!")
        self.sendMessageToclient("Good Bye !!")
        #self.writeCustomerDataToFile()
        self.clientObj.close()
        
    def runService(self):
        '''
        this is the heart of the server and it carries out the entire 
        functionality of the server by processing requests and sending 
        responses accordingly
        '''
        while True:  
            self.clientObj, self.clientAddress = self.s.accept()
            if self.userData != {}:
                self.userData = {}
            self.loadUserData()
            print ("accepted the client: ", self.clientAddress)
            self.sendMessageToclient("Congratulations you are successfully connected to the server !!!")
            
            while True:
                try:
                    clientReq = self.receiveMessageFromclient()
                    option = int(clientReq.decode('utf-8').split('-')[0])
                    data = clientReq.decode('utf-8').split('-')[1]
                    switcher = {
                        1   :  "findCustomer",
                        2   :  "addCustomer",
                        3   :  "deleteCustomer",
                        4   :  "updateCustomerAge",
                        5   :  "updateCustomerAddress",
                        6   :  "updateCustomerPhone",
                        7   :  "printReport",
                        8   :  "closeClientConnection"
                    }
                    fun = switcher.get(option,"invalid option")
                    getattr(Server, fun)(self,data)
                    if option == 8:
                        break
                except ValueError:
                    print ("error in splitting the message")
                    break
                except KeyboardInterrupt:
                    print("keyBoardInterruption while receiving a message from client")
                    break

if __name__ == '__main__':
    signal(SIGINT, handler)
    service = Server(12345)
    print("Server is listening..")
    service.runService()
    
    












