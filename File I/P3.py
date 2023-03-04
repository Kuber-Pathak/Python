for i in range(2, 11):
    with open(f"File I/tables/Multiplication_table_of{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}x{j}={i*j}\n")
