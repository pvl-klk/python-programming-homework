# Оценка сложности каждого решения
## Рекурсивное решение (самое быстрое)
**Рассмотрим неконстантную сложность алгоритма**
```Python 
for next_column in range(N): # Сложность - O(N)
        # Сложность - O(k), где k - глубина вызова
        if all(is_safe_placement(placement, position) for placement in placements): 
            foo(placements + [position]) # Рекурсивный вызов
```
**Рассмотрим сложность алгоритма на каждой глубине рекурсии**

- Уровень 0: $N \times O(N)$
- Уровень 1: $N \times (N - 1) \times O(N)$
- Уровень 2: $N \times (N - 1) \times (N - 2) \times O(N)$
- ...
- Уровень $N-1: N \times (N-1) \times (N-2) \times \dots \times 1 \times O(N) = O(N \times N!)$

**Сложность алгоритма:** $O(N \times N!)$

---

## Переборное решение
**Рассмотрим неконстантную сложность алгоритма**
```Python
while stack: # Сложность - O(N!)
    ...
    else:
        for column in range(N): # Сложность - O(N)
            for placement_column, placement_row in placements: # Сложность - O(k), где 0 <= k <= N-1
                ...
```
**Просуммируем оценку**
1. Количество узлов в дереве поиска: $O(N!)$
2. Работа на узле: $O(N) \times O(k) = O(Nk)$
3. Итоговая сложность: $\sum_{k=0}^{N-1} \frac{N!}{(N-k)!} \times O(Nk) = O(N \times N!)$

**Сложность алгоритма:** $O(N \times N!)$
