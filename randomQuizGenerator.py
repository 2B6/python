import random, os

#initializing
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
   'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
   'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
   
count_file=0
list_name_q=[]
list_name_a=[]


#making folders
path = 'C:\\Users\\12931\\Desktop'
os.chdir(path)
print(os.path.exists('quiz'))
if not(os.path.exists('quiz')):
    os.makedirs('quiz\Q');
    os.makedirs('quiz\A');

    
# Generate 35 quiz files.
for quizNum in range(35):

    # TODO: Write out the header for the quiz.
    name_q = ''.join(['quiz\Q\Question', str(count_file),'.txt'])
    name_a = ''.join(['quiz\A\Answer', str(count_file),'.txt'])
    list_name_q = list_name_q + [name_q]
    list_name_a = list_name_a + [name_a]

    #clear previous results
    fileQ = open(list_name_q[count_file], 'w')
    fileA = open(list_name_a[count_file], 'w')
    fileQ.write(list_name_q[count_file] + '\n name:  \t date:    \t\n'+'give capitals for following states\n')
    fileA.write('This is answer sheet for file '+list_name_q[count_file])
    fileQ.close()
    fileA.close()
    
    # TODO: Create the quiz and answer key files.
    fileQ = open(list_name_q[count_file], 'a')
    fileA = open(list_name_a[count_file], 'a')
    
    

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    
    # TODO: Loop through all 50 states, making a question for each.
    
    #capital is dict, state is list of state names, rand_state is element in state as list
    for rand_state in states:
        #making options
        option_list = [states[random.randint(0, 49)]] + [states[random.randint(0, 49)]] + [states[random.randint(0, 49)]] + [capitals[rand_state]]
        random.shuffle(option_list)
        #making questions
        single_question = '\n\n' + rand_state + '\n'

        for ele in option_list:
            single_question = single_question + '   \t.' + ele
            
        #print(single_question)
        #making solution
        single_solution = '\n'+ capitals[rand_state] + '\n'
        
        fileQ.write(single_question)
        fileA.write(single_solution)
        
        
        
    fileQ.close()
    fileA.close()
    
    count_file=count_file+1