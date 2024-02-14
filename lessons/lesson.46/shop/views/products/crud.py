# from sqlalchemy import delete

from models import db, Product


def get_products_list() -> list[Product]:
    return Product.query.all()


def get_product_by_id(product_id: int) -> Product:
    return Product.query.get_or_404(
        product_id,
        f"product #{product_id} not found",
    )


def create_product(name: str) -> Product:
    product = Product(
        name=name,
    )
    db.session.add(product)
    db.session.commit()
    return product


def delete_product(product: Product) -> None:
    # product = get_product_by_id(product_id)
    db.session.delete(product)
    db.session.commit()
    # del_stmt = delete(Product).where(Product.id == product_id)
    # db.session.execute(del_stmt)
    # db.session.commit()
