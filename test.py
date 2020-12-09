from py_expression_eval import Parser
parser = Parser()
print(parser.parse('1+2-1*2').evaluate({}))