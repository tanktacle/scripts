#!  port_knocker.py
#! This script will connect to an IP address and a port number, then reconnect to
#!   the next port number thats given from the current connection


# Before you use me: I lack a lot of features, but I can do a great job and I'm proud of myself and I will keep improving

import math, socket, time

host = '11.111.11.111'
port = 7747
client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
client.connect(( host, port ))

# hardcoded af
time_end = time.time() + 0.3 * 1

def tcp_client():
    
    # only prints the first line of the response, so i'm grabbing all response
    # by creating a loop
    while time.time() < time_end:
        response = client.recv( 65535 )
        print ( response )
        
    enter = '\r'
    space = '\n'
    percentage = '%'
    
    # server will only accept byte-type input, so we convert it
    enter_as_bytes = str.encode( enter )
    space_as_bytes = str.encode( space )
    
    client.send( enter_as_bytes )
    
    time.sleep(1)
    
    server_response = client.recv( 65535 )
    print ( server_response )
    ports = server_response.split( space_as_bytes )
    
    # imma get rid to the b letter that wraps every goddarn response
    port_number = bytes.decode( ports[1] )

    # time to find out if it's a string, operation or number
    try:
        int( port_number )
        int_port( port_number )
    except ValueError:
        if percentage in port_number:
            op_port( port_number )
        else:
            str_port( port_number )
    

def int_port( port_number ):
    
    port = int( port_number )
    
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    client.connect(( host, port ))
        
    while time.time() < time_end:
        response = client.recv( 65535 )
        print ( response )

def str_port( port_number ):
    print ('im a string')

def op_port( port_number ):
    print ('im an op')


if __name__=='__main__':
    tcp_client()
