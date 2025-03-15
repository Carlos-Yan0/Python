from random import randint

nums = (randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10))

#ordem = sorted(nums)
#maior = ordem[4]
#menor = ordem[0]

#print(f"Os números sorteados foram: {nums}")
#print(f"O maior número é {maior}")
#print(f"O menor número digitado é {menor}")

#outra maneira de se fazer logo abaixo

print("Números sorteados: ", end = "")
for c in nums:
    print(c, end = " ")

print(f"\nO maior número é {max(nums)}")
print(f"O menor número é {min(nums)}")


