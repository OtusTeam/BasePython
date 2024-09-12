from views.products.crud import ProductsStorage


# pylint:disable=use-implicit-booleaness-not-comparison
class TestProductsStorage:

    def test_get_empty(self):
        storage = ProductsStorage()
        assert storage.get() == []
