l = [11, 45, 1, 2, 4, 6, 1]
print(l)

l.append(7)             # append() method appends the given value at the end of the list
l.sort()                # sort() method sorts the list in the ascending order
l.sort(reverse=True)    # reverses the sorting or simply returns the list in descending order
l.reverse()             # in whichever order the list is by default the reverse() method reverses the default order
print(l.index(1))       # index(<index>) method returns the element at the given index in a list
print(l.count(1))       # count() method returns the count of the given element in a list
l.insert(1, 899)        # the insert(<index>, <value>) method insertes given value at the given index

s = [900, 100, 1100]
l.extend(s)             # the extend(<list>) method extends the list with a given list
k = l + s               # this will concatinate (add) the elements of l and s and put it in a new list k
print(k)

m = l
m[0] = 0                # here most beginners think the m is creating a new list with list l and than we're changing 0th element of the m to 0 but the m is giving a reference of the list l so any change in the m will effect to the original list l

m = l.copy()            # now this fixes the problem we encountered just before the copy() method copies the original list to the new list

print(l)