from staruml_classdiagramm import load_file
from staruml_classdiagramm import exist_class
from staruml_classdiagramm import exist_attribute
from staruml_classdiagramm import exist_association
from staruml_classdiagramm import exist_inheritance
from staruml_classdiagramm import version

version()

file = load_file('A33.mdj')

# tests
exist_attribute("Customer", "id", "int", "-")
exist_attribute("Customer", "firstname")
exist_attribute("Customer", "firstname", "String", "-")
exist_attribute("Customer", "lastname", "String", "-")
exist_attribute("Customer", "email", "String", "-")
exist_attribute("Customer", "telephone", "String", "-")
exist_attribute("Customer", "birthday", "LocalDate", "-")

# tests
# exist_class("Person")
# exist_attribute("Contract", "state", "char", "-", "A")
# exist_attribute("Contract", "state", "char", "-", "B")
