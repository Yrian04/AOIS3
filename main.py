from src.formula.normal_logical_formula_parser import NormalLogicalFormulaParser
from src.reducer.normal_logical_formula_reducer import NormalLogicalFormulaReducer
from src.reducer.calculated_method.calculated_method_reduce_strategy import CalculatedMethodReduceStrategy
from src.reducer.calculated_table_method.calculated_table_method_reduce_strategy import CalculatedTableMethodReduceStrategy
from src.reducer.table_method.table_method_reduce_strategy import TableMethodReduceStrategy

# (!a|!b|!c|!d)&(!a|!b|c|d)&(!a|b|!c|!d)&(!a|b|c|d)&(a|!b|!c|!d)&(a|!b|c|!d)&(a|b|!c|!d)&(a|b|c|d)
# (!a|!b|c)&(!a|b|c)&(!a|b|!c)&(a|b|!c)

string = input("Enter full normal formula: ")
parser = NormalLogicalFormulaParser('&', '|', '!')
formula = parser.parse(string)

print("Calculated method:")
reducer = NormalLogicalFormulaReducer(CalculatedMethodReduceStrategy())
reduced_formula = reducer.reduce(formula)
print(reduced_formula)

print("Calculated table method:")
reducer.reduce_strategy = CalculatedTableMethodReduceStrategy()
reduced_formula = reducer.reduce(formula)
print(reduced_formula)

print("Table method:")
reducer = TableMethodReduceStrategy()
reduced_formula = reducer.reduce(formula)
print(reduced_formula)

