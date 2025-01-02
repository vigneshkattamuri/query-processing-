from fuzzywuzzy import fuzz

def find_matching_names(list1, list2, threshold=80):
    matches = []
    
    
    for name1 in list1:
        for name2 in list2:
           
            similarity_score = fuzz.ratio(name1, name2)
      
            if similarity_score >= threshold:
                matches.append((name1, name2, similarity_score))
    
    return matches


list1 = ['John Doe', 'Jane Smith', 'Mary Jane', 'William Brown']
list2 = ['Jon Doe', 'Jane Smtih', 'Marie Jane', 'William Browne']


matches = find_matching_names(list1, list2, threshold=80)


for match in matches:
    print(f"Match: '{match[0]}' and '{match[1]}', Similarity Score: {match[2]}")
