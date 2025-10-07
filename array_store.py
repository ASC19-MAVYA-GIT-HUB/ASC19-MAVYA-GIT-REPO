class ArrayStore:
    def __init__(self):
        self.data = []

    def accept_data(self, nums):
        self.data = nums[:10]

    def display_for(self):
        for num in self.data:
            print(num, end=' ')
        print()

    def display_while(self):
        i = 0
        while i < len(self.data):
            print(self.data[i], end=' ')
            i += 1
        print()

    def sort_data(self):
        self.data.sort()

    def count_occurrence(self, num):
        return self.data.count(num)

    def insert_at(self, num, pos):
        self.data.insert(pos, num)

    def get_unique(self):
        return list(set(self.data))

# Test
store = ArrayStore()
store.accept_data([9, 2, 2, 9, 10, 9, 5, 6, 7, 8])
print("For Loop Display:")
store.display_for()
print("While Loop Display:")
store.display_while()
store.sort_data()
print("Sorted:", store.data)
print("Count of 9:", store.count_occurrence(9))
store.insert_at(99, 3)
print("After Insert:", store.data)
print("Unique Elements:", store.get_unique())