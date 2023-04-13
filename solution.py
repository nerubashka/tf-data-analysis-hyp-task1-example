import pandas as pd
import numpy as np


chat_id = 460109099 # Ваш chat ID, не меняйте название переменной
alpha = 0.06

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    _, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative="larger")
    return p_value < alpha # Ваш ответ, True или False
