import unittest
from BaseTypes import Container

class TestContainer(unittest.TestCase):
    def setUp(self):
        self.list1 = [1,2,3]
        self.list2 = [7,3,5]
        self.list3 = [8,9,10,11]
        self.container1 = Container(self.list1)
        self.container2 = Container(self.list2)
        self.container3 = Container(self.list3)
        self.containers = (self.container1,self.container2,self.container3)
        self.containerCeption = Container(self.containers)

    def test_creation(self):
        for i in range(len(self.container1.elements)):
            self.assertEqual(self.container1.elements[i], self.list1[i])
        for i in range(len(self.containerCeption)):
            self.assertEqual(self.containerCeption.elements[i],
                             self.containers[i])

    def test_len(self):
        self.assertEqual(len(self.container1), len(self.list1))

    def test_eq(self):
        self.assertTrue(self.container1 == self.list1)
        containerTest = Container(self.list1)
        self.assertTrue(containerTest == self.container1)
        self.assertFalse(self.container1 == self.container2)

    def test_get_by_index(self):
        for i in range(len(self.container1)):
            self.assertEqual(self.container1[i], self.list1[i])

    def test_set_by_index(self):
        for i in range(len(self.container1)):
            aux = self.list1[:]
            aux[i] = 10
            container4 = self.container1.setitem(i,10)
            self.assertIsNot(container4, self.container1)
            self.assertEqual(self.container1[i], self.list1[i])
            self.assertEqual(container4, aux)

    def test_deep_set_by_index(self):
        for i in range(len(self.container2)):
            aux = self.list2[:]
            aux[i] = 10
            containerCeption2 = self.containerCeption.setitem((1,i),10)
            self.assertEqual(containerCeption2[1], aux)

    def test_getslice(self):
        for i in range(len(self.container1)):
            for j in range(len(self.container1)):
                self.assertEqual(self.container1[i:j], self.list1[i:j])

    def test_setslice(self):
        for i in range(len(self.container1)):
            for j in range(len(self.container2)):
                aux = self.list1[:]
                aux[i:j] = self.list2[i:j]
                self.assertEqual(self.container1.setslice(i,j,aux[i:j]), aux)
        
    def test_iterable(self):
        try:
            for element in self.container1:
                pass
        except TypeError:
            self.assertTrue(False)
        self.assertTrue(True)

    def test_copy(self):
        containerTest = self.container1.copy()
        self.assertIsNot(containerTest, self.container1)
        self.assertEqual(containerTest, self.container1)

    def test_append(self):
        containerTest = self.container1.append(9)
        self.list1.append(9)
        self.assertEqual(containerTest, self.list1)
        containerTest = self.container2.append(self.container3)
        list4 = self.list2+self.list3
        self.assertEqual(containerTest, list4)

    def test_sort(self):
        containerTest = self.container2.sort()
        self.list2.sort()
        self.assertEqual(containerTest, self.list2)

    def test_in(self):
        self.assertTrue(1 in self.container1)


if __name__ == '__main__':
    unittest.main()
