#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://lark-parser.readthedocs.io/en/latest/how_to_use.html
# https://github.com/lark-parser/lark/tree/master/lark
# https://github.com/lark-parser/lark/blob/master/lark/grammars/python.lark
# https://lark-parser.readthedocs.io/en/latest/_static/lark_cheatsheet.pdf
# https://www.lark-parser.org/ide/
# https://flit.pypa.io/en/stable/
# https://proglib.io/p/kompilyator-svoimi-rukami-kratkiy-gid-dlya-nachinayushchih-2024-08-06
# https://habr.com/ru/articles/776438/

import os
import sys
from lark import Lark
import numpy as np
from scipy.stats import chisquare

BASE_DIR = os.path.dirname(__file__)
VARS_FILE = os.path.join(BASE_DIR, "..", "variables.txt")

with open(VARS_FILE, encoding='utf-8') as f:
    variables = f.read()
VARIABLES = set(variables.split('\n') + ['𐃰'])


class AvtandilProgram():
    
    def __init__(self):
        """Инициализация класса, создание рабочей переменной"""
        self.vars = {'𐃰': ''}
        
    def exception(self, msg):
        """Вывод исключения, начинается с символа ☹"""
        sys.exit('☹  {}'.format(msg))
        
    def float_polish(self, value):
        value = str(value)
        value = value.replace('.', ',')
        if value.split(',')[1] == '0':
            return value.split(',')[0]
        else:
            return value

    def assign_var(self, nv):
        """Присваивание переменной, имя которой хранится в словаре vars,
        значения по ключу имени; тут же проверка разрешенного имени"""
        try:
            name, value = nv.children
            name = str(name)
            value = str(value)
        except:
            name, value = nv
            if type(value) == float:
                value = self.float_polish(value)
        if name not in VARIABLES:
            self.exception('Запрещенное имя переменной: {}'.format(name))
        self.vars[name] = value
        return value

    def var(self, name):
        return self.vars[name]
    
    def summation(self, num1, num2):
        return float(num1) + float(num2)
    
    def subtraction(self, num1, num2):
        return float(num1) - float(num2)
    
    def multiplication(self, num1, num2):
        return float(num1) * float(num2)
    
    def division(self, num1, num2):
        if num2 == '0':
            return '∅'
        return float(num1) / float(num2)
    
    def float_true(self, val):
        if ',' in val:
            return val.replace(',', '.')
        else:
            return val
    
    def run_instruction(self, t):
        if t.data == 'operator':
            oper = str(t.children[0])
            numbers = []
            val = 0
            for num in t.children[1:]:
                num = str(num)
                if num == '∅':
                    val = '∅'
                    break
                else:
                    numbers.append(self.float_true(num))
            if not val:
                for i,n in enumerate(numbers):
                    if not i:
                        val = n
                    elif val == '∅':
                        break
                    else:
                        val = {'ᛝ': self.summation,
                               'ᚸ': self.subtraction,
                               'ᛪ': self.multiplication,
                               'ᛄ': self.division}[oper](val, n)
            self.assign_var(('𐃰', val))
    
        elif t.data == 'chi_sq':
            square_values = [float(val) for val in t.children]
            ch = chisquare(square_values)
            val = ch.pvalue
            self.assign_var(('𐃰', val))
        
        elif t.data == 'percent':
            number1, number2 = t.children
            val = float(number2) / float(number1) * 100
            self.assign_var(('𐃰', val))
    
        elif t.data == 'corr':
            vec1, vec2 = t.children
            array1 = np.array([float(val) for val in vec1.children])
            array2 = np.array([float(val) for val in vec2.children])
            val = np.corrcoef(array1, array2)[0][1]  
            self.assign_var(('𐃰', val))
            
        elif t.data == 'assign_var':
            self.assign_var(t)
            
        elif t.data == 'condition_digit':
            self.condition_digit(t)
            
        elif t.data == 'condition_even':
            self.condition_even(t)
    
        else:
            raise SyntaxError('☹ Неизвестная инструкция: %s' % t.data)
    
    def condition_digit(self, cnd):
        condition, value1, value2 = cnd.children
        value1 = float(self.float_true(value1))
        value2 = float(self.float_true(value2))
        
        if condition == '𐄷':
            if value1 == value2:
                return True
            else:
                return False
                                                 
        elif condition == '𑚐':
            if value1 != value2:
                return True
            else:
                return False
                                                 
        elif condition == '≈':
            if 0 <= value1 - value2 <= 1 or 0 <= value2 - value1 <= 1:
                return True
            else:
                return False
        
        #elif condition == '≉':
            #value1 = float(float_true(value1))
            #value2 = float(float_true(value2))
            #if 0 > value1 - value2 >= 1 and value2 - value1 >= 1:
                #return True
            #else:
                #return False
        
        elif condition == 'អ':
            if value1 > value2:
                return True
            else:
                return False
                
    def condition_even(self, cnd):
        condition, value1 = cnd.children
        value1 = float(self.float_true(value1))
        
        if condition == '᭕':
            if value1 % 2 == 0:
                return True
            else:
                return False
                
        elif condition == 'ゅ':
            if value1 % 2 != 0:
                return True
            else:
                return False
            
            
            

def main():
    with open(os.path.join(BASE_DIR, 'avtandil.ebnf'), encoding='utf-8') as f:
        grammar = f.read()
    
    with open(os.path.join(BASE_DIR, 'script.avdl'), encoding='utf-8') as f:
        avdl_code = f.read()
    
    with open(os.path.join(BASE_DIR, '..', 'variables.txt'), encoding='utf-8') as f:
        variables = f.read()
    variables = set(variables.split('\n'))
    
    
    parser = Lark(grammar, parser="lalr" )
    parse_tree = parser.parse(avdl_code)
    avt = AvtandilProgram()
    
    # for inst in parse_tree.children:
        # for tr in inst.children:
            # print(tr)
            # for token in tr.children:
                # if token.type == 'WORD' and token.value not in VARIABLES:
                    # print('☹ Запрещенное имя переменной:', token.value)
    
    # avt.run_instruction(parse_tree.children[0])
    # print(avt.vars['𐃰'])
    
    avt.run_instruction(parse_tree.children[1])
    print(avt.vars['𐃰'])
    
    # avt.run_instruction(parse_tree.children[2])
    # print(avt.vars['𐃰'])
    
    # avt.run_instruction(parse_tree.children[3])
    # print(avt.vars['𐃰'])
    
    # print(parse_tree.children[4].children)
    # ora1, ora2 = parse_tree.children[4].children
    # print(ora1.type)
    
    # avt.run_instruction(parse_tree.children[4])
    # print(avt.vars)
    
    # avt.assign_var(parse_tree.children[4])
    # print(avt.vars)
    
    # print(avt.condition_digit(parse_tree.children[5]))
    
    # print(avt.condition_digit(parse_tree.children[6]))
    
    # avt.run_instruction(parse_tree.children[7])
    # print(avt.vars['𐃰'])
    
    # avt.assign_var(parse_tree.children[8])
    # print(avt.vars)
    
    return 0

if __name__ == '__main__':
    main()
