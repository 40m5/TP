euros = [50, 20, 35, 100, 80]

dollars = map(lambda x: f"{x * 1.10}$" , euros )

print(list(dollars))