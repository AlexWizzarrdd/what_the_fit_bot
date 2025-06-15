# how do we get new basket info?
# else how do we continue work without image?

def get_basket_id(product_id: int):

    """
    Return a basket id according to the product id initial part. 
    Basket is a special server for product images
    """

    short_product_id = product_id // 100000
    if short_product_id < 144:
        return '01'
    if short_product_id < 288:
        return '02'
    if short_product_id < 432:
        return '03'
    if short_product_id < 720:
        return '04'
    if short_product_id < 1008:
        return '05'
    if short_product_id < 1062:
        return '06'
    if short_product_id < 1116:
        return '07'
    if short_product_id < 1170:
        return '08'
    if short_product_id < 1314:
        return '09'
    if short_product_id < 1602:
        return '10'
    if short_product_id < 1656:
        return '11'
    if short_product_id < 1920:
        return '12'
    if short_product_id < 2046:
        return '13'
    if short_product_id < 2190:
        return '14'
    if short_product_id < 2406:
        return '15'
    if short_product_id < 2622:
        return '16'
    if short_product_id < 2838:
        return '17'
    if short_product_id < 3054:
        return '18'
    if short_product_id < 3270:
        return '19'
    if short_product_id < 3486:
        return '20'
    if short_product_id < 3702:
        return '21'
    if short_product_id < 3918:
        return '22'
    if short_product_id < 4134:
        return '23'
    if short_product_id < 4350:
        return '24'
    if short_product_id < 4566:
        return '25'
    if short_product_id < 4878:
        return '26'
    if short_product_id < 5190:
        return '27'
    if short_product_id < 5502:
        return '28'
    raise ValueError("corresponding basket wasn't found")
