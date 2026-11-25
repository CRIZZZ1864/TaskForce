# ticket = {

#     'Issue ID' : 101,
#     'Title' : 'Login button not working',
#     'Description' : 'Clicking Login does nothing',
#     'Priority' : 'Critical',
#     'Status' : 'In Progress',
#     'Assigned' : True
# }

# print(f" Issue ID: {ticket['Issue ID']}")
# print(f" Title : {ticket['Title']}")
# print(f" Description : {ticket['Description']}")
# print(f" Priority : {ticket['Priority']}")
# print(f" Status : {ticket['Status']}")
# print(f" Assigned : {ticket['Assigned']}")

# if ticket['Priority'] == 'Critical':

#     print('Immediate Action Needed')

# elif ticket['Priority'] == 'High':
    
#     print('This issue should be handled soon')
    
# else :
    
#     print('Normal Priority Issue')    
    
    
    
# if ticket['Status']== 'Open' :
    
#         print('This ticket needs to be started.')
        
# elif ticket['Status']=='In Progress':
    
#     print('This ticket is currently being worked on.')  
    
# elif ticket['Status']=='Resolved':
    
#     print('This ticket has been resolved.') 
    
# else :
    
#     print('Unknown Ticket Status')             


# if ticket['Priority']=='Critical' and ticket['Status'] != 'Resolved':
    
#     print('This ticket requires urgent attention!')
    
# else :
    
#         print('No urgent action required.')

# statuses = ['Open', 'In Progress', 'Resolved', 'Open', 'In Progress']

# for status in statuses:

#     if status== 'Open':
        
#         print('Ticket waiting to be started')
        
#     elif status== 'In Progress':
        
#         print('Ticket currently being worked on') 
        
#     elif status=='Resolved' :
        
#         print('Ticket completed')  

# open_count = 0
# progress_count = 0
# resolved_count = 0

# for status in statuses:
    
#     if status=='Open':
        
#         open_count += 1
        
#     elif status=='In Progress':
        
#         progress_count += 1
        
#     elif status=='Resolved':
        
#         resolved_count+=1       
        
# print(f'Open tickets: {open_count}')
# print(f'In Progress tickets: {progress_count}')
# print(f'Resolved tickets: {resolved_count}')

# def check_ticket_status(status):
    
#     if status=='Open':
#         print('Ticket waiting to be started.')
        
#     elif status=='In Progress':
#         print('Ticket currently being worked on.')
        
#     elif status=='Resolved':
#         print('Tickets Completed.')
        
#     else:
#         print('Unknown Ticket Status.')            
        
        
# for status in statuses:
    
    # check_ticket_status(ticket['Status'])        
    
 
# def is_ticket_urgent(priority):
     
#      if priority=='Critical':
         
#          return True
     
#      else :
#          return False
     
    
# urgent = is_ticket_urgent(ticket['Priority'])           

# print(urgent)


tickets = [
    {
        'Issue ID': 101,
        'Title': 'Login button not working',
        'Priority': 'Critical',
        'Status': 'Open'
    },
    {
        'Issue ID': 102,
        'Title': 'Page loading slowly',
        'Priority': 'High',
        'Status': 'In Progress'
    },
    {
        'Issue ID': 103,
        'Title': 'Broken image on homepage',
        'Priority': 'Low',
        'Status': 'Resolved'
    },
    {
        'Issue ID': 104,
        'Title': 'Server connection failure',
        'Priority': 'Critical',
        'Status': 'In Progress'
    },
    {
        'Issue ID': 105,
        'Title': 'Password reset issue',
        'Priority': 'Medium',
        'Status': 'Open'
    }
]


for ticket in tickets:
    
    print(f"Issue ID: {ticket['Issue ID']}")
    print(f"Title: {ticket['Title']}")
    print(f"Priority: {ticket['Priority']}")
    print(f"Status: {ticket['Status']}")


open_count = 0
progress_count = 0
resolved_count = 0

for ticket in tickets:
    
    if ticket['Status']=='Open':
        
        open_count += 1 
        
    elif ticket['Status']=='In Progress':
        
        progress_count += 1
        
    elif ticket['Status']=='Resolved':
        
        resolved_count += 1        
        
print(open_count+progress_count+resolved_count)         

for ticket in tickets :
    
    if ticket['Priority']== 'Critical':
        
        print(ticket['Title'])
        
        
def is_ticket_urgent(priority):
      
        return priority == 'Critical'
    
    
for ticket in tickets:
    
    urgent = is_ticket_urgent(ticket['Priority'])    
    if urgent == True:
        
        print(ticket['Issue ID'])
        print(ticket['Title'])
    