

def find_min(string):
    hashmap = {}
    letter_set = []
    for i, letter in enumerate(string):
        if letter in hashmap:
            hashmap[letter].append(i)
        else:
            letter_set.append(letter)
            hashmap[letter] = [i]

    print hashmap
    def dfs(pos = 0, now_str = [], min_str = None):
        if pos == len(letter_set):
            final_list = sorted(now_str, key=lambda x: x[1])
            #print now_str, final_list
            final_str = ''
            for letter, pos in final_list:
                final_str += letter
            #print final_str
            if not min_str or final_str < min_str:
                return final_str
            else:
                return min_str

        now_letter = letter_set[pos]
        for index in hashmap[now_letter]:
            now_str.append((now_letter, index))
            min_str = dfs(pos+1, now_str, min_str)
            now_str.pop()
        return min_str

    return dfs()

if __name__ == '__main__':
    string = 'cbacdcbc'
    print find_min(string)
