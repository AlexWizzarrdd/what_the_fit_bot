# from core.parser.product import SortType
# from core.parser.wb_parse import wb_parse
# from core.parser.criteria import Criteria

# products_data = wb_parse('синяя футболка', SortType.PRICEDOWN.value, 5, 
#                          True, Criteria.has_feedbacks)

from core.telegram import main

main.main()
