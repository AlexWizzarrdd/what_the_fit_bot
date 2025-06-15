# functions which returns True if the criterion is met

class Criteria:

    """
    Different search criteria.

    Attributes:
    has_feedbacks (function): return True if product feedbacks > 0. 
    """

    has_feedbacks = lambda product: product.product_data["nmFeedbacks"] > 0
