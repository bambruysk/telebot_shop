from django.shortcuts import render

# Create your views here.


class TelegramViewProduct():
    def __init__(self,product_id):
        self.product = get_product_by_id(product_id)
    
    def get_images(self):
        images = get_images_for_product(self.product)
        return images

    def get_text(self):
        text = f"""{self.product.name}
            Цена: {self.product.price}

            {self.product.descriton}
            """
        return text
    def get_buttons(self):
        return None

