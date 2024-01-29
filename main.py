db_old = []

with open('numbers_old.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        db_old.append(line.strip())
already = 0
with open('numbers_new.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        a = '7' + line.replace(' ', '').replace('-', '').strip()
        if a in db_old:
            already += 1
        else:
            db_old.append(a)

with open('numbers_new_db_full_clear.txt', 'a', encoding='utf8') as f:
    for i in db_old:
        f.write(i)
        f.write('\n')

print('найдено повторов:', already)