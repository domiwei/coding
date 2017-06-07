class Solution(object):
    def reverseWords(self, s):
        s_list = s.split(' ')
        reverse_list = []
        for string in s_list:
            reverse_list.append(string[::-1])
        return ' '.join(reverse_list)

if __name__ == '__main__':
    sol = Solution()

    print sol.reverseWords('a book in the house')
