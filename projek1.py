import numpy as np
import time
import matplotlib.pyplot as plt

def bubble_sort(data):
    n = len(data)
    langkah = 0
    for i in range(n):
        for j in range(0, n-i-1):
            langkah += 1  
            if data[j]  > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data, langkah

def linear_search(data, target):
    langkah = 0
    for index, value in enumerate(data):
        langkah += 1  
        if value == target:
            return index, langkah
    return -1, langkah

def experiment():
    data_sizes = [1, 10, 100, 1000,2000,3000,4000,5000]
    bubble_sort_times = []
    linear_search_times = []                 

    for size in data_sizes:
        if size == 10:
            data_input = input(f"Masukkan 10 angka (pisahkan dengan spasi) untuk ukuran data {size}: ")
            data = list(map(int, data_input.split()))
            if len(data) != 10:
                print("Anda harus memasukkan tepat 10 angka.")
                return
        elif size == 1:
            value = int(input(f"Masukkan angka untuk data ke 1 dari ukuran {size}: "))
            data = [value]
        else:
            data = np.random.choice(range(size*10), size, replace=False)

        start_time = time.perf_counter()
        sorted_data, langkah_sort = bubble_sort(data.copy())
        end_time = time.perf_counter()
        bubble_sort_time = end_time - start_time
        bubble_sort_times.append(bubble_sort_time)

        while True:
            target = int(input(f"Masukkan target untuk ukuran data {size} (data: {sorted_data[:10]}...): "))
            if target in sorted_data:
                break
            else:
                print("Target tidak ada dalam data. Silakan masukkan target yang valid.")

        start_time = time.perf_counter()
        index, langkah_search = linear_search(sorted_data, target)
        end_time = time.perf_counter()
        linear_search_time = end_time - start_time
        linear_search_times.append(linear_search_time)

        print(f"\n{'-'*50}")
        print(f"Ukuran Data: {size}")
        print(f"Data Acak: {data[:10]}...")
        print(f"Data Terurut: {sorted_data[:10]}...")
        print(f"Jumlah langkah Bubble Sort: {langkah_sort}, Waktu: {bubble_sort_time:.6f} detik")
        print(f"Target: {target}")
        print(f"Index target: {index}, Jumlah langkah Linear Search: {langkah_search}, Waktu: {linear_search_time:.6f} detik")
        print(f"{'-'*50}\n")
        

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))  

    ax1.plot(data_sizes, bubble_sort_times, marker='o', label='Waktu Bubble Sort', color='blue')
    ax1.set_xscale('log') 
    ax1.set_title('Waktu Eksekusi Bubble Sort', fontsize=14, pad=15) 
    ax1.set_xlabel('Ukuran Data (Log Scale)', fontsize=12)
    ax1.set_ylabel('Waktu Eksekusi (detik)', fontsize=12)
    ax1.set_xticks(data_sizes)
    ax1.get_xaxis().set_major_formatter(plt.ScalarFormatter())  
    ax1.grid(True)
    ax1.legend(fontsize=10)  

    for i in range(len(data_sizes)):
        ax1.annotate(f"{bubble_sort_times[i]:.6f}", (data_sizes[i], bubble_sort_times[i]), 
                     textcoords="offset points", xytext=(0, 5), ha='center', fontsize=10)

    ax2.plot(data_sizes, linear_search_times, marker='o', label='Waktu Linear Search', color='orange')
    ax2.set_xscale('log') 
    ax2.set_title('Waktu Eksekusi Linear Search', fontsize=14, pad=15) 
    ax2.set_xlabel('Ukuran Data (Log Scale)', fontsize=12)
    ax2.set_ylabel('Waktu Eksekusi (detik)', fontsize=12)
    ax2.set_xticks(data_sizes)
    ax2.get_xaxis().set_major_formatter(plt.ScalarFormatter())  
    ax2.grid(True)
    ax2.legend(fontsize=10)  
   
    for i in range(len(data_sizes)):
        ax2.annotate(f"{linear_search_times[i]:.6f}", (data_sizes[i], linear_search_times[i]), 
                     textcoords="offset points", xytext=(0, 5), ha='center', fontsize=10)

    plt.tight_layout(pad=3)  
    plt.show()
    print("TERIMA KASIH SUDAH MENJALANKAN PROGRAM INI")

experiment()