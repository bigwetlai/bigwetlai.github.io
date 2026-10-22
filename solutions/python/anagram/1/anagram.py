def find_anagrams(word, candidates):
    ans = []
    
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue

        candidate_list = list(candidate.lower())
        candidate_status = True
        for char in word.lower():
            if char in candidate_list:
                candidate_list.remove(char)
            else:
                candidate_status = False
                pass
        if not candidate_list and candidate_status:
            ans.append(candidate)
        
        
    return ans

        
                
