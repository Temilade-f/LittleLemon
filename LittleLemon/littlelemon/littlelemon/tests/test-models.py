from django.tests import TestCase

class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream",price=80,inventory=100)
        self.asserEqual(item,"IceCream : 80")

class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIclient()
        Menu.objects.create(title='indomie1',price='12',inventory='1')
        Menu.objects.create(title='indomie2',price='130',inventory='1')
        Menu.objects.create(title='indomie3',price='900',inventory='1')

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.asserEqual(response.status_code,200)

        MenuItem = Menu.objects.all()
        serializer = MenuSerializer(MenuItem, many=True)
        
        self.asserEqual(response.data,serializer.data)
        