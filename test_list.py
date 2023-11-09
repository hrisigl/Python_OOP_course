class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest




class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3)

    def test_init_all_ints(self):
        self.assertEqual(3, len(self.list.get_data()))

    def test_get_data_returns_correctly(self):
        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_add_el_not_type_int_raises(self):
        self.assertEqual(3, len(self.list.get_data()))

        possible_els = [{}, [], "asd", 3.2]

        for el in possible_els:
            with self.assertRaises(ValueError) as ve:
                self.list.add(el)
            self.assertEqual("Element is not Integer", str(ve.exception))

        self.assertEqual(3, len(self.list.get_data()))

    def test_add_if_el_is_int_returns_list(self):
        self.assertEqual(3, len(self.list.get_data()))

        self.list.add(1)
        self.assertEqual(4, len(self.list.get_data()))
        self.assertEqual([1, 2, 3, 1], self.list.get_data())

        self.list.add(2)
        self.assertEqual(5, len(self.list.get_data()))
        self.assertEqual([1, 2, 3, 1, 2], self.list.get_data())

    def test_remove_index_if_bigger_raises(self):
        self.assertEqual(3, len(self.list.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_correct_and_returns(self):
        self.assertEqual(3, len(self.list.get_data()))

        res = self.list.remove_index(0)

        self.assertEqual(2, len(self.list.get_data()))
        self.assertEqual([2, 3], self.list.get_data())
        self.assertEqual(1, res)

    def test_get_incorrect_index_raises(self):
        self.assertEqual(3, len(self.list.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_correct(self):
        self.assertEqual(3, len(self.list.get_data()))

        res = self.list.remove_index(1)
        self.assertEqual(2, res)

    def test_insert_index_not_correct_raises(self):
        self.assertEqual(3, len(self.list.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.list.insert(10, 1)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_if_el_not_int(self):
        self.assertEqual(3, len(self.list.get_data()))

        possible_els = [{}, [], "asd", 3.2]

        for el in possible_els:
            with self.assertRaises(ValueError) as ve:
                self.list.insert(1, el)
            self.assertEqual("Element is not Integer", str(ve.exception))

        self.assertEqual(3, len(self.list.get_data()))

    def test_insert_correct(self):
        self.assertEqual(3, len(self.list.get_data()))

        self.list.insert(0, 1)
        self.assertEqual(4, len(self.list.get_data()))
        self.assertEqual([1, 1, 2, 3], self.list.get_data())

        self.list.insert(0, 1)
        self.assertEqual(5, len(self.list.get_data()))
        self.assertEqual([1, 1, 1, 2, 3], self.list.get_data())

    def test_get_biggest(self):
        self.assertEqual(3, len(self.list.get_data()))
        self.assertEqual([1, 2, 3], self.list.get_data())

        res = self.list.get_biggest()
        self.assertEqual(3, res)

    def test_get_index(self):
        self.assertEqual(3, len(self.list.get_data()))
        self.assertEqual([1, 2, 3], self.list.get_data())

        res = self.list.get_index(3)
        self.assertEqual(2, res)

if __name__ == "__main__":
    unittest.main()