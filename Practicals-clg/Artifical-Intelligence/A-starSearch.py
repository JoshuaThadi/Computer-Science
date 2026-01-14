import queue as Q
from RMP import dict_gn, dict_hn  # dictionaries with distances and heuristics

start = 'Arad'
goal = 'Bucharest'
result = ''  # to store the final path and total cost

# Function to calculate f(n) = g(n) + h(n)
def get_fn(citystr):
    cities = citystr.split(",")
    gn = 0
    for ctr in range(0, len(cities) - 1):
        gn += dict_gn[cities[ctr]][cities[ctr + 1]]  # actual cost g(n)
    hn = dict_hn[cities[-1]]  # heuristic from last city
    return gn + hn

# Function to expand the next city in the queue
def expand(cityq):
    global result
    if cityq.empty():
        return
    tot, citystr, thiscity = cityq.get()
    if thiscity == goal:
        result = citystr + " :: " + str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr + "," + cty), citystr + "," + cty, cty))
    expand(cityq)

# Main function
def main():
    cityq = Q.PriorityQueue()
    cityq.put((get_fn(start), start, start))
    expand(cityq)
    print("The A* path with the total is:")
    print(result)

main()
