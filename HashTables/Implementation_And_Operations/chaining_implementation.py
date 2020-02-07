'''
Description:
Open Hashing/Chaining/Bucketing is one of the popular hash table implementations in which every key in the hash table maps to a list of values. In case of a collission, the value is appended to the end of the list.

Hash Function:
   hash(num) = num % size_table

Bucket Data Structure:
   Python Lists

Average Time Complexity:
	Search = O(1)
	Insertion  = O(1)
	Deletion  = O(1)
	Resize = O(n)

Worst Time Complexity:
   Search - O(n)
   Insertion - O(n)
   Deletion - O(n)
   Resize = O(n)

Resizing:
   load_function > 0.6 ==> RESIZE,
   (load_function = no.of.elements/no.of.buckets)

Status: Resizing Pending
'''
class OpenHash:
    def __init__(self,n):
        self.__n = n
        self.__table = []
        for i in range(n):
            self.__table.append([])
        return
    def __str__(self):
        ret_str = ""
        for index,val in enumerate(self.__table):
            if len(val) == 0 :
                my_str = "Row "+str(index)+" []\n"
                ret_str+=my_str
            else:
                my_str = "Row "+str(index)+" "+str(val)+"\n"
                ret_str+=my_str

        return ret_str

    def hash(self,i):
        return (i%self.__n)

    def insert(self,num):
        hash_val = self.hash(num)
        inner_table = self.__table[hash_val]
        for indices,vals in enumerate(inner_table):
            if vals == num:
                inner_table.pop(indices)
                break

        inner_table.append(num)

    def member(self,num):
        hash_val = self.hash(num)
        inner_table = self.__table[hash_val]
        for items in inner_table:
            if items == num:
                return True
        return False

    def delete(self,num):
        hash_val = self.hash(num)
        inner_table = self.__table[hash_val]
        for index,items in enumerate(inner_table):
            if items == num:
                inner_table.pop(index)


##DRIVER
if __name__ == '__main__':
	hash_object = OpenHash(10)
	hash_object.insert(5)
	hash_object.insert(8)
	hash_object.insert(25)
	print(hash_object)
	print(hash_object.member(8))
	hash_object.delete(8)
	print(hash_object.member(8))
	print(hash_object)
