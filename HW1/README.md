# Homework 1

## Purpose:

本次作業主要是要練習列運算和矩陣相乘

## Summary

希望透過列運算和矩陣相乘來解決一些小問題

- Problem 1:  
主要是利用列運算來偵測 graph 中是否有 cycle。具體過程如下:  
  
  1. 先將 graph 用矩陣來表示 (用-1、0、1來表示)  
  2. 沿著每個 column 中的每個 row 去找到第一個元素 1，再透過列運算 (addition) 與該 column 中的 -1 那些 row 個別相加，並將相加過後的結果放到矩陣最後面且刪掉 row 為 1 的那列  
  3. 檢查是否有整列為 0，如果有則代表這個 graph 有 cycle

- Problem 2:  
主要是利用矩陣相乘來偵測 graph 中是否有 cycle。具體過程如下:  
  
  1. 先將 graph 用矩陣來表示 (用0、1來表示)  
  2. 將 graph_new 跟 graph 做矩陣相乘，其中一開始 graph_new 就是 graph  
  3. 檢查對角線是否有大於等於 1 的元素，如果有代表有 cycle，反之亦然

要完成這次的作業其實不難，但比較困難的是為什麼這樣做就可以去判斷 graph 中是否有 cycle。目前的理解是在做矩陣乘法或列運算的時候也在對 graph 作變更，導致某些情況出現時就帶表著圖形有 cycle。這部份如果有人知道為什麼，再麻煩跟我分享

## Reference

- [原始課程作業說明](https://docs.google.com/presentation/d/17AuUeKUYrFjQYipT7ixQfETZO0D0TD13YampykFZCww/edit#slide=id.p13)