from mallard.customer import Customer
from mallard.searcher import Searcher
import mallard

harrex = Customer("harrex", "0414021544", "h@rrex.au")
mallard.database.add_to_table(
    "customers",
    ["id", "name", "phone", "email"],
    [harrex.id, harrex.name, harrex.phone, harrex.email],
)

searcher = Searcher(mallard.database)
print(searcher.id_search("customers", "name", "har"))
