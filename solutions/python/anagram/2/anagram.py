def find_anagrams(word, candidates):
    ans = []
    
    for candidate in candidates:
        if candidate.casefold() == word.casefold():
            continue
        if sorted(candidate.casefold()) == sorted(word.casefold()):
            ans.append(candidate)
        
        
    return ans

        
                
