import unittest

from main import *

class MyTestCase(unittest.TestCase):
    # Языки программирования
    prog_langs = [
        Proglang(1, "C++"),
        Proglang(2, "C#"),
        Proglang(3, "Pascal"),
        Proglang(4, "Python"),
        Proglang(5, "Java"),
    ]

    # Операторы
    opers = [
        Oper(1, "Array index", "[]", 2, 1),
        Oper(2, "Increment", "++", 1, 1),
        Oper(3, "Equality", "==", 2, 2),
        Oper(4, "Null coalescing", "??", 2, 2),
        Oper(5, "Assignment", ":=", 2, 3),
        Oper(6, "Exponentiation", "**", 2, 4),
        Oper(7, "Ternary operator", "?:", 3, 5),
    ]

    opers_prog_langs = [
        OperProglang(1, 1),
        OperProglang(1, 2),
        OperProglang(1, 3),
        OperProglang(1, 4),
        OperProglang(1, 5),

        OperProglang(2, 1),
        OperProglang(2, 2),
        OperProglang(2, 5),

        OperProglang(3, 1),
        OperProglang(3, 2),
        OperProglang(3, 4),
        OperProglang(3, 5),

        OperProglang(4, 2),

        OperProglang(5, 3),

        OperProglang(6, 4),

        OperProglang(7, 1),
        OperProglang(7, 2),
        OperProglang(7, 5),
    ]

    def test_a1(self):
        one_to_many = [(op.description, op.syntax, op.arg_amount, pl.name)
                       for pl in prog_langs
                       for op in opers
                       if op.prog_lang_id == pl.id]
        self.assertEqual(a1_sol(one_to_many),
                         [('Array index', '[]', 2, 'C++'), ('Assignment', ':=', 2, 'Pascal'),
                          ('Equality', '==', 2, 'C#'), ('Exponentiation', '**', 2, 'Python'),
                          ('Increment', '++', 1, 'C++'), ('Null coalescing', '??', 2, 'C#'),
                          ('Ternary operator', '?:', 3, 'Java')])
    def test_a2(self):
        one_to_many = [(op.description, op.syntax, op.arg_amount, pl.name)
                       for pl in prog_langs
                       for op in opers
                       if op.prog_lang_id == pl.id]
        self.assertEqual(a2_sol(one_to_many),
                         [('C++', 3)])

    def test_a3(self):
        many_to_many_temp = [(pl.name, op_pl.prog_lang_id, op_pl.oper_id)
                             for pl in prog_langs
                             for op_pl in opers_prog_langs
                             if pl.id == op_pl.prog_lang_id]

        many_to_many = [(op.description, op.syntax, op.arg_amount, pl_name)
                        for pl_name, pl_id, op_id in many_to_many_temp
                        for op in opers if op.id == op_id]
        self.assertEqual(a3 _sol(many_to_many),
                         {'==': ['C++', 'C#', 'Python', 'Java'], ':=': ['Pascal']})


if __name__ == '__main__':
    unittest.main()
