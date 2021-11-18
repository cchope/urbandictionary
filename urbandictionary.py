import requests

def urban_dictionary(search_term):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term":search_term}
    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "d60eca41e9msh28b55b48d2ff106p197cd0jsn0f40789fc5db"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    definitions = response['list']

    index = 0
    d = True
    while(d and index < len(definitions)):
        definition = definitions[index]['definition'].replace("[", " ")
        definition = definition.replace("]", " ")
        definition = definition.replace("\r", " ")
        definition = definition.replace("\n", " ")
        example = definitions[index]['example'].replace("[", " ")
        example = example.replace("]", " ")
        example = example.replace("\n", " ")

        print("-------------------------------------------------------------------------")
        print("Definition: "+ definition)
        print("Example:  "+ example)
        print("-------------------------------------------------------------------------")
        index +=1
        print("Would you like to see another definition?  ")
        choice = input("Press d for definition and q to quit  ")
        if(choice == "d"):
            pass
        elif(choice == "q"):
            d = False
        else:
            d = False
            # print("Would you like to see another definition? ")
            # choice = input("Press d for definition and q to quit ")



def main():
    print("Urban Dictionary")
    word = input("What word would you like to define? ")
    urban_dictionary(word)
    
main()
    


