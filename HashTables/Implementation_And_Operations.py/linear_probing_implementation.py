'''
Description:
Closed Hashing/Probing/Open Addressing is one of the popular hash table implementations in which every key in the hash table maps to a single element. In case of a collission, we call the rehash() function and look for other empty spots in the hash table to insert the value.

Linear Probing is one such probing algorithms and it's named so because of its rehash function.

Hash Function:
   hash(num) = num % size_table

Rehash Function:
   rehash(num,i) = (hash(num)+k) % size_table
   **FUN FACT: It's called the linear probing approach because of this rehash function. It will always look in the next bucket in case of a collission.

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
   load_function > size_table/3 collissions ==> RESIZE,
   (load_function = if more than size_table/3 collissions occur during an insert operation, resize)

Status: Resizing Pending
'''

class ClosedHash:
    def __init__(self,n):
        self.__n = n
        self.__table = []
        for i in range(n):
            self.__table.append(None)
        return

    def __str__(self):
        ret_str = ""
        for indices,items in enumerate(self.__table):
            temp_str = "Row "+str(indices)+" "+str(items)+"\n"
            ret_str+=temp_str

        return ret_str

    def hash(self,i):
        return (i%self.__n)

    def rehash(self,i,k):
        return (self.hash(i%self.__n)+k)%self.__n

    def insert(self,num):
        for k in range(self.__n):
            key = self.rehash(num,k)
            if self.__table[key] == num:
                return
            if self.__table[key] == None:
                self.__table[key] = num
                return

        print("TABLE FULL")


    def member(self,num):
        for k in range(self.__n):
            key = self.rehash(num,k)
            if self.__table[key] == num:
                return True

        return False

    def delete(self,num):
        for k in range(self.__n):
            key = self.rehash(num,k)
            if self.__table[key] == num:
                self.__table[key] = None
                return


##DRIVER
if __name__ == '__main__':
	hash_object = ClosedHash(10)
	hash_object.insert(5)
	hash_object.insert(8)
	hash_object.insert(25)
	print(hash_object)
	print(hash_object.member(8))
	hash_object.delete(8)
	print(hash_object.member(8))
	print(hash_object)
