print("--------------number 1--------------")

l = "лфилыифнрнфыринфриннфннннннннр"
k = 1
c = 0
for i in range(len(l)-1):
	if l[i] == "н" and l[i+1] == "н":
		k += 1
	else:
		k = 1
	if k > c:
		c = k
print(f"Самая длинная последовательность: {c} \nПреобразованная строка: {l.replace("н"*c, "!"*c)}")

print("--------------number 2--------------")

# 1 способ

l = 'ываы[аыв]а(нннн)ыа{выва'
if l.find("(") and l.find(")"):
	print(((l.split("("))[1].split(")"))[0])
if l.find("[") and l.find("]"):
	print(((l.split("["))[1].split("]"))[0])
if l.find("{") and l.find("}"):
	print(((l.split("{"))[1].split("}"))[0])

# 2 способ

# l = 'ываыаыва(нннн)ыавыва'
# l1 = ""
# for i in range(len(l)-1):
# 	if l[i] == "(":
# 		while l[i] != ")":

# 	if l[i] == ")":
# 		break
# print(l1)

print("--------------number 3--------------")

l = "притмфьыао лфьлфмьдл акация фдэээдвыьжд адаптация пра"
lst = l.split(" ")
for i in lst:
	if (i[0] == "а" or i[0] == "А") and i[-1] == "я":
		print(i, end="\t")



