import wolframalpha
import pprint
import open_image 

def wolframalpha_query_text(question):
    #take user input
    query = question

    #give the registered id from wolframalpha
    app_id = "3E6X9K-K5PTR98A9R"

    #create client
    client=wolframalpha.Client(app_id)

    #print res
    res1 = ''
    res =client.query(query)
    resres = ''
    #answer = next(res.results).text
    #answer = next(res.results).text
    #print(answer)
    
    j = 0
    text = ''
    #for pod in res.pods:
     # pprint.pprint(pod)
    for pod in res.pods:
        j = j+1
        if j == 2:       
            for sub in pod.subpods:
                  text = sub.plaintext
    return text
                #print(text)
               

def wolframalpha_query_image(question):
    #take user input
    query = question

    #give the registered id from wolframalpha
    app_id = "3E6X9K-K5PTR98A9R"

    #create client
    client=wolframalpha.Client(app_id)

    #print res
    res1 = ''
    res =client.query(query)
    resres = ''
    #answer = next(res.results).text
    #answer = next(res.results).text
    #print(answer)
    i = 0
    j = 0
    #for pod in res.pods:
     # pprint.pprint(pod)
   
    for pod in res.pods:
        j = j+1
        if j == 2:       
            for sub in pod.subpods:
                i = i+1
                text = sub.plaintext
                #print(text)
                if text != None :
                    j = j-1
                else:    
                    for im in sub.img:
                        image = im.src

    if image != None:
        #print(image)
        gui = open_image.gui()
        gui.open_image(image)
    else:
        print('Image not found')
    

if __name__ == '__main__':

    while True:
        question = input("Question: ")
        text = wolframalpha_query_text(question)
        print('Result: '+text)
        wolframalpha_query_image(question)
        
        
