import collections as coll

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        num_tickets = 0
        tickets_hash = coll.defaultdict(list)
        for travelFrom, travelTo in sorted(tickets):
            tickets_hash[travelFrom].append(travelTo)
            num_tickets += 1

        if num_tickets == 0:
            return []

        path = []
        def travelling(cityFrom, num_tickets):
            if num_tickets == 0:
                path.append(cityFrom)
                return True

            for i in xrange(len(tickets_hash[cityFrom])):
                cityTo = tickets_hash[cityFrom].pop(i)
                if travelling(cityTo, num_tickets - 1) == True:
                    path.append(cityFrom)
                    return True
                else:
                    tickets_hash[cityFrom].insert(i, cityTo)

            return False

        # travelling!
        begin = 'JFK'
        travelling(begin, num_tickets)
        path.reverse()
        return path

if __name__ == '__main__':
    sol = Solution()
    #tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print sol.findItinerary(tickets)
    tickets = [["JFK","SFO"]]
    print sol.findItinerary(tickets)
    tickets = []
    print sol.findItinerary(tickets)

