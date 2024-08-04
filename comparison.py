import search_boyer_moore as bms
import search_kmp as kmp
import search_rabin_karp as rks
from timeit import timeit

ex_1 = "Цільовий елемент порівнюється із середнім"
ex_2 = "Аналіз останніх досліджень і публікацій"

def print_timing(algorithm_name, execution_time, result):
    print(f"{algorithm_name}: {execution_time:.6f} секунд, результат: {result}")

for file in ["Text 1.txt", "Text 2.txt"]:
    with open(file, "r", encoding="windows-1251") as f:
        text = f.read()

        for str in [ex_1, ex_2]:
            print(f"\nФайл: {file}, Рядок: {str}\n")
            print_timing(
                ">>>БОЄР-МУР",
                timeit("bms.search_boyer_moore(text, str)", globals=globals(), number=1),
                bms.search_boyer_moore(text, str),
            )
            print_timing(
                ">>>КНУТ-МОРРІС-ПРАТТ",
                timeit("kmp.search_kmp(text, str)", globals=globals(), number=1),
                kmp.search_kmp(text, str),
            )
            print_timing(
                ">>>РАБІН-КАРП",
                timeit("rks.search_rabin_karp(text, str)", globals=globals(), number=1),
                rks.search_rabin_karp(text, str),
            )